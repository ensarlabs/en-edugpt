from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    sub: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    sub: Optional[str] = None

class User(UserBase):
    user_id: str
    created_at: str

    class Config:
        orm_mode = True
