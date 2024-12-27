from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.status_service import StatusService
from app.database.connection import get_db
from app.schemas.status_schema import StatusResponse, StatusCreateRequest, StatusUpdateRequest

router = APIRouter()


@router.get("/", response_model=list[StatusResponse])
def get_statuses(db: Session = Depends(get_db)):
    """
    Retrieve all statuses
    """
    return StatusService.get_statuses(db)


@router.get("/{status_id}", response_model=StatusResponse)
def get_status_by_id(status_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a status by its ID.
    """
    stat = StatusService.get_status_by_id(db, status_id)
    if not stat:
        raise HTTPException(status_code=404, detail="Status not found")

    return stat


@router.post("/", response_model=StatusResponse)
def create_status(status_data: StatusCreateRequest, db: Session = Depends(get_db)):
    """
    Create a new status.
    Example:
    owner_data = {
        "create_user": str
        "name": str,
    }
    """
    return StatusService.create_status(db, status_data)


@router.patch("/{status_id}/", response_model=StatusResponse)
def update_status(status_id: int, status_update_data: StatusUpdateRequest, db: Session = Depends(get_db)):
    """
    Partially update a status by ID.
    """
    updated_status = StatusService.update_status(db, status_id, status_update_data.dict(exclude_unset=True))
    if not updated_status:
        raise HTTPException(status_code=404, detail="Status not found")
    return updated_status
