from sqlalchemy import Column, Integer
from db.models import Base


class HostageTable(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(Integer)
