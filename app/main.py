from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # Needed so SQLAlchemy can register the tables.
from app.database import Base, engine
from app.routers import auth_router, project_router, task_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Project Manager API",
    description="Simple backend API for personal project and task management",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(project_router)


@app.get("/")
def root():
    return {"message": "Project Manager API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
