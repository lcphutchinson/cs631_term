"""Data models for CRUD operations on special Division Employee Consultant relations"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class ConsultantCreate(BaseModel):
    division: str = Field(..., min_length=1, max_length=32, description="Division for this relation")
    employee: int = Field(..., description="Employee for this relation")

    model_config = ConfigDict(from_attributes=True)

class ConsultantRead(BaseModel):
    division: str
    employee: int

    model_config = ConfigDict(from_attributes=True)

class AffiliationCreate(BaseModel):
    employee: int = Field(..., description="Employee for this affiliation")
    division: Optional[bool] = Field(False, description="Label for division Affiliation")
    department: Optional[bool] = Field(False, descirption="Label for department Affiliation")
    id: str = Field(..., description="Key label for Affiliation")

    model_config = ConfigDict(from_attributes=True)
