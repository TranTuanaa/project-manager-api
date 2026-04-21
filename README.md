# Project Manager API

A simple backend API for managing projects and tasks.

Project scope is intentionally small: enough to show core backend skills for an intern application without adding unnecessary complexity.

## Links

- Repository: https://github.com/TranTuanaa/project-manager-api
- Live API: https://project-manager-api-5gkz.onrender.com
- API Docs: https://project-manager-api-5gkz.onrender.com/docs
- Health Check: https://project-manager-api-5gkz.onrender.com/health

## Main Features

- Register and login with JWT
- CRUD for projects
- CRUD for tasks inside projects
- Each user can only access their own data

## Tech Stack

- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- SQLite
- Python 3.12

## Run Locally

```bash
git clone https://github.com/TranTuanaa/project-manager-api.git
cd project-manager-api
py -3.12 -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Local API Docs: `http://127.0.0.1:8000/docs`

## API Notes

- `GET /` returns a simple service status response
- `GET /health` returns `{"status": "healthy"}`
- All `/projects/*` and `/tasks/*` endpoints require `Authorization: Bearer <access_token>`
- Passwords must be at least 8 characters

## Environment Variables

- `SECRET_KEY`: JWT signing key for development or deployment
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

## Sample Request Body

```json
{
  "title": "Design database",
  "description": "Create users, projects, tasks tables",
  "status": "todo",
  "priority": "medium",
  "project_id": 1
}
```
