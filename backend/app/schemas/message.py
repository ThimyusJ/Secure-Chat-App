from pydantic import BaseModel # type: ignore
from datetime import datetime
from uuid import UUID

class MessageCreate(BaseModel):
    receiver_username: str
    content: str

from uuid import UUID

class MessageResponse(BaseModel):
    id: UUID
    sender_id: UUID
    receiver_id: UUID
    content: str
    timestamp: datetime
    read: bool  # ✅ Boolean

    class Config:
        from_attributes = True  # Pydantic v2 compatible

