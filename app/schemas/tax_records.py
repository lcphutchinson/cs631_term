"""Data models for CRUD operations on Tax Record entities"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class TaxRecordCreate(BaseModel):
    employee: int = Field(..., description="Employee associated with this tax record")
    date: datetime = Field(..., description="Time of tax withholding")
    f_tax: float = Field(..., description="Federal tax withheld")
    s_tax: float = Field(..., description="State tax withheld")
    m_tax: float = Field(..., description="Other taxes withheld")

    model_config = ConfigDict(from_attributes=True)

class TaxRecordRead(BaseModel):
    employee: int
    date: datetime
    f_tax: float
    s_tax: float
    m_tax: float

    model_config = ConfigDict(from_attributes=True)

