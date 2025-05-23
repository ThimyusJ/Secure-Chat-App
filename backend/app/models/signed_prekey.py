from sqlalchemy import Column, Integer, String, ForeignKey, DateTime # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from datetime import datetime
from app.database import Base

class SignedPreKey(Base):
    __tablename__ = "signed_prekeys"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    key = Column(String, nullable=False)
    signature = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
