from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status  # type: ignore
from sqlalchemy.orm import Session  # type: ignore
from ..database import get_db
from ..models.user import User
from ..services.security import hash_password, verify_password, create_access_token
from pydantic import BaseModel  # type: ignore
from ..services.security import get_current_user

auth_router = APIRouter()

# Schema for user input
class UserCreate(BaseModel):
    username: str
    password: str

# Schema for output
class UserOut(BaseModel):
    id: UUID
    username: str

    class Config:
        from_attributes = True

# Schema for login request
class LoginRequest(BaseModel):
    username: str
    password: str

# Schema for registration response (includes token)
class RegisterResponse(BaseModel):
    id: UUID
    username: str
    access_token: str

    class Config:
        from_attributes = True

@auth_router.get("/me")
def get_current_user_info(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username
    }

@auth_router.post("/register", response_model=RegisterResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
        identity_key="placeholder"  # TODO: Replace with real key from client
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token({"sub": new_user.username})

    return {
        "id": new_user.id,
        "username": new_user.username,
        "access_token": token
    }

@auth_router.post("/login")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token({"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}
