"""ORM logic for the Office table"""

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app import ModelBase

class Office(ModelBase):
    __tablename__ = "office"

    employee= Column(Integer, ForeignKey('employee.num'), primary_key=True)
    room    = Column(Integer, ForeignKey('room.num'), primary_key=True)
    phone   = Column(String(16), nullable=False)

    r_employee = relationship("Employee", back_populates="r_office")
    r_room = relationship("Room", back_populates="r_office")

