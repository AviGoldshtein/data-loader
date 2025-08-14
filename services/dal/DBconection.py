import mysql.connector
import os
from dotenv import load_dotenv


class DConnector:

    load_dotenv()

    def __init__(self):
        host = os.getenv("#####")
        user = os.getenv("#####")
        port_str = os.getenv("#####")
        password = os.getenv("#####")
        database = os.getenv("#####")
        try:
            port = int(port_str)
        except (ValueError, TypeError):
            raise ValueError(f"invalid port : {port_str}.")

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def get_connection(self):
        return self.conn

    def close_connection(self):
        self.conn.close()