import time
import random
from app.celery_app import celery_app

@celery_app.task
def random_number(max_value: int):
    time.sleep(5)
    return random.randint(0, max_value)