from sqlalchemy import Column, String, JSON, TIMESTAMP, ForeignKey, BYTEA
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from . import Base

class Thread(Base):
    __tablename__ = "threads"
    thread_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    assistant_id = Column(UUID(as_uuid=True), ForeignKey("assistants.assistant_id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    name = Column(String)
    updated_at = Column(TIMESTAMP)
    metadata = Column(JSON)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.document_id"))
    checkpoint = Column(BYTEA)
    document = relationship("Document")
    assistant = relationship("Assistant")
    user = relationship("User")
