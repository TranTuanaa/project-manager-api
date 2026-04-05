from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.task import Task, TaskStatus, TaskPriority
from app.schemas.task import TaskCreate, TaskResponse

task_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# GET all tasks
@task_router.get("/", response_model=List[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

# GET task by id
@task_router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# CREATE new task
@task_router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(
        title=task.title,
        description=task.description,
        status=TaskStatus(task.status),
        priority=TaskPriority(task.priority)
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# UPDATE task
@task_router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.title = task_update.title
    task.description = task_update.description
    task.status = TaskStatus(task_update.status)
    task.priority = TaskPriority(task_update.priority)
    
    db.commit()
    db.refresh(task)
    return task

# DELETE task
@task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return None