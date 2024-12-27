from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.owner_service import OwnerService
from app.database.connection import get_db
from app.schemas.owner_schema import OwnerResponse, OwnerCreateRequest, OwnerUpdateRequest

router = APIRouter()


@router.get("/", response_model=list[OwnerResponse])
def get_owners(db: Session = Depends(get_db)):
    """
    Retrieve all owners
    """
    return OwnerService.get_owners(db)


@router.get("/{owner_id}", response_model=OwnerResponse)
def get_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an owner by its ID.
    """
    own = OwnerService.get_owner_by_id(db, owner_id)
    if not own:
        raise HTTPException(status_code=404, detail="Owner not found")

    return own


@router.post("/", response_model=OwnerResponse)
def create_owner(owner_data: OwnerCreateRequest, db: Session = Depends(get_db)):
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
    return OwnerService.create_owner(db, owner_data)


@router.patch("/{owner_id}/", response_model=OwnerResponse)
def update_owner(owner_id: int, owner_update_data: OwnerUpdateRequest, db: Session = Depends(get_db)):
    """
    Partially update an owner by ID.
    """
    updated_owner = OwnerService.update_owner(db, owner_id, owner_update_data.dict(exclude_unset=True))
    if not updated_owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return updated_owner
