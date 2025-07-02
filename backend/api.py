from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Any, Dict

from . import crud, models
from .database import engine, get_db
from .readers import create_celtic_cross_reading

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api/readings/celtic-cross")
def get_celtic_cross_reading(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Generate a new Celtic Cross reading"""
    try:
        reading = create_celtic_cross_reading(db)
        return reading
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating reading: {str(e)}")

@app.get("/api/cards/{short_name}")
def get_card_details(short_name: str, db: Session = Depends(get_db)) -> Any:
    """Get details for a specific card by short name"""
    db_card = crud.get_card_by_short_name(db, short_name=short_name)
    if db_card is None:
        raise HTTPException(status_code=404, detail=f"Card not found: {short_name}")
    return db_card