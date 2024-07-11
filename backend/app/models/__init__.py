from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .user import User
from .assistant import Assistant
from .document import Document
from .thread import Thread
from .document_thread import DocumentThread

__all__ = [
    "User",
    "Assistant",
    "Document",
    "Thread",
    "DocumentThread",
    "Base",
]
