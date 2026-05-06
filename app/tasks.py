import time
import random

from app.celery_app import celery_app
from app.db import update_task_record

@celery_app.task(bind=True)
def random_number(self, max_value: int):
    print("inside task/random_number")
    try:
        time.sleep(10)
        print(f"type of max_value: {type(max_value)}")
        result = random.randint(0, int(max_value))
        update_task_record(self.request.id, "SUCCESS", str(result))
        return result
    except Exception as e:
        update_task_record(self.request.id, "FAILURE", str(e))
        raise
    