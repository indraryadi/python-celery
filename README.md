# Terms:
- Producer: the application that sends tasks to the broker
- Broker (Redis/RabbitMQ): a message queue system that receives stores, and delivers tasks between producers and workers 
- Celery worker: a process that consumes tasks from the broker queue and executes them 
- Task: a python function registered with Celery that can be executed asynchronously
- Result backend (Redis/DB): a storage system where task results and states are saved
- Celery beat: a scheduler that periodically send task to the broker 
- Worker concurency: number of tasks a worker can process in parallel

# How celery work?
- The producer sends a task to a message broker (Redis or RabbitMQ).
- The broker stores it in a queue. 
- Celery workers continuously read from the queue and execute the tasks asynchronously
- The result is stored on the Result backend (Redis or DB) if configured
- For scheduled tasks, Celery beat periodically sends tasks to the broker 

# How to run this project
- run all service: docker compose up -d --build
- check all container is up: docker ps
- open http://localhost:8000/docs
- to check what is happening on the celery, monitor the log inside worker: docker logs -f celery-celery-worker-1
- send a post request
- watch the task was received by worker and give the result
```
[2026-05-06 06:40:14,461: INFO/MainProcess] Task app.tasks.random_number[50fa35aa-125c-4288-a3d3-bab84ab36974] received
[2026-05-06 06:40:19,468: INFO/ForkPoolWorker-8] Task app.tasks.random_number[50fa35aa-125c-4288-a3d3-bab84ab36974] succeeded in 5.006302157999926s: 8
```
- copy the task id from post response, then send a get request to check the detail
- the result should be same with the log