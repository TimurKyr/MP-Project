from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from ..repositories.object_repository import ObjectRepository
from ..repositories.owner_repository import OwnerRepository
from ..repositories.contract_repository import ContractRepository
from ..repositories.document_repository import DocumentRepository


class ObjectService:
    @staticmethod
    def get_objects(db: Session, filters: Optional[dict] = None):
        """
        Retrieve all objects from the database with optional filters.
        """
        return ObjectRepository.get_objects(db, filters)

    @staticmethod
    def get_object_by_id(db: Session, object_id: int):
        """
        Retrieve a specific object by its ID.
        """
        return ObjectRepository.get_object_by_id(db, object_id)

    @staticmethod
    def create_object(db: Session, object_data):
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
                "type_id": int,
                "number": int,
                "date": str,
            },
            "contract": {
                "object_cost_kzt": float,
                "object_cost_usd": float,
                "market_cost_kzt": float,
                "date": str
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
        create_user = object_data.create_user
        create_date = datetime.now().strftime('%Y-%m-%d')
        update_user = None
        update_date = None

        owner = OwnerRepository.get_owner_by_bin(db, object_data.owner.bin)
        if not owner:
            owner_create = object_data.owner.dict()
            owner_create["create_user"] = create_user
            owner_create["create_date"] = create_date
            owner_create["update_user"] = update_user
            owner_create["update_date"] = update_date
            owner = OwnerRepository.create_owner(db, owner_create)

        # create new document
        document = DocumentRepository.create_document(db, object_data.document.dict())
        document_id = document.id

        # create new contract
        contract = ContractRepository.create_contract(db, object_data.contract.dict())
        contract_id = contract.id

        create_data = {
            "name": object_data.name,
            "owner_id": owner.id,
            "industry_id": object_data.industry_id,
            "address_id": object_data.address_id,
            "year_construction": object_data.year_construction,
            "year_purchase": object_data.year_purchase,
            "document_id": document_id,
            "contract_id": contract_id,
            "class_name": object_data.class_name,
            "floors_below": object_data.floors_below,
            "floors_above": object_data.floors_above,
            "area_total": object_data.area_total,
            "area_rentable": object_data.area_rentable,
            "parking_closed": object_data.parking_closed,
            "parking_open": object_data.parking_open,
            "plot_owned": object_data.plot_owned,
            "plot_rent": object_data.plot_rent,
            "status_id": object_data.status_id,
            "create_user": create_user,
            "create_date": create_date,
            "update_user": update_user,
            "update_date": update_date
        }

        return ObjectRepository.create_object(db, create_data)

    @staticmethod
    def update_object(db: Session, object_id: int, object_update_data):
        """
        Update an existing object with provided fields.
        """
        object = ObjectRepository.get_object_by_id(db, object_id)
        if not object:
            return None

        object.update_date = datetime.now().strftime('%Y-%m-%d')

        if object_update_data["owner"]:
            changed_owner = OwnerRepository.get_owner_by_bin(db, object_update_data["owner"]["bin"])
            if not changed_owner:
                owner_create = object_update_data["owner"]
                owner_create["create_user"] = object_update_data.update_user
                owner_create["create_date"] = datetime.now().strftime('%Y-%m-%d')
                owner_create["update_user"] = None
                owner_create["update_date"] = None
                changed_owner = OwnerRepository.create_owner(db, owner_create)
            object_update_data["owner"] = changed_owner
            object_update_data["owner_id"] = changed_owner.id

        # create new document
        if object_update_data["document"]:
            changed_document = DocumentRepository.create_document(db, object_update_data["document"])
            object_update_data["document"] = changed_document
            object_update_data["document_id"] = changed_document.id

        # create new contract
        if object_update_data["contract"]:
            changed_contract = ContractRepository.create_contract(db, object_update_data["contract"])
            object_update_data["contract"] = changed_contract
            object_update_data["contract_id"] = changed_contract.id

        return ObjectRepository.update_object(db, object, object_update_data)
