from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository


class DocumentService:
    @staticmethod
    def get_document_by_id(db: Session, document_id: int):
        """
        Retrieve a specific document by its ID.
        """
        return DocumentRepository.get_document_by_id(db, document_id)

    @staticmethod
    def create_document(db: Session, document_data):
        """
        Create a new document.
        Example:
        document_data = {
            "type_id": int,
            "number": str,
            "date": date
        }
        """
        create_data = {
            "type_id": document_data.type_id,
            "number": document_data.number,
            "date": document_data.date
        }
        return DocumentRepository.create_document(db, create_data)

    @staticmethod
    def get_document_types(db: Session):
        """
        Retrieve all document types
        """
        return DocumentRepository.get_document_types(db)

    @staticmethod
    def get_document_type_by_id(db: Session, document_type_id: int):
        """
        Retrieve a specific document type by its ID.
        """
        return DocumentRepository.get_document_type_by_id(db, document_type_id)

    @staticmethod
    def create_document_type(db: Session, document_type_data):
        """
        Create a new document type.
        Example:
        document_type_data = {
            "name": str
        }
        """
        create_data = {
            "name": document_type_data.name
        }
        return DocumentRepository.create_document_type(db, create_data)

    @staticmethod
    def update_document_type(db: Session, document_type_id: int, document_type_update_data):
        """
        Update an existing document type with provided fields.
        """
        document_type = DocumentRepository.get_document_type_by_id(db, document_type_id)
        if not document_type:
            return None

        return DocumentRepository.update_document_type(db, document_type, document_type_update_data)
