from app.database import Base, engine
from app.models.user import User
from app.models.signed_prekey import SignedPreKey
from app.models.one_time_prekey import OneTimePreKey

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
