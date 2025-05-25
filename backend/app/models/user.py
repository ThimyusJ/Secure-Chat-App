from sqlalchemy import Column, String, DateTime # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from datetime import datetime
import uuid
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    identity_key = Column(String, nullable=False)  # Base64-encoded public key
    created_at = Column(DateTime, default=datetime.utcnow)
    hashed_password = Column(String, nullable=False)

