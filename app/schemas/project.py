"""Data models for CRUD operations Project entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=32, description="Project title")
    manager: int = Field(..., description="Employee# for project lead")
    launch: datetime = Field(..., description="Project launch date")
    budget: float = Field(..., description="Budget for this project")
    deadline: Optional[datetime] = Field(None, description="Deadline for this project")

    model_config = ConfigDict(from_attributes=True)

class ProjectRead(BaseModel):
    active: bool
    num: int
    name: str
    manager: int
    launch: datetime
    budget: float
    deadline: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

class SimpleProjectRead(BaseModel):
    num: int
    name: str
    deadline: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

class ProjectUpdate(BaseModel):
    active: Optional[bool] = Field(None, description="New active status for this project")
    name: Optional[str] = Field(None, min_length=1, max_length=32, description="New name for this project")
    manager: Optional[int] = Field(None, description="New manager for this project")
    launch: Optional[datetime] = Field(None, description="New launch date for this project")
    budget: Optional[float] = Field(None, description="New budget for this project")
    deadline: Optional[datetime] = Field(None, description="New deadline for this project")

    model_config = ConfigDict(from_attributes=True)
