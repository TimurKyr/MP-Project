from sqlalchemy.orm import Session
from app.models.models import Status


class StatusRepository:
    @staticmethod
    def get_statuses(db: Session):
        """
        Retrieve all statuses
        """
        query = db.query(Status)

        return query.all()

    @staticmethod
    def get_status_by_id(db: Session, status_id: int):
        """
        Retrieve a status by its ID.
        """
        return db.query(Status).filter(Status.id == status_id).first()

    @staticmethod
    def create_status(db: Session, status_data):
        """
        Create a new owner in the database.
        """
        new_status = Status(**status_data)
        db.add(new_status)
        db.commit()
        db.refresh(new_status)

        return new_status

    @staticmethod
    def update_status(db: Session, status: Status, status_update_data) -> Status:
        """
        Update a status with the provided fields.
        """
        for key, value in status_update_data.items():
            if value is not None:
                setattr(status, key, value)

        db.add(status)
        db.commit()
        db.refresh(status)
        return status
