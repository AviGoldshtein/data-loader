import mysql.connector
import os
from dotenv import load_dotenv


class DConnector:

    load_dotenv()

    def __init__(self):
        host = os.getenv("MYSQL_HOST")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        database = os.getenv("MYSQL_DATABASE")

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