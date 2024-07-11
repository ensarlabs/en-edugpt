from sqlalchemy import Column, String, Boolean, ForeignKey, JSON, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from . import Base

class Assistant(Base):
    __tablename__ = "assistants"
    assistant_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    name = Column(String)
    config = Column(JSON)
    updated_at = Column(TIMESTAMP)
    public = Column(Boolean)
    user = relationship("User")
