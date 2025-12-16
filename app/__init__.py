import os
from sqlalchemy.orm import declarative_base

DatabaseURL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:postgres@localhost:5432/fastapi_db"
)
ModelBase = declarative_base()
