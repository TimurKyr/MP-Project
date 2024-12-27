from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.industry_service import IndustryService
from app.database.connection import get_db
from app.schemas.industry_schema import IndustryResponse, IndustryCreateRequest, IndustryUpdateRequest

router = APIRouter()


@router.get("/", response_model=list[IndustryResponse])
def get_industries(db: Session = Depends(get_db)):
    """
    Retrieve all industries
    """
    return IndustryService.get_industries(db)


@router.get("/{industry_id}", response_model=IndustryResponse)
def get_industry_by_id(industry_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an industry by its ID.
    """
    ind = IndustryService.get_industry_by_id(db, industry_id)
    if not ind:
        raise HTTPException(status_code=404, detail="Industry not found")

    return ind


@router.post("/", response_model=IndustryResponse)
def create_industry(industry_data: IndustryCreateRequest, db: Session = Depends(get_db)):
    """
    Create a new industry.
    Example:
    industry_data = {
        "create_user": str,
        "name": str
    }
    """
    return IndustryService.create_industry(db, industry_data)


@router.patch("/{industry_id}/", response_model=IndustryResponse)
def update_industry(industry_id: int, industry_update_data: IndustryUpdateRequest, db: Session = Depends(get_db)):
    """
    Partially update an industry by ID.
    """
    updated_industry = IndustryService.update_industry(db, industry_id, industry_update_data.dict(exclude_unset=True))
    if not updated_industry:
        raise HTTPException(status_code=404, detail="Industry not found")
    return updated_industry
