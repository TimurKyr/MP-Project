from datetime import datetime

from sqlalchemy.orm import Session
from app.repositories.status_repository import StatusRepository


class StatusService:
    @staticmethod
    def get_statuses(db: Session):
        """
        Retrieve all statuses
        """
        return StatusRepository.get_statuses(db)

    @staticmethod
    def get_status_by_id(db: Session, status_id: int):
        """
        Retrieve a specific status by its ID.
        """
        return StatusRepository.get_status_by_id(db, status_id)

    @staticmethod
    def create_status(db: Session, status_data):
        """
        Create a new status.
        Example:
        owner_data = {
            "create_user": str
            "name": str,
        }
        """
        create_data = {
            "name": status_data.name,
            "create_user": status_data.create_user,
            "create_date": datetime.now().strftime('%Y-%m-%d'),
            "update_user": None,
            "update_date": None
        }
        return StatusRepository.create_status(db, create_data)

    @staticmethod
    def update_status(db: Session, status_id: int, status_update_data):
        """
        Update an existing status with provided fields.
        """
        status = StatusRepository.get_status_by_id(db, status_id)
        if not status:
            return None

        status.update_date = datetime.now().strftime('%Y-%m-%d')

        return StatusRepository.update_status(db, status, status_update_data)
