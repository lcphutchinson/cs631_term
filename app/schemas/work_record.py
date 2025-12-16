"""Data models for CRUD operations on Work Record entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class WorKRecordCreate(BaseModel):
    employee: int = Field(..., description="Employee# associated with this record")
    project: int = Field(..., description="Project# associated with this record")
    start_date: Optional[datetime] = Field(None, description="Date work begins")
    end_date: Optional[datetime] = Field(None, description="Date work ends")
    role: str = Field(..., min_length=1, max_length=32, description="Employee role during work period")

    model_config = ConfigDict(from_attributes=True)

class WorkRecordRead(BaseModel):
    employee: int
    project: int
    start_date: datetime
    end_date: datetime
    role: str

    model_config = ConfigDict(from_attributes=True)

class WorkRecordUpdate(BaseModel):
    employee: Optional[int] = Field(None, description="New employee for this record")
    project: Optional[int] = Field(None, description="New project for this record")
    start_date: Optional[datetime] = Field(None, description="New start date for this record")
    end_date: Optional[datetime] = Field(None, description="New end date for this record")
    role: Optional[str] = Field(None, min_length=1, max_length=32, description="New role for this record")

    model_config = ConfigDict(from_attributes=True)

