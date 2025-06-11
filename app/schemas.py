from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    is_done: bool = False

class Task(TaskCreate):
    id: int

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool
    user_id: int

    class Config:
        from_attributes = True
