# Project Manager API

Personal backend practice project built with **FastAPI + SQLAlchemy**.

## Main Features

- JWT authentication with register and login
- CRUD projects
- CRUD tasks by project
- Each user can only access their own data

## Tech Stack

- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- SQLite
- Python 3.12.8

## Run Locally

```bash
git clone https://github.com/TranTuanaa/project-manager-api.git
cd project-manager-api
py -3.12 -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI: `http://127.0.0.1:8000/docs`

## Config

- `SECRET_KEY`: JWT secret key
- `DATABASE_URL`: database URL, default is `sqlite:///./project_manager.db`

## Main Endpoints

- `POST /auth/register`
- `POST /auth/login`
- `POST /projects/`
- `GET /projects/`
- `GET /projects/{project_id}`
- `PUT /projects/{project_id}`
- `DELETE /projects/{project_id}`
- `POST /tasks/`
- `GET /tasks/`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Example Task Payload

```json
{
  "title": "Design database",
  "description": "Create users, projects, tasks tables",
  "status": "todo",
  "priority": "medium",
  "project_id": 1
}
```
