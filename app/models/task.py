from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.database import Base

class TaskStatus(str, enum.Enum):
    todo = "todo"
    doing = "doing"
    done = "done"

class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.todo)
    priority = Column(Enum(TaskPriority), default=TaskPriority.medium)
    
    # Liên kết với User (ai tạo task)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Liên kết với Project (task thuộc project nào)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship
    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"