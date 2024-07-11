from sqlalchemy.orm import Session
from ..models import user, assistant, document, thread, document_thread
from ..schemas import UserCreate, UserUpdate, AssistantCreate, DocumentCreate, DocumentUpdate, ThreadCreate, ThreadUpdate, DocumentThreadCreate

# User CRUD
def get_user(db: Session, user_id: str):
    return db.query(user.User).filter(user.User.user_id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = user.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: str, user_update: UserUpdate):
    db_user = get_user(db, user_id)
    if db_user:
        for key, value in user_update.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: str):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Assistant CRUD
def get_assistant(db: Session, assistant_id: str):
    return db.query(assistant.Assistant).filter(assistant.Assistant.assistant_id == assistant_id).first()

def create_assistant(db: Session, assistant: AssistantCreate):
    db_assistant = assistant.Assistant(**assistant.dict())
    db.add(db_assistant)
    db.commit()
    db.refresh(db_assistant)
    return db_assistant

# Document CRUD
def get_document(db: Session, document_id: str):
    return db.query(document.Document).filter(document.Document.document_id == document_id).first()

def create_document(db: Session, document: DocumentCreate):
    db_document = document.Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def update_document(db: Session, document_id: str, document_update: DocumentUpdate):
    db_document = get_document(db, document_id)
    if db_document:
        for key, value in document_update.dict().items():
            setattr(db_document, key, value)
        db.commit()
        db.refresh(db_document)
    return db_document

def delete_document(db: Session, document_id: str):
    db_document = get_document(db, document_id)
    if db_document:
        db.delete(db_document)
        db.commit()
    return db_document

# Thread CRUD
def get_thread(db: Session, thread_id: str):
    return db.query(thread.Thread).filter(thread.Thread.thread_id == thread_id).first()

def create_thread(db: Session, thread: ThreadCreate):
    db_thread = thread.Thread(**thread.dict())
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)
    return db_thread

def update_thread(db: Session, thread_id: str, thread_update: ThreadUpdate):
    db_thread = get_thread(db, thread_id)
    if db_thread:
        for key, value in thread_update.dict().items():
            setattr(db_thread, key, value)
        db.commit()
        db.refresh(db_thread)
    return db_thread

def delete_thread(db: Session, thread_id: str):
    db_thread = get_thread(db, thread_id)
    if db_thread:
        db.delete(db_thread)
        db.commit()
    return db_thread

# DocumentThread CRUD
def get_document_thread(db: Session, document_thread_id: str):
    return db.query(document_thread.DocumentThread).filter(document_thread.DocumentThread.document_thread_id == document_thread_id).first()

def create_document_thread(db: Session, document_thread: DocumentThreadCreate):
    db_document_thread = document_thread.DocumentThread(**document_thread.dict())
    db.add(db_document_thread)
    db.commit()
    db.refresh(db_document_thread)
    return db_document_thread
