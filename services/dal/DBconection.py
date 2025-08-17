import mysql.connector
import os
import time

class DConnector:
    def __init__(self):
        self.conn = None

    def get_connection(self):
        if self.conn and self.conn.is_connected():
            return self.conn

        host = os.getenv("MYSQL_HOST")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        database = os.getenv("MYSQL_DATABASE")

        for _ in range(10):  # לנסות להתחבר 10 פעמים
            try:
                self.conn = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
                return self.conn
            except mysql.connector.Error:
                time.sleep(3)
        raise RuntimeError("Cannot connect to MySQL after several retries")

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            self.conn = None

    def __del__(self):
        self.close_connection()