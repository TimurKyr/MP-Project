from typing import Optional

from pydantic import BaseModel
from datetime import date


class DocumentResponse(BaseModel):
    id: int
    type_id: int
    number: str
    date: date

    class Config:
        orm_mode = True


class DocumentCreateRequest(BaseModel):
    type_id: int
    number: str
    date: date


class DocumentUpdateRequest(BaseModel):
    type_id: Optional[int] = None
    number: Optional[str] = None
    date: Optional[date] = None


class DocumentTypeResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class DocumentTypeCreateRequest(BaseModel):
    name: str


class DocumentTypeUpdateRequest(BaseModel):
    name: str
