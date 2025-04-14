class Card:
    def __init__(self, name, suit, rank, value, ordering):
        
        """ generic card object 
        
            name/suit/rank - full name of card, suit, rank-name (eg K)
            value - int, numeric value of card
            ordering - position of card in 'properly' sorted deck, 0-len(deck)
            (possibly trying a mapped 0-10 range, but probably not at first)
        
        """
        self.name = name
        self.suit = suit
        self.rank = rank
        self.value = value
        self.ordering = ordering
        pass
