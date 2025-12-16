import logging as logs

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from app import DatabaseURL, ModelBase

class DatabaseClient():
    _instance: 'DatabaseClient' = None
    _is_configured: bool = False

    def __new__(cls) -> 'DatabaseClient': 
        if not cls._instance:
            cls._instance = super(DatabaseClient, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if self._is_configured:
            return
        try:
            self.engine = create_engine(DatabaseURL, echo=True)
        except SQLAlchemyError as e:
            logs.critical(f"Error creating SQLAlchemy Engine: {e}")
            raise
        self.model_base = ModelBase
        self.session_agent = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
        self._is_configured = True

    def get_session(self):
        session = self.session_agent()
        try:
            yield session
        finally:
            session.close()

