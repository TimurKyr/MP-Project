from sqlalchemy.orm import Session

from app.models.models import Contract


class ContractRepository:
    @staticmethod
    def get_contracts(db: Session):
        """
        Retrieve all get_contracts
        """
        query = db.query(Contract)

        return query.all()

    @staticmethod
    def get_contract_by_id(db: Session, contract_id: int):
        """
        Retrieve a contract by its ID.
        """
        return db.query(Contract).filter(Contract.id == contract_id).first()

    @staticmethod
    def create_contract(db: Session, contract_data):
        """
        Create a new document in the database.
        """
        new_contract = Contract(**contract_data)
        db.add(new_contract)
        db.commit()
        db.refresh(new_contract)

        return new_contract
