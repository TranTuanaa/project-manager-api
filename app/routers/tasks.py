from fastapi import APIRouter

task_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@task_router.get("/")
def get_all_tasks():
    return {"message": "List of all tasks"}

@task_router.get("/{task_id}")
def get_task(task_id: int):
    return {"message": f"Task with id {task_id}"}

@task_router.post("/")
def create_task():
    return {"message": "Task created successfully"}