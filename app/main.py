from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.api.routes.tasks import router as tasks_router
from app.core.config import get_settings
from app.db.session import Base, engine, get_db
from app.models.task import Task

settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok", "message": "Task Manager API is running"}


app.include_router(tasks_router)
