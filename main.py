from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class task(BaseModel):
    tite: str
    descrption: str
    state : str
    

@app.post('/')
def create_task():
    


