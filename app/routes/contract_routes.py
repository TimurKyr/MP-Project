from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.contract_service import ContractService
from app.database.connection import get_db
from app.schemas.contract_schema import ContractResponse, ContractCreateRequest

router = APIRouter()


@router.get("/{contract_id}", response_model=ContractResponse)
def get_contract_by_id(contract_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a contract by its ID.
    """
    con = ContractService.get_contract_by_id(db, contract_id)
    if not con:
        raise HTTPException(status_code=404, detail="Contract not found")

    return con


@router.post("/", response_model=ContractResponse)
def create_contract(contract_data: ContractCreateRequest, db: Session = Depends(get_db)):
    """
    Create a new contract.
    Example:
    contract_data = {
        "object_cost_kzt": float
        "object_cost_usd": float
        "market_cost_kzt": float
        "date": date
    }
    """
    return ContractService.create_contract(db, contract_data)
