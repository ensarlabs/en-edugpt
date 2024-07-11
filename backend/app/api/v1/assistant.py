from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ... import schemas
from ...services import crud
from ...api.deps import get_db

router = APIRouter()

@router.post("/assistants/", response_model=schemas.Assistant)
def create_assistant(assistant: schemas.AssistantCreate, db: Session = Depends(get_db)):
    return crud.create_assistant(db=db, assistant=assistant)

@router.get("/assistants/{assistant_id}", response_model=schemas.Assistant)
def read_assistant(assistant_id: str, db: Session = Depends(get_db)):
    db_assistant = crud.get_assistant(db, assistant_id=assistant_id)
    if db_assistant is None:
        raise HTTPException(status_code=404, detail="Assistant not found")
    return db_assistant
