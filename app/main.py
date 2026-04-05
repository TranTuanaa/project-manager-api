from fastapi import FastAPI
from app.routers.tasks import task_router   # ← Sửa dòng này

app = FastAPI(
    title="Project Manager API",
    description="Backend API quản lý dự án và công việc",
    version="1.0.0"
)

# Include router
app.include_router(task_router)   # ← Sửa dòng này

@app.get("/")
def read_root():
    return {"message": "Project Manager API is running successfully! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}