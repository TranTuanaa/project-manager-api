# Project Manager API

A RESTful backend API for managing projects and tasks, built with **FastAPI** and **SQLAlchemy**.

## Links

- Repository: https://github.com/TranTuanaa/project-manager-api
- Live API: https://project-manager-api-5gkz.onrender.com
- API Docs: https://project-manager-api-5gkz.onrender.com/docs
- Health Check: https://project-manager-api-5gkz.onrender.com/health

## Main Features

- JWT-based authentication with register and login
- Full CRUD operations for projects
- Full CRUD operations for tasks within projects
- User-scoped access control for private data

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

API Docs:
- Local: `http://127.0.0.1:8000/docs`
- Live: `https://project-manager-api-5gkz.onrender.com/docs`

## API Notes

- `GET /` returns a simple service status response
- `GET /health` returns `{"status": "healthy"}`
- All `/projects/*` and `/tasks/*` endpoints require `Authorization: Bearer <access_token>`

## Environment Variables

- `SECRET_KEY`: JWT signing key
- `DATABASE_URL`: database connection string, defaults to `sqlite:///./project_manager.db`

## Main Endpoints

Public:
- `POST /auth/register`
- `POST /auth/login`
- `GET /`
- `GET /health`

Protected:
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

## Sample Task Payload

```json
{
  "title": "Design database",
  "description": "Create users, projects, tasks tables",
  "status": "todo",
  "priority": "medium",
  "project_id": 1
}
```
