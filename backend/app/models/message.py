from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from uuid import uuid4
from datetime import datetime
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID # type: ignore

class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    sender_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    receiver_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    read = Column(Boolean, default=False)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
