class QueryConfig:
    def __init__(self, config_data: dict):
        """
        Initialize QueryConfig instance.

        Args:
            config_data (dict): A dictionary containing the configuration settings for a query.
        """
        self.sql_file: str = config_data['sql_file']
        self.target_table: str = config_data['target_table']
        self.target_delete_period: str = config_data['target_delete_period']
        self.target_attribute: str = config_data['target_attribute']
        self.table_prefix: str = config_data['table_prefix']
        self.start_date: str = config_data['start_date']
        self.end_dt: str = config_data['end_dt']
        self.is_run: int = config_data['is_run']

    def should_run(self) -> bool:
        """
        Check if the query should be run

        Returns:
            bool: True if the query should be run, False otherwise.
        """
        return self.is_run == 1
