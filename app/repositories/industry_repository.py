from sqlalchemy.orm import Session

from app.models.models import Industry


class IndustryRepository:
    @staticmethod
    def get_industries(db: Session):
        """
        Retrieve all industries
        """
        query = db.query(Industry)

        return query.all()

    @staticmethod
    def get_industry_by_id(db: Session, industry_id: int):
        """
        Retrieve an industry by its ID.
        """
        return db.query(Industry).filter(Industry.id == industry_id).first()

    @staticmethod
    def create_industry(db: Session, industry_data):
        """
        Create a new industry in the database.
        """
        new_industry = Industry(**industry_data)
        db.add(new_industry)
        db.commit()
        db.refresh(new_industry)

        return new_industry

    @staticmethod
    def update_industry(db: Session, industry: Industry, industry_update_data) -> Industry:
        """
        Update an industry with the provided fields.
        """
        for key, value in industry_update_data.items():
            if value is not None:
                setattr(industry, key, value)

        db.add(industry)
        db.commit()
        db.refresh(industry)
        return industry
