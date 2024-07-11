from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ... import schemas
from ...services import crud
from ...api.deps import get_db

router = APIRouter()

@router.post("/documents/", response_model=schemas.Document)
def create_document(document: schemas.DocumentCreate, db: Session = Depends(get_db)):
    return crud.create_document(db=db, document=document)

@router.get("/documents/{document_id}", response_model=schemas.Document)
def read_document(document_id: str, db: Session = Depends(get_db)):
    db_document = crud.get_document(db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

@router.put("/documents/{document_id}", response_model=schemas.Document)
def update_document(document_id: str, document: schemas.DocumentUpdate, db: Session = Depends(get_db)):
    db_document = crud.update_document(db, document_id=document_id, document_update=document)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

@router.delete("/documents/{document_id}", response_model=schemas.Document)
def delete_document(document_id: str, db: Session = Depends(get_db)):
    db_document = crud.delete_document(db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document
