from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.task import Task, TaskStatus, TaskPriority
from app.schemas.task import TaskCreate, TaskResponse
from app.core.deps import get_current_user
from app.models.user import User

# Dùng task_router để khớp với main.py
task_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# GET all tasks của user hiện tại
@task_router.get("/", response_model=List[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks

# CREATE task
@task_router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = Task(
        title=task.title,
        description=task.description,
        status=TaskStatus(task.status),
        priority=TaskPriority(task.priority),
        user_id=current_user.id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# GET task by id
# GET all tasks của user hiện tại
@task_router.get("/", response_model=List[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks

# UPDATE task
@task_router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
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
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return None