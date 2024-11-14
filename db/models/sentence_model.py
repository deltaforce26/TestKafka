from sqlalchemy import Column, Integer, ARRAY, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models import Base



class SentenceModel(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentences = Column(ARRAY(String))

    message = relationship('MessageModel', back_populates='sentences')
    message_id = Column(Integer, ForeignKey('messages.id'))