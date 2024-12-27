from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.document_service import DocumentService
from app.database.connection import get_db
from app.schemas.document_schema import DocumentResponse, DocumentCreateRequest, DocumentTypeResponse, \
    DocumentTypeCreateRequest, DocumentTypeUpdateRequest

router = APIRouter()


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document_by_id(document_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a document by its ID.
    """
    doc = DocumentService.get_document_by_id(db, document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return doc


@router.post("/", response_model=DocumentResponse)
def create_document(document_data: DocumentCreateRequest, db: Session = Depends(get_db)):
    """
    Create a new document.
    Example:
    document_data = {
        "type_id": int,
        "number": str,
        "date": date
    }
    """
    return DocumentService.create_document(db, document_data)


@router.get("/types/", response_model=list[DocumentTypeResponse])
def get_document_types(db: Session = Depends(get_db)):
    """
    Retrieve all document types
    """
    return DocumentService.get_document_types(db)


@router.get("/types/{document_type_id}", response_model=DocumentTypeResponse)
def get_document_type_by_id(document_type_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a document type by its ID.
    """
    document_type = DocumentService.get_document_type_by_id(db, document_type_id)
    if not document_type:
        raise HTTPException(status_code=404, detail="Document type not found")

    return document_type


@router.post("/types/", response_model=DocumentTypeResponse)
def create_document_type(document_type_data: DocumentTypeCreateRequest, db: Session = Depends(get_db)):
    """
    Create a new document type.
    Example:
    document_type_data = {
        "name": str
    }
    """
    return DocumentService.create_document_type(db, document_type_data)


@router.patch("/types/{document_type_id}/", response_model=DocumentTypeUpdateRequest)
def update_document_type(document_type_id: int, document_type_update_data: DocumentTypeUpdateRequest,
                         db: Session = Depends(get_db)):
    """
    Partially update an document type by ID.
    """
    updated_document_type = DocumentService.update_document_type(db, document_type_id, document_type_update_data.
                                                                 dict(exclude_unset=True))
    if not updated_document_type:
        raise HTTPException(status_code=404, detail="Document type not found")
    return updated_document_type
