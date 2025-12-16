"""Data models for CRUD operations on Department entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class DepartmentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=32, description="Name for this department")
    div: str = Field(..., min_length=1, max_length=32, description="Division organizing this department")
    head: int = Field(..., description="Employee# for department lead")
    dt_est: Optional[datetime] = Field(None, description="Date department established")
    budget: float = Field(..., description="Budget value for the department")

    model_config = ConfigDict(from_attributes=True)

class DepartmentRead(BaseModel):
    active: bool
    num: int
    name: str
    div: str
    head: int
    dt_est: datetime
    budget: float

    model_config = ConfigDict(from_attributes=True)

class DepartmentUpdate(BaseModel):
    active: Optional[bool] = Field(None, description="New activity status for this department")
    name: Optional[str] = Field(None, min_length=1, max_length=32, description="New name for this department")
    div: Optional[str] = Field(None, min_length=1, max_length=32, description="New Division for this department")
    head: Optional[int] = Field(None, description="New lead for this department")
    dt_est: Optional[datetime] = Field(None, description="New establishment date for this department")
    budget: Optional[float] = Field(None, description="New budget for this department")

    model_config = ConfigDict(from_attributes=True)
