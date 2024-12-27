from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.location_repository import LocationRepository


class LocationService:
    @staticmethod
    def get_location_by_address_id(db: Session, address_id):
        """
        Retrieve a specific location by address ID.
        """
        location = LocationRepository.get_location_by_address_id(db, address_id)

        if not location:
            raise HTTPException(status_code=404, detail="Address not found")
        return location

    @staticmethod
    def create_location(db: Session, location_data):
        """
        Create a new location (address, street, locality, country).
        """
        return LocationRepository.create_location(db, location_data)

    @staticmethod
    def create_address(db: Session, address_data):
        """
        Create a new address in the database.
        """
        return LocationRepository.create_address(db, address_data)

    @staticmethod
    def create_street(db: Session, street_data):
        """
        Create a new street in the database.
        """
        return LocationRepository.create_street(db, street_data)

    @staticmethod
    def create_locality(db: Session, locality_data):
        """
        Create a new locality in the database.
        """
        return LocationRepository.create_locality(db, locality_data)

    @staticmethod
    def create_country(db: Session, country_data):
        """
        Create a new country in the database.
        """
        return LocationRepository.create_country(db, country_data)
