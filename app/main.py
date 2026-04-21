from fastapi import FastAPI

from app.database import Base, engine
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from app.routers import auth
from app.routers.projects import router as project_router
from app.routers.tasks import task_router

app = FastAPI(
    title="Project Manager API",
    description="Backend API quan ly du an va cong viec",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(task_router)
app.include_router(project_router)

@app.get("/")
def read_root():
    return {"message": "Project Manager API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
