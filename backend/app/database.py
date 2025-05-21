from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

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

