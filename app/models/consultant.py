"""ORM logic for the Consultant table"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app import ModelBase

class Consultant(ModelBase):
    __tablename__ = "consultant"

    division= Column(String(32), ForeignKey("division.name"), primary_key=True)
    employee= Column(Integer, ForeignKey("employee.num"), primary_key=True)

    r_division = relationship("Division", back_populates="r_consultant")
    r_employee = relationship("Employee", back_populates="r_consultant")


