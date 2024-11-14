from sqlalchemy import Column, Integer
from db.models import Base


class ExplosiveTable(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(Integer)