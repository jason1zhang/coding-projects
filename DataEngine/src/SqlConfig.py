import json
from typing import Dict
from QueryConfig import QueryConfig

class SqlConfig:
    def __init__(self, file_path: str):
        """
        Initialize SqlConfig instance.

        Args:
            file_path (str): Path to the json file containing SQL configurations.
        """
        self.configs: Dict[str, QueryConfig] = self.load_config(file_path)

    def load_config(self, file_path: str) -> Dict[str, QueryConfig]:
        """
        Load SQL configurations from a json file.

        Args:
            file_path (str): Path to the json file containing SQL configurations.

        Returns:
            Dict[str, QueryConfig]: A dictionary mapping query name to QueryConfig instances.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
        return {key: QueryConfig(value) for key, value in data.items()}
    
    def get_query_config(self, query_name: str) -> QueryConfig:
        """
        Get the QueryConfig instance for a specific query.

        Args:
            query_name (str): The name of the query.

        Returns:
            QueryConfig: The QueryConfig instance for the specific query.
        """
        return self.configs[query_name]