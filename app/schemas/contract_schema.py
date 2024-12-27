from pydantic import BaseModel
from datetime import date


class ContractResponse(BaseModel):
    id: int
    object_cost_kzt: float
    object_cost_usd: float
    market_cost_kzt: float
    date: date

    class Config:
        orm_mode = True


class ContractCreateRequest(BaseModel):
    object_cost_kzt: float
    object_cost_usd: float
    market_cost_kzt: float
    date: date
