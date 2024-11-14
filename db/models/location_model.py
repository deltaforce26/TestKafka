from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from db.models import Base, MessageModel


class LocationModel(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    country = Column(String)

    message_id:  Mapped[int] = mapped_column(ForeignKey("messages.id"))
    message:  Mapped["MessageModel"] = relationship(back_populates="location_model")

