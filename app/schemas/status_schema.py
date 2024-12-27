from typing import Optional

from pydantic import BaseModel
from datetime import date


class StatusResponse(BaseModel):
    id: int
    name: str
    create_user: str
    update_user: Optional[str] = None
    create_date: date
    update_date: Optional[date] = None

    class Config:
        orm_mode = True


class StatusCreateRequest(BaseModel):
    create_user: str
    name: str


class StatusUpdateRequest(BaseModel):
    update_user: str
    name: str
