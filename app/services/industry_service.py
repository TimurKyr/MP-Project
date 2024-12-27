from datetime import datetime

from sqlalchemy.orm import Session

from app.repositories.industry_repository import IndustryRepository


class IndustryService:
    @staticmethod
    def get_industries(db: Session):
        """
        Retrieve all industries
        """
        return IndustryRepository.get_industries(db)

    @staticmethod
    def get_industry_by_id(db: Session, industry_id: int):
        """
        Retrieve a specific industry by its ID.
        """
        return IndustryRepository.get_industry_by_id(db, industry_id)

    @staticmethod
    def create_industry(db: Session, industry_data):
        """
        Create a new industry.
        Example:
        industry_data = {
            "create_user": str,
            "name": str
        }
        """
        create_data = {
            "name": industry_data.name,
            "create_user": industry_data.create_user,
            "create_date": datetime.now().strftime('%Y-%m-%d'),
            "update_user": None,
            "update_date": None
        }
        return IndustryRepository.create_industry(db, create_data)

    @staticmethod
    def update_industry(db: Session, industry_id: int, industry_update_data):
        """
        Update an existing industry with provided fields.
        """
        industry = IndustryRepository.get_industry_by_id(db, industry_id)
        if not industry:
            return None

        industry.update_date = datetime.now().strftime('%Y-%m-%d')

        return IndustryRepository.update_industry(db, industry, industry_update_data)
