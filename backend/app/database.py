from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker, Session # type: ignore

DATABASE_URL = DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/securechatdb"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ This is the function auth.py is trying to import
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

