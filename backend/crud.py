from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from . import models

def get_card_by_short_name(db: Session, short_name: str):
    return db.query(models.TarotCard).filter(models.TarotCard.name_short == short_name).first()

def get_random_cards(db: Session, count: int):
    return db.query(models.TarotCard).order_by(func.random()).limit(count).all()
