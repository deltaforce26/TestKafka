from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.models import Base




class DeviceModel(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)

    messages = relationship('MessageModel', back_populates='device')

