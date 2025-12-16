"""Data models for CRUD operations on Employee entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class EmployeeCreate(BaseModel):
    hourly: bool = Field(..., description="pay status for this employee")
    f_name: str = Field(..., min_length=1, max_length=50, description="First name")
    m_name: Optional[str] = Field(None, min_length=1, max_length=50, description="Middle name")
    l_name: str = Field(..., min_length=1, max_length=50, description="Last name")
    salary: float = Field(..., description="Salary for this employee")
    street: str = Field(..., min_length=1, max_length=32, description="Address street")
    city: str = Field(..., min_length=1, max_length=32, description="Address city")
    state: str = Field(..., min_length=1, max_length=32, description="Address state")
    zip: str = Field(..., min_length=1, max_length=16, description="Address zip")

    model_config = ConfigDict(from_attributes=True)

class EmployeeRead(BaseModel):
    active: bool
    hourly: bool
    num: int
    f_name: str
    m_name: Optional[str]
    l_name: str
    salary: float
    street: str
    city: str
    state: str
    zip: str

    model_config = ConfigDict(from_attributes=True)

class EmployeeVerboseRead(EmployeeRead):
    room: Optional[int]
    phone: Optional[int]
    aff_type: Optional[str]
    aff_name: Optional[str]

class SafeEmployeeRead(BaseModel):
    num: int
    hourly: bool
    salary: float
    f_name: str
    l_name: str

    model_config = ConfigDict(from_attributes=True)

class EmployeeUpdate(BaseModel):
    active: Optional[bool] = Field(False, description="New active status for this employee")
    hourly: Optional[bool] = Field(False, description="New employment type for this employee")
    f_name: Optional[str] = Field(None, min_length=1, max_length=50, description="New first name for this employee")
    m_name: Optional[str] = Field(None, min_length=1, max_length=50, description="New middle name for this employee")
    l_name: Optional[str] = Field(None, min_length=1, max_length=50, description="New last name for this employee")
    salary: Optional[float] = Field(None, description="New salary for this employee")
    street: Optional[str] = Field(None, min_length=1, max_length=32, description="New address street for this employee")
    city: Optional[str] = Field(None, min_length=1, max_length=32, description="New address city for this employee")
    state: Optional[str] = Field(None, min_length=1, max_length=32, description="New address state for this employee")
    zip: Optional[str] = Field(None, dmin_length=1, max_length=16, desciption="New address ZIP for this employee")

    model_config = ConfigDict(from_attributes=True)
