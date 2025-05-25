from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from app.database import get_db
from app.models.user import User
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageResponse
from app.dependencies import get_current_user

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/send", response_model=MessageResponse)
def send_message(request: MessageCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    receiver = db.query(User).filter(User.username == request.receiver_username).first()
    if not receiver:
        raise HTTPException(status_code=404, detail="Receiver not found")

    message = Message(
        sender_id=current_user.id,
        receiver_id=receiver.id,
        content=request.content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

@router.get("/conversations/{username}", response_model=list[MessageResponse])
def get_conversation(username: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    other_user = db.query(User).filter(User.username == username).first()
    if not other_user:
        raise HTTPException(status_code=404, detail="User not found")

    messages = db.query(Message).filter(
        ((Message.sender_id == current_user.id) & (Message.receiver_id == other_user.id)) |
        ((Message.sender_id == other_user.id) & (Message.receiver_id == current_user.id))
    ).order_by(Message.timestamp).all()

    return messages
