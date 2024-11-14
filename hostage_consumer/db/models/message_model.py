from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from hostage_consumer.db.models import Base


class MessageModel(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    city = Column(String)
    country = Column(String)
    sentences = ''

    device = relationship('DeviceModel', back_populates='messages')
    device_id = Column(Integer, ForeignKey('devices.id'))


