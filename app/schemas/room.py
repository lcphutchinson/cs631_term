"""Data model for CRUD operations on Room entities"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class RoomCreate(BaseModel):
    building: str = Field(..., min_length=1, max_length=32, description="Parent building for room")
    dept: int = Field(..., description="Department overseeing room")
    area: float = Field(..., description="Room area")

    model_config = ConfigDict(from_attributes=True)

class RoomRead(BaseModel):
    num: int
    building: str
    dept: int
    area: float

    model_config = ConfigDict(from_attributes=True)

class RoomUpdate(BaseModel):
    building: Optional[str] = Field(None, min_length=1, max_length=32, description="New building for this room")
    dept: Optional[int] = Field(None, description="New department for this room")
    area: Optional[float] = Field(None, description="New area for this room")

    model_config = ConfigDict(from_attributes=True)


