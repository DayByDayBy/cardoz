from typing import Dict, List, Tuple, Optional, Any, TypedDict

class TarotCard(TypedDict):
    name: str
    nameShort: str
    suit: str
    value: str
    meaningUp: str
    meaningRev: str
    desc: str

from ..obj import tarot_deck