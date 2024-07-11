from pydantic import BaseModel
from typing import Optional

class DocumentBase(BaseModel):
    name: str
    s3_url: str

class DocumentCreate(DocumentBase):
    pass

class DocumentUpdate(DocumentBase):
    name: Optional[str] = None
    s3_url: Optional[str] = None

class Document(DocumentBase):
    document_id: str
    user_id: str
    uploaded_at: str

    class Config:
        orm_mode = True
