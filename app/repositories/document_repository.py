from sqlalchemy.orm import Session

from app.models.models import Document, DocumentType


class DocumentRepository:
    @staticmethod
    def get_document_by_id(db: Session, document_id: int):
        """
        Retrieve a document by its ID.
        """
        return db.query(Document).filter(Document.id == document_id).first()

    @staticmethod
    def create_document(db: Session, document_data):
        """
        Create a new document in the database.
        """
        new_document = Document(**document_data)
        db.add(new_document)
        db.commit()
        db.refresh(new_document)

        return new_document

    @staticmethod
    def get_document_types(db: Session):
        """
        Retrieve all document types
        """
        query = db.query(DocumentType)

        return query.all()

    @staticmethod
    def get_document_type_by_id(db: Session, document_type_id: int):
        """
        Retrieve a document type by its ID.
        """
        return db.query(DocumentType).filter(DocumentType.id == document_type_id).first()

    @staticmethod
    def create_document_type(db: Session, document_type_data):
        """
        Create a new document type in the database.
        """
        new_document_type = DocumentType(**document_type_data)
        db.add(new_document_type)
        db.commit()
        db.refresh(new_document_type)

        return new_document_type

    @staticmethod
    def update_document_type(db: Session, document_type: DocumentType, document_type_update_data) -> DocumentType:
        """
        Update a document type with the provided fields.
        """
        for key, value in document_type_update_data.items():
            if value is not None:
                setattr(document_type, key, value)

        db.add(document_type)
        db.commit()
        db.refresh(document_type)
        return document_type
