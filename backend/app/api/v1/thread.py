from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ... import schemas
from ...services import crud
from ...api.deps import get_db

router = APIRouter()

@router.post("/threads/", response_model=schemas.Thread)
def create_thread(thread: schemas.ThreadCreate, db: Session = Depends(get_db)):
    return crud.create_thread(db=db, thread=thread)

@router.get("/threads/{thread_id}", response_model=schemas.Thread)
def read_thread(thread_id: str, db: Session = Depends(get_db)):
    db_thread = crud.get_thread(db, thread_id=thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return db_thread

@router.get("/threads/", response_model=List[schemas.Thread])
def read_threads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    threads = crud.get_threads(db, skip=skip, limit=limit)
    return threads

@router.put("/threads/{thread_id}", response_model=schemas.Thread)
def update_thread(thread_id: str, thread: schemas.ThreadUpdate, db: Session = Depends(get_db)):
    db_thread = crud.get_thread(db, thread_id=thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return crud.update_thread(db=db, thread_id=thread_id, thread=thread)

@router.delete("/threads/{thread_id}", response_model=schemas.Thread)
def delete_thread(thread_id: str, db: Session = Depends(get_db)):
    db_thread = crud.get_thread(db, thread_id=thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return crud.delete_thread(db=db, thread_id=thread_id)
