"""ORM logic for the Building table"""

from enum import Enum as E

from sqlalchemy import Column, DateTime, Enum, Float, String, func
from sqlalchemy.orm import relationship

from app import ModelBase
from app.enums import AcquisitionType

class Building(ModelBase):
    __tablename__ = "building"

    name    = Column(String(32), primary_key=True)
    acq_date= Column(DateTime, server_default=func.now(), nullable=False)
    acq_type= Column(Enum(AcquisitionType), nullable=False)
    expense = Column(Float, nullable=False)

    r_room = relationship("Room", back_populates="r_building")
