# Task Manager API

A simple FastAPI task manager backed by PostgreSQL.

## Features

- Create, list, update, and delete tasks
- SQLAlchemy ORM models
- PostgreSQL connection through `DATABASE_URL`
- Automatic table creation on startup for a simple local setup

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and adjust values if needed.

## Run

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API

- `GET /` - health check
- `GET /tasks` - list tasks
- `POST /tasks` - create a task
- `GET /tasks/{task_id}` - get one task
- `PATCH /tasks/{task_id}` - update a task
- `DELETE /tasks/{task_id}` - delete a task

## Example request

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Finish report","description":"Draft and review the final report"}'
```
