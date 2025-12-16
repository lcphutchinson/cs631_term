"""Data models for CRUD operations on Milestone entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class MilestoneCreate(BaseModel):
    project: int = Field(..., description="Project associated with this milestone")
    completed: bool = Field(..., description="Completion status")
    deadline: Optional[datetime] = Field(None, description="Deadline for this milestone")
    description: str = Field(..., min_length=1, max_length=140, description="Description of this milestone")

    model_config = ConfigDict(from_attributes=True)

class MilestoneRead(BaseModel):
    project: int
    completed: bool
    deadline: Optional[datetime]
    description: str

    model_config = ConfigDict(from_attributes=True)

class MilestoneUpdate(BaseModel):
    completed: Optional[bool] = Field(None, description="New completion status for this milestone")
    deadline: Optional[datetime] = Field(None, description="New deadline for this milestone")
    description: Optional[string] = Field(None, min_length=1, max_length=140, description="New description for this milestone")

    model_config = ConfigDict(from_attributes=True)

