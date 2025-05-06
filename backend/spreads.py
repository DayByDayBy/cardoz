import random
from typing import List, Tuple, Dict, Any
from .models import TarotCard

class SpreadPosition:
    def __init__(self, name: str, description: str, pos: int,
                #  x_pos: int, 
                #  y_pos: int
                 ):
        self.name = name
        self.description = description
        self.pos = pos
        
        # visual positioning data? better here, or in the front?
        # self.x_pos = x_pos
        # self.y_pos = y_pos
        
        # if here, need to add the x and y values back in to the class below:

class CelticCrossSpread:
    def __init__(self):
        self.positions = [
            SpreadPosition("Present", "Represents the present situation", 0),
            SpreadPosition("Challenge", "Represents the immediate challenge", 1),  # Same position, displayed rotated
            SpreadPosition("Foundation", "The basis of the situation", 2),
            SpreadPosition("Recent Past", "What is passing away", 3),
            SpreadPosition("Possible Outcome", "The attitude or approach to take", 4),
            SpreadPosition("Immediate Future", "What is coming soon", 5),
            SpreadPosition("Self", "Your position or attitude", 6),
            SpreadPosition("External Influences", "Others' attitudes", 7),
            SpreadPosition("Hopes and Fears", "Your expectations", 8),
            SpreadPosition("Final Outcome", "The culmination of all influences", 9),
        ]
    
    def get_positions(self):
        return self.positions
