from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Criando o engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criando a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarando o Base
Base = declarative_base()
