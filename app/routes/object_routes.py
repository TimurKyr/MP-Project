from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.object_service import ObjectService
from app.database.connection import get_db
from app.schemas.object_schema import ObjectGetAllRequest, ObjectResponse, ObjectCreateRequest, ObjectUpdateRequest

router = APIRouter()


@router.get("/", response_model=list[ObjectResponse])
def get_objects(
    filters: ObjectGetAllRequest = Depends(),
    db: Session = Depends(get_db),
):
    """
    Retrieve all objects with optional filtering.
    Filters are passed as query parameters.
    """
    # Remove any None values
    filters = {key: value for key, value in filters.dict().items() if value is not None}

    return ObjectService.get_objects(db, filters)


@router.get("/{object_id}", response_model=ObjectResponse)
def get_object_by_id(object_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an object by its ID.
    """
    obj = ObjectService.get_object_by_id(db, object_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Object not found")

    return obj


@router.post("/", response_model=ObjectResponse)
def create_object(object_data: ObjectCreateRequest, db: Session = Depends(get_db)):
    """
    Create a new object in the database.
    Example:
    object_data = {
        "create_user": str,
        "owner": {
            "bin": int,
            "name": str,
            "abbreviation": str,
            "mp_share": Optional[int],
        },
        "industry_id": str,
        "address_id": int,
        "year_construction": Optional[int],
        "year_purchase": Optional[int],
        "document": {
            "type_name": str,
            "number": int,
            "date": str,
        },
        "contract": {
            "object_cost_kzt": float,
            "object_cost_usd": float,
            "market_cost_kzt": float,
            "date": str,
        },
        "class_name": str,
        "floors_below": int,
        "floors_above": int,
        "area_total": float,
        "area_rentable": float,
        "parking_closed": int,
        "parking_open": int,
        "plot_owned": float,
        "plot_rent": float,
        "status_id": int,
    }
    """
    return ObjectService.create_object(db, object_data)


@router.patch("/{object_id}/", response_model=ObjectResponse)
def update_object(object_id: int, object_update_data: ObjectUpdateRequest, db: Session = Depends(get_db)):
    """
    Partially update an object by ID.
    """
    updated_object = ObjectService.update_object(db, object_id, object_update_data.dict(exclude_unset=True))
    if not updated_object:
        raise HTTPException(status_code=404, detail="Object not found")
    return updated_object
