from fastapi import APIRouter, Security, Depends, HTTPException, status
from app.auth import oauth2_scheme
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

db_dependency = Depends(database.get_db)

@router.get("/tasks")
def read_tasks(db: Session = db_dependency):
    tasks = db.query(models.Task).all()
    return tasks

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = db_dependency):
    db_task = models.Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
