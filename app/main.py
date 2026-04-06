from fastapi import FastAPI
from app.routers import tasks, auth
from app.database import engine, Base

app = FastAPI(
    title="Project Manager API",
    description="Backend API quản lý dự án và công việc với Authentication",
    version="1.0.0"
)

# Tạo tất cả bảng trong database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)           # Auth router
app.include_router(tasks.task_router)     # ← Sửa thành task_router

@app.get("/")
def read_root():
    return {"message": "Project Manager API is running successfully! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)