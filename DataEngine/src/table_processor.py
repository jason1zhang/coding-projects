from HermesClient import HermesClient
from Helper import load_config, setup_logging, handle_exception, send_log_email, reset_log_stream
from datetime import datetime, timedelta
from TableDataEngine import TableDataEngine
from SqlConfig import SqlConfig

def main():
    """
    Main function to process SQL queries based on the provided configuration.

    This function sets up logging, loads the configuration settings, and attempts to process the queries up to a maximum number of retries.
    """
    MAX_RETRIES = 5
    log_stream = setup_logging()
    config = load_config('./config/engine_config.json')

    for i in range(MAX_RETRIES):
        try:
            process_queries(config)
            break
        except Exception as e:
            handle_exception(e, i, MAX_RETRIES)

    send_log_email(log_stream, config)
    reset_log_stream(log_stream)

def process_queries(config):
    """
    Processes a set of SQL queries based on the provided configuration.

    This function creates a HermesClient and a SqlConfig object using the provided configuration.
    It then iterates over each query in the SqlConfig object, calculates the start and end dates for the query,
    and processes the query using a TableDataEngine object.

    Args:
        config (dict): A dictionary containing the configuration settings. It should include the following keys:
            - 'user_name': The username for the HermesClient
            - 'password': The password for the HermesClient
            - 'hdmi-queue': The queue name for the HermesClient
            - 'sql_config_file': The path to the SQL configuration file.
    """
    with HermesClient(config['user_name'], config['password'], config['hdmi_queue']) as hc:
        sql_config = SqlConfig(config['sql_config_file'])

        for query_name in sql_config.configs.keys():
            query_config = sql_config.get_query_config(query_name)
            start_date = datetime.strptime(query_config.start_date, '%Y-%m-%d') - timedelta(days=2)
            end_date = datetime.now() if query_config.end_dt == 'current_date' else datetime.strptime(query_config.end_dt, '%Y-%m-%d')

            engine = TableDataEngine(hc, start_date, end_date)
            engine.process_query_config(query_name, query_config)

# Main program
if __name__ == "__main__":
    main()