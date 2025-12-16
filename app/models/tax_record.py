"""ORM logic for the Tax Record table"""
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Float, Integer, func
from sqlalchemy.orm import relationship

from app import ModelBase

class TaxRecord(ModelBase):
    __tablename__ = "tax_record"

    employee    = Column(Integer, ForeignKey("employee.num"), primary_key=True)
    date        = Column(DateTime, primary_key=True, default=func.now())
    f_tax       = Column(Float, nullable=False)
    s_tax       = Column(Float, nullable=False)
    m_tax       = Column(Float, nullable=False)

    r_employee = relationship("Employee", back_populates="r_tax_record")
