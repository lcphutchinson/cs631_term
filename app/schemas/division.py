"""Data models for CRUD operations on Division entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class DivisionCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=32, description="Name for this division")
    head: int = Field(..., description="Employee# for Division Head")
    dt_est: Optional[datetime] = Field(None, description="Date of Division establishment")
    budget: float = Field(..., description="Budget for this Division")

    model_config = ConfigDict(from_attributes=True)

class DivisionRead(BaseModel):
    active: bool
    name: str
    head: int
    dt_est: datetime
    budget: float

    model_config = ConfigDict(from_attributes=True)

class DivisionUpdate(BaseModel):
    active: Optional[bool] = Field(None, description="New activity status for this division")
    name: Optional[str] = Field(None, min_length=1, max_length=32, description="New name for this division")
    head: Optional[int] = Field(None, description="New lead for this division")
    dt_est: Optional[datetime] = Field(None, description="New establishement date for this division")
    budget: Optional[float] = Field(None, description="New budget for this division")

    model_config = ConfigDict(from_attributes=True)


