"""ORM logic for the Room table"""

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app import ModelBase

class Room(ModelBase):
    __tablename__ = "room"

    num     = Column(Integer, primary_key=True)
    building= Column(String(32), ForeignKey("building.name"), nullable=False)
    dept    = Column(Integer, ForeignKey("department.num"), nullable=False)
    area    = Column(Float, nullable=False)

    r_building = relationship("Building", back_populates="r_room")
    r_department = relationship("Department", back_populates="r_room")
    r_office = relationship("Office", back_populates="r_room")


