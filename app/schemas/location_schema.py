from typing import Optional

from pydantic import BaseModel


class LocationResponse(BaseModel):
    location: Optional[dict]

    class Config:
        orm_mode = True


class LocationCreateRequest(BaseModel):
    num: str
    sub_num: Optional[str]
    street_name: Optional[str]
    locality_name: Optional[str]
    country_name: Optional[str]


# class LocationCreateResponse(BaseModel):
#


class AddressBase(BaseModel):
    street_id: int
    num: str
    sub_num: str


class AddressCreate(AddressBase):
    pass


class AddressResponse(AddressBase):
    id: int

    class Config:
        orm_mode = True


class StreetBase(BaseModel):
    locality_id: int
    name: int


class StreetCreate(StreetBase):
    pass


class StreetResponse(StreetBase):
    id: int

    class Config:
        orm_mode = True


class LocalityBase(BaseModel):
    country_id: int
    name: int


class LocalityCreate(LocalityBase):
    pass


class LocalityResponse(LocalityBase):
    id: int

    class Config:
        orm_mode = True


class CountryBase(BaseModel):
    name: int


class CountryCreate(CountryBase):
    pass

    class Config:
        orm_mode = True


class CountryResponse(CountryBase):
    id: int

    class Config:
        orm_mode = True

