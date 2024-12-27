from sqlalchemy.orm import Session

from app.models.models import Owner


class OwnerRepository:
    @staticmethod
    def get_owners(db: Session):
        """
        Retrieve all owners
        """
        query = db.query(Owner)

        return query.all()

    @staticmethod
    def get_owner_by_id(db: Session, owner_id: int):
        """
        Retrieve an owner by its ID.
        """
        return db.query(Owner).filter(Owner.id == owner_id).first()

    @staticmethod
    def get_owner_by_bin(db: Session, owner_bin: int):
        """
        Retrieve an owner by its bin.
        """
        return db.query(Owner).filter(Owner.bin == owner_bin).first()

    @staticmethod
    def create_owner(db: Session, owner_data):
        """
        Create a new owner in the database.
        """
        new_owner = Owner(**owner_data)
        db.add(new_owner)
        db.commit()
        db.refresh(new_owner)

        return new_owner

    @staticmethod
    def update_owner(db: Session, owner: Owner, owner_update_data) -> Owner:
        """
        Update an owner with the provided fields.
        """
        for key, value in owner_update_data.items():
            if value is not None:
                setattr(owner, key, value)

        db.add(owner)
        db.commit()
        db.refresh(owner)
        return owner
