import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def draw_n(deck, n):
    hand = random.sample(deck, n)
    print(hand)
    
def draw_3(deck):
    spread =random.sample(deck,3)
    return spread
    
def draw_10(deck):
    spread =random.sample(deck,10)
    return spread
    
# def celtic_cross(deck):
#     drawn_cards = draw_10(deck)
#     rev = False
    
#     for card in drawn_cards:
#         spread = [
#             (x, y) 
#             for x, y 
#             in zip(drawn_cards[card], rev)
#             ]
        
        
def celtic_cross(deck):
    drawn_cards = draw_10(deck)
    spread = [(card, random.choice([False, True])) for card in drawn_cards]
    return spread




    
    

def main ():
    celtic_cross(deck)




if __name__ == "__main__":
    main()
    