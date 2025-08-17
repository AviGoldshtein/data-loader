from services.dal.DBconection import DConnector


class DataLoader:
    def __init__(self):
        self.connector = DConnector()

    def load_data(self):
        conn = self.connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data")
        rows = cursor.fetchall()
        return rows
