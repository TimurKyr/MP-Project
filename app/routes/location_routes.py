from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.location_service import LocationService
from app.database.connection import get_db
from app.schemas.location_schema import LocationResponse, AddressResponse, StreetResponse, LocalityResponse, \
    CountryResponse, AddressCreate, StreetCreate, LocalityCreate, CountryCreate, LocationCreateRequest

router = APIRouter()


@router.get("/{address_id}", response_model=LocationResponse)
def get_location_by_address_id(address_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific location by address ID.
    """
    add = LocationService.get_location_by_address_id(db, address_id)

    return {"location": add}


@router.get("/", response_model=LocationResponse)
def create_location(location_data: LocationCreateRequest, db: Session = Depends(get_db)):
    """
    Create a new location (address, street, locality, country).
    """
    LocationService.create_location(db, location_data)


@router.post("/addresses", response_model=AddressResponse)
def create_address(address_data: AddressCreate, db: Session = Depends(get_db)):
    """
    Create a new address.
    """
    return LocationService.create_address(db, address_data)


@router.post("/streets", response_model=StreetResponse)
def create_street(street_data: StreetCreate, db: Session = Depends(get_db)):
    """
    Create a new street.
    """
    return LocationService.create_street(db, street_data)


@router.post("/localities", response_model=LocalityResponse)
def create_locality(locality_data: LocalityCreate, db: Session = Depends(get_db)):
    """
    Create a new locality.
    """
    return LocationService.create_locality(db, locality_data)


@router.post("/countries", response_model=CountryResponse)
def create_country(country_data: CountryCreate, db: Session = Depends(get_db)):
    """
    Create a new country.
    """
    return LocationService.create_country(db, country_data)
