from fastapi import FastAPI # type: ignore
from app.api.auth import auth_router


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])

