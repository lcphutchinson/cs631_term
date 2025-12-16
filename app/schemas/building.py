"""Data models for CRUD operations on Building entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional

from app.enums import AcquisitionType

class BuildingCreate(BaseModel):
    
    name: str = Field(..., min_length=1, max_length=32, description="Name of the building", example="Central King Building")
    acq_date: Optional[datetime] = Field(None, description="Time of building acquisition")
    acq_type: AcquisitionType = Field(..., description="Type of acquisition", example="Lease")
    expense: float = Field(..., description="Expense value for the acquisition")

    model_config = ConfigDict(from_attributes=True)

    @field_validator("acq_type", mode="before")
    @classmethod
    def validate_type(cls, s):
        return AcquisitionType.validate(s)

class BuildingRead(BaseModel):
    
    name: str
    acq_date: datetime
    acq_type: AcquisitionType
    expense: float

    model_config = ConfigDict(from_attributes=True)

class BuildingUpdate(BaseModel):

    acq_date: Optional[datetime] = Field(None, description="New building acquisition date")
    acq_type: Optional[AcquisitionType] = Field(None, description="New acquisition type")

    model_config = ConfigDict(from_attributes=True)

    @field_validator("acq_type", mode="before")
    @classmethod
    def validate_type(cls, s):
        if s is None: 
            return None
        return AcquisitionType.validate(s)






