"""ORM logic for the Department Employee table"""

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app import ModelBase

class DepartmentEmployee(ModelBase):
    __tablename__ = "department_employee"

    department  = Column(Integer, ForeignKey("department.num"), primary_key=True)
    employee    = Column(Integer, ForeignKey("employee.num"), primary_key=True)

    r_department = relationship("Department", back_populates="r_department_employee")
    r_employee = relationship("Employee", back_populates="r_department_employee")

    
