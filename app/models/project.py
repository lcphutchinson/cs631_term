"""ORM logic for the Project table"""

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, func, text
from sqlalchemy.orm import relationship

from app import ModelBase

class Project(ModelBase):
    __tablename__ = "project"

    active  = Column(Boolean, server_default=text('TRUE'), nullable=False)
    num     = Column(Integer, primary_key=True)
    name    = Column(String(32), nullable=False)
    manager = Column(Integer, ForeignKey("employee.num"), nullable=False)
    launch  = Column(DateTime, server_default=func.now(), nullable=False)
    budget  = Column(Float, nullable=False)
    deadline= Column(DateTime, nullable=True)

    r_employee = relationship("Employee", back_populates="r_project")
    r_project_assignment = relationship("ProjectAssignment", back_populates="r_project")
    r_work_record = relationship("WorkRecord", back_populates="r_project")
    r_milestone = relationship("Milestone", back_populates="r_project")
