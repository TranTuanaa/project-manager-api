from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectResponse
from app.core.deps import get_current_user

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)

# Create new project
@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project: ProjectCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    db_project = Project(
        name=project.name,
        description=project.description,
        status=project.status,
        owner_id=current_user.id
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Get all projects of current user
@router.get("/", response_model=List[ProjectResponse])
def get_all_projects(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    projects = db.query(Project).filter(Project.owner_id == current_user.id).all()
    return projects