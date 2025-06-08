from fastapi import FastAPI
from app.auth import router as auth_router
from app.tasks import router as task_router
from app.database import Base, engine  # Se estiver usando ORM

app = FastAPI(title="TaskManager API")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])

print("Rotas registradas:")
for route in app.routes:
    print(f" {route.path} -> {route.name}")
