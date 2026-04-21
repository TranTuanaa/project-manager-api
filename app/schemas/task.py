from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.models.task import TaskPriority, TaskStatus

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    priority: TaskPriority = TaskPriority.medium

class TaskCreate(TaskBase):
    project_id: int

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    project_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
