import random

deck = [1, 2, 3, 4, 5, 6, 7, 8]

def draw_n(deck, n):
    hand = random.sample(deck, n)
    print(hand)
    
def draw_3_spread(deck):
    spread =random.sample(deck,3)
    print(spread)
    
def draw_cross(deck):
    spread =random.sample(deck,10)
    print(spread)

    
       
def main ():
    draw_n(deck, 3)
    draw_3_spread(deck)
    # draw_cross(deck)    ## won't run with small list test var
    
    
if __name__ == "__main__":
    main()
    