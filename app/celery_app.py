import os
from celery import Celery

celery_app = Celery(
    'worker',
    broker = os.getenv('CELERY_BROKER_URL'),
    backend = os.getenv('CELERY_BACKEND_URL'),
)

celery_app.conf.update(
    task_track_started=True,
)
celery_app.autodiscover_tasks(["app"])