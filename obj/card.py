class Card:
    def __init__(self, name, suit, rank, value, ordering):
        
        """ generic card object 
        
            name/suit/rank - full name of card, suit, rank-name (eg K)
            value - int, numeric value of card
            order_pos - position of card in 'properly' sorted deck, likely 0-len(deck)
            (possibly trying a mapped 0-10 range later, but probably not at first)
            
            a few methods that might be useful
        """
        
        self.name = name
        self.suit = suit
        self.rank = rank
        self.value = value
        self.order_pos = ordering
        pass
    
    
    # getters:
    
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def get_value(self):
        return self.value
    def get_ordering(self):
        return self.order_pos
    
    # object checks:
    
    def __repr__(self):
         return f'<card: {self.name}>'
     
    def __eq__(self, other):
        return (
            isinstance(other, Card) and 
            self.name == other.name and 
            self.suit and other.suit and 
            self.rank and other.rank
            )
    
    
    # card checks:
    
    def is_same_suit(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit
        return False
    
    def is_same_value(self, other):
        if isinstance(other, Card):
            return self.value == other.value
        return False
    
    def is_diff_both(self, other):
        return self.suit == other.suit and self.value == other.value
    
