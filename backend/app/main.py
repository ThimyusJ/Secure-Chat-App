from fastapi import FastAPI # type: ignore
from app.api.auth import auth_router
from app.api import message


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(message.router)

