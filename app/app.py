from services.dal.data_loader import DataLoader
from fastapi import FastAPI

app = FastAPI()
data_loader = DataLoader()

@app.get("/get_data")
def get_data():
    data = data_loader.load_data()
    return data