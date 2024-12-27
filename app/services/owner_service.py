from datetime import datetime

from sqlalchemy.orm import Session
from app.repositories.owner_repository import OwnerRepository


class OwnerService:
    @staticmethod
    def get_owners(db: Session):
        """
        Retrieve all owners
        """
        return OwnerRepository.get_owners(db)

    @staticmethod
    def get_owner_by_id(db: Session, owner_id: int):
        """
        Retrieve a specific owner by its ID.
        """
        return OwnerRepository.get_owner_by_id(db, owner_id)

    @staticmethod
    def create_owner(db: Session, owner_data):
        """
        Create a new owner.
        Example:
        owner_data = {
            "create_user": str
            "bin": int,
            "name": str,
            "abbreviation": str
            "mp_share": int
        }
        """
        create_data = {
            "bin": owner_data.bin,
            "name": owner_data.name,
            "abbreviation": owner_data.abbreviation,
            "mp_share": owner_data.mp_share,
            "create_user": owner_data.create_user,
            "create_date": datetime.now().strftime('%Y-%m-%d'),
            "update_user": None,
            "update_date": None
        }
        return OwnerRepository.create_owner(db, create_data)

    @staticmethod
    def update_owner(db: Session, owner_id: int, owner_update_data):
        """
        Update an existing owner with provided fields.
        """
        owner = OwnerRepository.get_owner_by_id(db, owner_id)
        if not owner:
            return None

        owner.update_date = datetime.now().strftime('%Y-%m-%d')

        return OwnerRepository.update_owner(db, owner, owner_update_data)
