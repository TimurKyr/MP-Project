from pydantic import BaseModel
from datetime import date


class IndustryResponse(BaseModel):
    id: int
    name: str
    create_user: str
    update_user: str | None
    create_date: date
    update_date: date | None

    class Config:
        orm_mode = True


class IndustryCreateRequest(BaseModel):
    create_user: str
    name: str


class IndustryUpdateRequest(BaseModel):
    update_user: str
    name: str
