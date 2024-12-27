from typing import Optional

from pydantic import BaseModel
from datetime import date


class OwnerResponse(BaseModel):
    id: int
    bin: int
    name: str
    abbreviation: str
    mp_share: int
    create_user: str
    update_user: Optional[str] = None
    create_date: date
    update_date: Optional[date] = None

    class Config:
        orm_mode = True


class OwnerCreateRequest(BaseModel):
    create_user: str
    bin: int
    name: str
    abbreviation: str
    mp_share: int


class OwnerUpdateRequest(BaseModel):
    update_user: str
    bin: Optional[int] = None
    name: Optional[str] = None
    abbreviation: Optional[str] = None
    mp_share: Optional[int] = None
