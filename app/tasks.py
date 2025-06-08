from fastapi import APIRouter, Security
from app.auth import oauth2_scheme

router = APIRouter()

@router.get("/tasks")
def read_tasks(token: str = Security(oauth2_scheme)):
    return [{"task": "Com segurança!"}]
