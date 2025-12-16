"""ORM logic for the Employee table"""

from sqlalchemy import Boolean, Column, Float, Integer, String, text
from sqlalchemy.orm import relationship

from app import ModelBase

class Employee(ModelBase):
    __tablename__ = "employee"

    active  = Column(Boolean, nullable=False, server_default=text('TRUE'))
    hourly  = Column(Boolean, nullable=False)
    num     = Column(Integer, primary_key=True)
    f_name  = Column(String(50), nullable=False)
    m_name  = Column(String(50), nullable=True)
    l_name  = Column(String(50), nullable=False)
    salary  = Column(Float, nullable=False)
    street  = Column(String(32), nullable=False)
    city    = Column(String(32), nullable=False)
    state   = Column(String(32), nullable=False)
    zip     = Column(String(16), nullable=False)

    r_office = relationship("Office", back_populates="r_employee")
    r_work_record = relationship("WorkRecord", back_populates="r_employee")
    r_division = relationship("Division", back_populates="r_employee")
    r_department = relationship("Department", back_populates="r_employee")
    r_project = relationship("Project", back_populates="r_employee")
    r_project_assignment = relationship("ProjectAssignment", back_populates="r_employee")
    r_department_employee = relationship("DepartmentEmployee", back_populates="r_employee")
    r_consultant = relationship("Consultant", back_populates="r_employee")
    r_tax_record = relationship("TaxRecord", back_populates="r_employee")
