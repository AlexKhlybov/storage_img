from .base import engine, metadata
from .inbox import inbox
from .users import users

metadata.create_all(bind=engine)
