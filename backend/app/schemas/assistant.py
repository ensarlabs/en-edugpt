from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class AssistantBase(BaseModel):
    user_id: UUID4
    name: str
    config: dict
    public: bool

class AssistantCreate(AssistantBase):
    pass

class Assistant(AssistantBase):
    assistant_id: UUID4
    updated_at: datetime

    class Config:
        orm_mode = True
