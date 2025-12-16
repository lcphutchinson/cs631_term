"""ORM logic for the Milestone table"""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app import ModelBase

class Milestone(ModelBase):
    __tablename__ = "milestone"

    num         = Column(Integer, primary_key=True)
    project     = Column(Integer, ForeignKey("project.num"), nullable=False)
    complete    = Column(Boolean, default=False, nullable=False)
    deadline    = Column(DateTime, nullable=True)
    description = Column(String(140), nullable=False)

    r_project = relationship("Project", back_populates="r_milestone")

