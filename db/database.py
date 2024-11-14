from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError



DB_URL = 'postgresql://postgres:postgres@localhost:5432/messages_db'

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)






def test_connection():
    try:
        with session_maker() as session:
            session.execute(text('SELECT 1'))
            print('\n\n----------- Connection successful !')
    except SQLAlchemyError as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)