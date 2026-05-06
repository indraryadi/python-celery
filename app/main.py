from fastapi import FastAPI

from app.db import init_db, create_task_record, get_task_record
from app.tasks import random_number

app = FastAPI()
init_db()

@app.post("/tasks")
def create_task(max_value: int = 100):
    print("INSIDE CREATE TASK")
    task = random_number.delay(max_value)
    print("DONE CREATE TASK")
    create_task_record(task.id)
    return {"task_id": task.id}

@app.get("/tasks/{id}")
def get_task(id: str):
    print(f"id: {id}")
    row = get_task_record(str(id))

    if not row:
        return {"error": "not found"} 
    
    return{
        "task_id": row[0],
        "status": row[1],
        "result": row[2],
    }