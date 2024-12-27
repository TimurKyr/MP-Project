from sqlalchemy.orm import Session

from app.repositories.contract_repository import ContractRepository


class ContractService:
    @staticmethod
    def get_contract_by_id(db: Session, contract_id: int):
        """
        Retrieve a specific contract by its ID.
        """
        return ContractRepository.get_contract_by_id(db, contract_id)

    @staticmethod
    def create_contract(db: Session, contract_data):
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
        create_data = {
            "object_cost_kzt": contract_data.object_cost_kzt,
            "object_cost_usd": contract_data.object_cost_usd,
            "market_cost_kzt": contract_data.market_cost_kzt,
            "date": contract_data.date
        }

        return ContractRepository.create_contract(db, create_data)
