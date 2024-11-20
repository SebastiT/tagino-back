from pydantic import BaseModel
from datetime import date, datetime


# class DocumentBase(BaseModel):
  

class DocumentCreate(BaseModel):
    date: date  # Fecha con formato "YYYY-MM-DD"
    type: str
    grade: int
    section: str


class DocumentResponse(BaseModel):
    id: int
    date: date
    url: str
    type: str
    grade: int
    section: str
    report: bool
    upload_date: datetime

    class Config:
        orm_mode = True
