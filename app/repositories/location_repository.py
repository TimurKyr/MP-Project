from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models.models import Address, Street, Locality, Country


class LocationRepository:
    @staticmethod
    def get_location_by_address_id(db: Session, address_id: int):
        """
        Retrieve a specific location by address ID.
        """
        address, street, locality, country = None, None, None, None

        address = db.query(Address).filter(Address.id == address_id).first()
        if address:
            street = db.query(Street).filter(Street.id == int(address.street_id)).first()
            if street:
                locality = db.query(Locality).filter(Locality.id == int(street.locality_id)).first()
                if locality:
                    country = db.query(Country).filter(Country.id == int(locality.country_id)).first()
        else:
            raise HTTPException(status_code=404, detail="Address not found")

        location = {
            "address": address.num + '/' + address.sub_num,
            "street": street.name if street else "",
            "locality": locality.name if locality else "",
            "country": country.name if country else ""
        }

        return location

    @staticmethod
    def create_location(db: Session, location_data):
        """
        Create a new location (address, street, locality, country).
        """
        address = db.query(Address).filter(and_(Address.num == str(location_data.num))).first()
        street = db.query(Street).filter(Street.name == str(location_data.street_name)).first()
        locality = db.query(Locality).filter(Locality.name == str(location_data.locality_name)).first()
        country = db.query(Country).filter(Country.name == str(location_data.country_name)).first()

    @staticmethod
    def create_address(db: Session, address_data):
        """
        Create a new address in the database.
        """
        new_address = Address(**address_data.dict())
        db.add(new_address)
        db.commit()
        db.refresh(new_address)

        return new_address

    @staticmethod
    def create_street(db: Session, street_data):
        """
        Create a new street in the database.
        """
        new_street = Street(**street_data.dict())
        db.add(new_street)
        db.commit()
        db.refresh(new_street)

        return new_street

    @staticmethod
    def create_locality(db: Session, locality_data):
        """
        Create a new locality in the database.
        """
        new_locality = Locality(**locality_data.dict())
        db.add(new_locality)
        db.commit()
        db.refresh(new_locality)

        return new_locality

    @staticmethod
    def create_country(db: Session, country_data):
        """
        Create a new country in the database.
        """
        new_country = Country(**country_data.dict())
        db.add(new_country)
        db.commit()
        db.refresh(new_country)

        return new_country
