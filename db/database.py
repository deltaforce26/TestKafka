from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

DB_URL = 'postgresql://admin:1234@localhost:5432/messages_db'

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
