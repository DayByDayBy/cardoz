class Card:
    def __init__(self, name, suit, rank, value, ordering):
        
        """ generic card object 
        
            name/suit/rank - full name of card, suit, rank-name (eg K)
            value - int, numeric value of card
            ordering - position of card in 'properly' sorted deck, 0-len(deck)
            (possibly trying a mapped 0-10 range, but probably not at first)
            
            a few methods that might be useful
        """
        
        
        self.name = name
        self.suit = suit
        self.rank = rank
        self.value = value
        self.ordering = ordering
        
        pass
    
    def __repr__(self):
         return f'<card: {self.name}>'
     
    def __eq__(self, other):
        return (
            isinstance(other, Card) and 
            self.name == other.name and 
            self.suit and other.suit and 
            self.rank and other.rank
            )
    
    
    
    def is_same_suit(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit
        return False
    
