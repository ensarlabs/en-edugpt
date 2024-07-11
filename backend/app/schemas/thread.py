from pydantic import BaseModel
from typing import Optional

class ThreadBase(BaseModel):
    name: str
    metadata: Optional[dict]

class ThreadCreate(ThreadBase):
    pass

class ThreadUpdate(ThreadBase):
    name: Optional[str] = None
    metadata: Optional[dict] = None

class Thread(ThreadBase):
    thread_id: str
    assistant_id: str
    user_id: str
    document_id: str
    updated_at: str

    class Config:
        orm_mode = True
