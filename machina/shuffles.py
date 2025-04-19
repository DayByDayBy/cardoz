import random 
from functools import reduce
from collections import deque


deck = [1, 2, 3, 4, 5, 6, 7, 8]

def perfect_riffle(deck):
    mid = len(deck)//2
    a,b = deck[:mid], deck[mid:]
    riffled_deck = [card for pair in zip(a,b) for card in pair]
    return riffled_deck

def close_riffle(deck):
    mid = len(deck)//2+ random.randint(-3,3)
    a,b = deck[:mid], deck[mid:]
    close_rif = [ card for pair in zip(a, b) for card in pair] + a[len(b):]+b[len(a):]
    return close_rif

def sloppy_riffle(deck):
    mid = len(deck)//2
    a,b = deque(deck[:mid]), deque(deck[mid:])
    
    slop_deck = [
        (a if not b else b if not a else (a if random.random() < 0.5 else b)).popleft()
        for _ in range(len(deck))
        if a or b
        ]
    slop_deck += list(a) + list(b)
    return slop_deck


def cut(deck):
    mid = len(deck)//2+ random.randint(-5,5)
    a,b = deck[:mid], deck[mid:]
    return a, b

def cut_and_middle(deck):
    # get two rough halves, 
    # place second half in rough middle of first half
    # return new deck
    
    mid = len(deck)//2+ random.randint(-5,5)
    a,b = deck[:mid], deck[mid:]
    
    a_mid = len(deck)//2+ random.randint(-3,3)
    a1, a2 = a[:a_mid], a[a_mid:]
    
    return a1+b+a2




def lambda_shuffler(deck, n, shuffle):
    return reduce(lambda d, _: shuffle(d), range(n), deck)


def main():
    print('close: ', lambda_shuffler(deck, 9, close_riffle))
    print('sloppy: ', lambda_shuffler(deck, 9, sloppy_riffle))
    print('perf:', lambda_shuffler(deck, 9, perfect_riffle))
    

if __name__ == "__main__":
    main()