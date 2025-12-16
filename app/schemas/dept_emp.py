"""Data models for CRUD operations on Department Employee relations"""

from pydantic import BaseModel, ConfigDict, Field

class DepartmentEmployeeCreate(BaseModel):
    department: int = Field(..., description="Department for this relation")
    employee: int = Field(..., description="Employee for this relation")

    model_config = ConfigDict(from_attributes=True)

class DepartmentEmployeeRead(BaseModel):
    department: int
    employee: int

    model_config = ConfigDict(from_attributes=True)
