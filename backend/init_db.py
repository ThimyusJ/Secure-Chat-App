from app.database import engine
from app.database import Base
from app.models.user import User
from app.models.message import Message

def init():
    print("Creating tables...")

    # Optional: drop and recreate specific tables during development
    # ⚠️ Only do this for tables you're actively modifying!
    Message.__table__.drop(engine, checkfirst=True)

    # Create all tables that don't exist
    Base.metadata.create_all(bind=engine)

    print("Done.")

if __name__ == "__main__":
    init()
