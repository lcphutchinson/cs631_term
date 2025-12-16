"""ORM logic for Division table"""

from sqlalchemy import Boolean, Column, DateTime, Integer, Float, ForeignKey, String, func, text
from sqlalchemy.orm import relationship

from app import ModelBase

class Division(ModelBase):
    __tablename__ = "division"

    active  = Column(Boolean, server_default=text('TRUE'), nullable=False)
    name    = Column(String(32), primary_key=True)
    head    = Column(Integer, ForeignKey("employee.num"), nullable=False)
    dt_est  = Column(DateTime, server_default=func.now(), nullable=False)
    budget  = Column(Float, nullable=False)

    r_department = relationship("Department", back_populates="r_division")
    r_employee = relationship("Employee", back_populates="r_division")
    r_consultant = relationship("Consultant", back_populates="r_division")
