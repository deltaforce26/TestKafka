from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from db.models import Base
from db.models.location_model import LocationModel


class MessageModel(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(String)

    location: Mapped["LocationModel"] = relationship(back_populates="message_model")

    sentences = relationship('SentenceModel', back_populates='message')

    device = relationship('DeviceModel', back_populates='messages')
    device_id = Column(Integer, ForeignKey('devices.id'))


