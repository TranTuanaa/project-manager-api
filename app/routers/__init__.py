from app.routers.auth import router as auth_router
from app.routers.projects import router as project_router
from app.routers.tasks import router as task_router

__all__ = ["auth_router", "project_router", "task_router"]
