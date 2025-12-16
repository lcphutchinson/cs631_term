"""ORM logic for WorkRecord table"""

import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app import ModelBase

class WorkRecord(ModelBase):
    __tablename__ = "work_record"

    employee    = Column(Integer, ForeignKey("employee.num"), primary_key=True)
    project     = Column(Integer, ForeignKey("project.num"), primary_key=True)
    start_date  = Column(DateTime, primary_key=True, default=func.now())
    end_date    = Column(DateTime, nullable=True)
    role        = Column(String(32), nullable=False)

    r_employee = relationship("Employee", back_populates="r_work_record")
    r_project = relationship("Project", back_populates="r_work_record")
    
    
