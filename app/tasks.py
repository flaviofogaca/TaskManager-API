from fastapi import APIRouter, Security, Depends, HTTPException, status
from app.auth import oauth2_scheme
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import get_db
from app.schemas import TaskResponse, TaskUpdate
from app.auth import get_current_user
from app.models import User


router = APIRouter()

db_dependency = Depends(database.get_db)

@router.get("/tasks")
def read_tasks(db: Session = db_dependency):
    tasks = db.query(models.Task).all()
    return tasks

@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        is_done=task.is_done,
        user_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.is_done is not None:
        task.is_done = task_update.is_done

    db.commit()
    db.refresh(task)
    return task

