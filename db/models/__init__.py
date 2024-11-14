from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .sentence_model import SentenceModel
from .message_model import MessageModel
from .device_model import DeviceModel
from .location_model import LocationModel
from .hostage_table import HostageTable
from .explosive_table import ExplosiveTable