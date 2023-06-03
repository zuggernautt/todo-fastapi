from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Task(BaseModel):
    id:int
    tite: str
    descrption: str
    state : str
    
@app.get('/')
def list_task():
    
    return ("Hello u")

@app.post('/create/')
def create_task(task:Task):
    return Task

@app.get('/read_one_task')


    


