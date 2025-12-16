"ORM logic for the Project Assignment table"

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app import ModelBase

class ProjectAssignment(ModelBase):
    __tablename__ = "project_assignment"

    employee    = Column(Integer, ForeignKey("employee.num"), primary_key=True)
    project     = Column(Integer, ForeignKey("project.num"), primary_key=True)

    r_employee = relationship("Employee", back_populates="r_project_assignment")
    r_project = relationship("Project", back_populates="r_project_assignment")

