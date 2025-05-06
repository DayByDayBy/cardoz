
from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from .models import TarotCard
from .readers import create_celtic_cross_reading
from ..obj import tarot_deck

deck = tarot_deck

app = FastAPI()

@app.get("/api/readings/celtic-cross")
def get_celtic_cross_reading() -> Dict[str, Any]:
    """Generate a new Celtic Cross reading"""
    try:
        reading = create_celtic_cross_reading(deck)
        return reading
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating reading: {str(e)}")

@app.get("/api/cards/{short_name}")
def get_card_details(short_name: str) -> Dict[str, Any]:
    """Get details for a specific card by short name"""
    for card in deck:
        if card["nameShort"] == short_name:
            return card
    raise HTTPException(status_code=404, detail=f"Card not found: {short_name}")

