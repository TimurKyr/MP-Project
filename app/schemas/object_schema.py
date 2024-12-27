from typing import Optional

from pydantic import BaseModel
from datetime import date
from fastapi import Query

from .owner_schema import OwnerCreateRequest
from .document_schema import DocumentCreateRequest
from .contract_schema import ContractCreateRequest


class ObjectGetAllRequest(BaseModel):
    status_id: Optional[int] = Query(None)
    class_name: Optional[str] = Query(None)
    owner_id: Optional[int] = Query(None)
    industry_id: Optional[int] = Query(None)
    locality_id: Optional[int] = Query(None)
    country_id: Optional[int] = Query(None)


class ObjectResponse(BaseModel):
    id: int
    name: str
    owner_id: int
    industry_id: int
    address_id: int
    year_construction: Optional[int] = None
    year_purchase: Optional[int] = None
    document_id: int
    contract_id: int
    class_name: str
    floors_below: Optional[int] = None
    floors_above: Optional[int] = None
    area_total: Optional[float] = None
    area_rentable: Optional[float] = None
    parking_closed: Optional[int] = None
    parking_open: Optional[int] = None
    plot_owned: Optional[float] = None
    plot_rent: Optional[float] = None
    status_id: int
    create_user: str
    update_user: Optional[str] = None
    create_date: date
    update_date: Optional[date] = None

    class Config:
        orm_mode = True


class OwnerCreate(OwnerCreateRequest):
    create_user: Optional[str] = None


class ObjectCreateRequest(BaseModel):
    create_user: str
    name: str
    owner: OwnerCreate
    industry_id: int
    address_id: int
    year_construction: Optional[int] = None
    year_purchase: Optional[int] = None
    document: DocumentCreateRequest
    contract: ContractCreateRequest
    class_name: str
    floors_below: Optional[int] = None
    floors_above: Optional[int] = None
    area_total: Optional[float] = None
    area_rentable: Optional[float] = None
    parking_closed: Optional[int] = None
    parking_open: Optional[int] = None
    plot_owned: Optional[float] = None
    plot_rent: Optional[float] = None
    status_id: int


class ObjectUpdateRequest(BaseModel):
    update_user: str
    name: Optional[str] = None
    owner: Optional[OwnerCreate] = None
    industry_id: Optional[int] = None
    address_id: Optional[int] = None
    year_construction: Optional[int] = None
    year_purchase: Optional[int] = None
    document: Optional[DocumentCreateRequest] = None
    contract: Optional[ContractCreateRequest] = None
    class_name: Optional[str] = None
    floors_below: Optional[int] = None
    floors_above: Optional[int] = None
    area_total: Optional[float] = None
    area_rentable: Optional[float] = None
    parking_closed: Optional[int] = None
    parking_open: Optional[int] = None
    plot_owned: Optional[float] = None
    plot_rent: Optional[float] = None
    status_id: Optional[int] = None
