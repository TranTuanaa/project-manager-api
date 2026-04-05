from fastapi import FastAPI

app = FastAPI(
    title="Project Manager API",
    description="Backend API quản lý dự án và công việc",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Project Manager API đang chạy tốt! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}