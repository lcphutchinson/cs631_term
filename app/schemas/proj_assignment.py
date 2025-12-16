"""Data models for CRUD operations on Employee Project relations"""

from pydantic import BaseModel, ConfigDict, Field

class ProjectAssignmentCreate(BaseModel):
    employee: int = Field(..., description="Employee# for this relation")
    project: int = Field(..., description="Project# for this relation")
    
    model_config = ConfigDict(from_attributes=True)

class ProjectAssignmentRead(BaseModel):
    employee: int
    project: int

    model_config = ConfigDict(from_attributes=True)
