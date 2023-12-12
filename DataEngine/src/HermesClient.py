import pyodbc
import pandas as pd
import os
from pandas import DataFrame
from typing import List, Tuple

WRITE_TIMEOUT = READ_TIMEOUT = int(os.getenv('HADOOP_READ_TIMEOUT', '0'))

class HermesClient:
    """
    A client for interacting with the Hermes database.

    This client provides methods to read from and write to the Hermes database.
    It uses the pyodbc library to establish a connection to the database.

    Attributes:
        username (str)： The username for the Hermes database.
        password (str): The password for the Hermes database.
        queue(str): The queue for the Hermes database.
        conn (pyodbc.Connection): The connection to the Hermes database.

    Methods:
        __enter__: Establishes a connection to the Hermes database.
        __exit__: Closees the connection to the Hermes database.
        read(query: str, **params) -> DataFrame: Executes a read query on the Hermes databases.
        write(queries: List[str]): Executes a list of write queries on the Hermes database.
    """
    def __init__(self, username: str, password: str, queue: str = None) -> None:
        self.username = username
        self.password = password
        self.queue = queue
        self.conn = None

    def __enter__(self):
        config_string = f'DSN=Hermes;UID={self.username};PWD={self.password}'
        if self.queue:
            config_string += f";SSP_queue={self.queue}"
        self.conn = pyodbc.connect(config_string, auto_commit=True)
        setting = "set spark.sql.thriftserver.shareResult=false"
        self.conn.execute(setting)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def read(self, query: str, **params) -> DataFrame:
        return pd.read_sql(query.format(**params), self.conn)
    
    def write(self, *queries):
        cursor = self.conn.cursor()
        for query in queries:
            cursor.execute(query)
        cursor.commit()
        cursor.close()