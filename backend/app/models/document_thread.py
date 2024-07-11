from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from . import Base

class DocumentThread(Base):
    __tablename__ = "document_threads"
    document_thread_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.document_id"))
    thread_id = Column(UUID(as_uuid=True), ForeignKey("threads.thread_id"))
    document = relationship("Document")
    thread = relationship("Thread")
