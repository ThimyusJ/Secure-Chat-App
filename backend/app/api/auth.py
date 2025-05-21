from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..services.security import hash_password
from pydantic import BaseModel

auth_router = APIRouter()

# Pydantic schema for user input
class UserCreate(BaseModel):
    username: str
    password: str

# Schema for output
class UserOut(BaseModel):
    id: UUID
    username: str

    class Config:
        from_attributes = True  # Use this instead of orm_mode for Pydantic v2

@auth_router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
        identity_key="placeholder"  # Replace with real key exchange logic later
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

