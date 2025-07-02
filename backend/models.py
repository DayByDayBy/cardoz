from sqlalchemy import Column, Integer, String, Text
from .database import Base

class TarotCard(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    name_short = Column(String, unique=True, index=True)
    suit = Column(String)
    value = Column(String)
    meaning_up = Column(Text)
    meaning_rev = Column(Text)
    desc = Column(Text)
