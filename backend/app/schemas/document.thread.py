from pydantic import BaseModel, UUID4

class DocumentThreadBase(BaseModel):
    document_id: UUID4
    thread_id: UUID4

class DocumentThreadCreate(DocumentThreadBase):
    pass

class DocumentThread(DocumentThreadBase):
    document_thread_id: UUID4

    class Config:
        orm_mode = True
