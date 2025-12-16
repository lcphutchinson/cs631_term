"""Data models for CRUD operations on Office entities"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class OfficeCreate(BaseModel):
    employee: int = Field(..., description="Employee for this office")
    room: int = Field(..., description="Office Room#")
    phone: str = Field(..., min_length=1, max_length=16, description="Office Phone#")

    model_config = ConfigDict(from_attributes=True)

class OfficeRead(BaseModel):
    employee: int    
    room: int 
    phone: str

    model_config = ConfigDict(from_attributes=True)

class OfficeUpdate(BaseModel):
    employee: Optional[int] = Field(None, description="New Employee for this office")
    room: Optional[int] = Field(None, description="New Room for this office")
    phone: Optional[str] = Field(None, min_length=1, max_length=16, description="New Phone# for this office")

    model_config = ConfigDict(from_attributes=True)
