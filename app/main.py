from fastapi import FastAPI

from app.routers import auth
from app.routers.tasks import task_router
from app.routers.projects import router as project_router   # Import project router

from app.database import engine, Base

# Import models để SQLAlchemy biết tạo bảng
from app.models.user import User
from app.models.task import Task
from app.models.project import Project

app = FastAPI(
    title="Project Manager API",
    description="Backend API quản lý dự án và công việc với Authentication",
    version="1.0.0"
)

# Tạo tất cả bảng trong database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(project_router, prefix="/projects", tags=["projects"])

@app.get("/")
def read_root():
    return {"message": "Project Manager API is running successfully! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)