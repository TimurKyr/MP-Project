from typing import Optional

from sqlalchemy.orm import Session

from app.models.models import Object


class ObjectRepository:
    @staticmethod
    def get_objects(db: Session, filters: Optional[dict] = None):
        """
        Retrieve all objects with optional filtering.
        Filters are applied dynamically based on the keys in the filters dictionary.
        """
        query = db.query(Object)
        for key, value in filters.items():
            if hasattr(Object, key):
                query = query.filter(getattr(Object, key) == value)

        return query.all()

    @staticmethod
    def get_object_by_id(db: Session, object_id: int):
        """
        Retrieve an object by its ID.
        """
        return db.query(Object).filter(Object.id == object_id).first()

    @staticmethod
    def create_object(db: Session, object_data):
        """
        Create a new object in the database.
        """
        new_object = Object(**object_data)
        db.add(new_object)
        db.commit()
        db.refresh(new_object)

        return new_object

    @staticmethod
    def update_object(db: Session, object: Object, object_update_data) -> Object:
        """
        Update an object with the provided fields.
        """
        for key, value in object_update_data.items():
            if value is not None:
                setattr(object, key, value)

        db.add(object)
        db.commit()
        db.refresh(object)
        return object
