from fastapi import FastAPI
from app.routers import auth
from app.routers.tasks import task_router
from app.routers.projects import router as project_router

from app.database import engine, Base

# Import models
from app.models.user import User
from app.models.task import Task
from app.models.project import Project

app = FastAPI(
    title="Project Manager API",
    description="Backend API quản lý dự án và công việc",
    version="1.0.0"
)

# Tạo database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(project_router, prefix="/projects", tags=["projects"])

@app.get("/")
def read_root():
    return {"message": "Project Manager API is running on Render! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}