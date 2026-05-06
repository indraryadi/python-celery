from fastapi import FastAPI
from celery.result import AsyncResult

from app.tasks import random_number
from app.celery_app import celery_app

app = FastAPI()

@app.post("/tasks")
def create_task(max_value: int = 100):
    task = random_number.delay(max_value)
    return {"task_id": task.id}

@app.get("/tasks/{id}")
def get_task(id: str):
    result = AsyncResult(id, app = celery_app)

    if result.ready():
        return {
            "status": result.status,
            "result": result.result,
        }
    
    return {"status": result.status}