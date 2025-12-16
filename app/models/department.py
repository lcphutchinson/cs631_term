"""ORM logic for the Department table"""

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, func, text
from sqlalchemy.orm import relationship

from app import ModelBase

class Department(ModelBase):
    __tablename__ = "department"

    active  = Column(Boolean, server_default=text('TRUE'), nullable=False)
    num     = Column(Integer, primary_key=True)
    name    = Column(String(32), nullable=False)
    div     = Column(String(32), ForeignKey("division.name"), nullable=False)
    head    = Column(Integer, ForeignKey("employee.num"), nullable=False)
    dt_est  = Column(DateTime, server_default=func.now(), nullable=False)
    budget  = Column(Float, nullable=False)

    r_division = relationship("Division", back_populates="r_department")
    r_employee = relationship("Employee", back_populates="r_department")
    r_room = relationship("Room", back_populates="r_department")
    r_department_employee = relationship("DepartmentEmployee", back_populates="r_department")
