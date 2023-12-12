from datetime import datetime, timedelta
from typing import Tuple, List
import logging
from termcolor import colored
from Helper import timer, get_color
from QueryConfig import QueryConfig
from HermesClient import HermesClient

class TableDataEngine:
    """
    TableDataEngine is a class for managing and processing data from tables.

    This class provides methods for reading data from a table, updating a table with new data, and processing a query configuration.

    Attributes:
        hc (HermesClient): An instance of the HermesClient class for database operations.
        start_date (datetime): The start date for data processing.
        end_date (datetime): The end date for data processing.

    Methods:
        read_data(target_table: str, target_attribute: str, target_period: str) -> int:
            Reads data from a target table for a specific period.

        update_table(new_table: str, target_table: str, target_delete_date: str) -> None:
            Updates a target table with data from a new table.

        process_query_config(query_name: str, query_config: QueryConfig) -> None:
            Processes a query configuration.
    """
    def __init__(self, client: HermesClient, start_date: datetime, end_date: datetime = datetime.now()):
        self.start_date = start_date
        self.end_date = end_date
        self.client = client

    def generate_table_in_days(self, table_prefix: str) -> List[Tuple[str, str, str]]:
        """
        Generate a list of days between start_date and end_date, inclusive.

        Args:
            table_prefix (str): The prefix for the table names.

        Returns:
            List[Tuple[str, str, str]]: A list of tuples, each containing the table name, the start date in 'YYYY-MM-DD' format, and the end date in 'YYYY-MM-DD' format.
        """
        days = []
        current_date = self.start_date

        while current_date <= self.end_date:
            table_name = f'{table_prefix}_{current_date.year}_{current_date.month:02d}_{current_date.day:02d}'
            start_date_formatted = current_date.strftime('%Y-%m-%d')
            end_date_formatted = start_date_formatted

            days.append((table_name, start_date_formatted, end_date_formatted))

            current_date += timedelta(days=1)

        return days
    
    def build_sql_query(self, sql_file_path: str, table_name: str, start_dt_str: str, end_dt_str: str) -> str:
        """
        Constructs a SQL query string from a template file, replacing placeholders with actual values.

        Args:
            sql_file_path (str): The path to the SQL template file.
            table_name (str): The name of the table.
        
        Returns:
            str: The constructed SQL query string.
        """
        with open(sql_file_path, 'r') as file:
            sql_query = file.read()

        sql_query = sql_query.replace('{table_name}', table_name)
        sql_query = sql_query.replace('{start_dt}', start_dt_str)
        sql_query = sql_query.replace('{end_dt}', end_dt_str)

        return sql_query
    
    def update_table(self, new_table: str, target_table: str, target_delete_date: str) -> None:
        """
        Updates a target table with data from a new table.

        This method performs three steps:
        1. Deletes existing data for a specific day from the target table.
        2. Inserts new data for the specific day from the new table into the target table.
        3. Drops the new table.

        Args:
            new_table (str): The name of the new table containing the data to be inserted.
            target_table (str): The name of the target table to be updated.
            target_delete_date (str): The date for which data should be deleted from the target table.

        Returns:
            None
        """
        year, month, day = new_table.split('_')[-3:]

        # Step 1: Delete the existing data for the specific day
        delete_sql = f"""
        DELETE FROM {target_table}
        WHERE
            date_format({target_delete_date}, 'yyyy-MM-dd) = '{year}-{month}-{day}'
        """

        try:
            self.client.write(delete_sql)
            logging.info(f"Step 3 => Deleted data for {year}-{month}-{day} from {target_table}")
        except Exception as e:
            logging.error(f"Step 3 => Error deleting data for {year}-{month}-{day} from {target_table}: {e}")
            return
        
        # Step 2: Insert the new data for the specific day
        insert_sql = f"""
        INSERT INTO {target_table}
        SELECT * FROM {new_table}
        """

        try:
            self.client.write(insert_sql)
            logging.info(f"Step 4 => Inserted data for {year}-{month}-{day} from {new_table} into {target_table}")
        except Exception as e:
            logging.error(f"Step 4 => Error inserting data for {year}-{month}-{day} from {new_table} into {target_table}: {e}")
            return
        
        # Step 3: Drop the new table
        drop_table_sql = f"""
        DROP TABLE {new_table}
        """
        try:
            self.client.write(drop_table_sql)
            logging.info(f"Step 5 => Dropped table {new_table}\n")
        except Exception as e:
            logging.error(f"Step 5 => Error dropping table {new_table}: {e}\n")
            return
        
    def read_data(self, target_table, target_attribute, target_period, target_date_str) -> int:
        query = f"SELECT sum({target_attribute}) FROM {target_table} WHERE {target_period} = '{target_date_str}'"
        result = self.client.read(query, target_period=target_period, target_attribute=target_attribute)

        return result.iat[0, 0]
    
    def process_query_config(self, query_name: str, query_config: QueryConfig) -> None:
        if query_config.should_run():
            tables = self.generate_table_in_days(query_config.table_prefix)

            for daily_table, start_dt_str, end_dt_str in tables:
                # Step 1: Read the data of previous day from target table for comparison
                logging.info("Step 1 => Start reading data from %s for start date %s", colored(query_config.target_table, 'green'), colored(start_dt_str, 'green'))

                pre_result = self.read_data(query_config.target_table, query_config.target_attribute, query_config.target_delete_period, start_dt_str)
                if pre_result is not None:
                    logging.info("\t   Read data with previous result: %s for start date: %s", colored(format(pre_result, ','), 'blue'), start_dt_str)
                else:
                    logging.info("\t   No previous result found for start date: %s", start_dt_str)

                # Step 2: Build and process the daily tables
                # Build the sql query for processing the daily tables
                sql = self.build_sql_query(query_config.sql_file, daily_table, start_dt_str, end_dt_str)
                sql_lst = sql.split(';')

                logging.info("Step 2 => Start processing %s for query %s", colored(daily_table, 'green'), colored(query_name, 'green'))
                try:
                    with timer(f"\t   Time spent on building table {daily_table}"):
                        self.client.write(*sql_lst)

                        # Read the data from newly created daily table for comparison
                        cur_result = self.read_data(daily_table, query_config.target_attribute, query_config.target_delete_period, start_dt_str)
                        if cur_result is not None:
                            logging.info("\t   Read data with current result: %s for start date: %s", colored(format(cur_result, ','), 'blue'), start_dt_str)
                            if pre_result is not None:
                                difference = cur_result - pre_result
                                percent_difference = abs(difference) / pre_result * 100
                                logging.info("\t   The difference between the current result and previous result is: %s%% (absolute difference: %s)", colored(format(percent_difference, '.2f'), get_color(percent_difference)), colored(format(difference, ','), 'blue'))
                            else:
                                logging.info("\t   No previous result found. Unable to calculate percent difference.")
                        else:
                            logging.info("\t   No current result found for start date: %s", start_dt_str)

                except Exception as e:
                    logging.error(f"Error processing table {daily_table}: {e}")
                    continue

                self.update_table(daily_table, query_config.target_table, query_config.target_delete_period)