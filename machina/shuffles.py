import random 
from functools import reduce
from collections import deque


# deck = [
    # 'a', 
    # 'b', 
    # 'c', 
    # 'd', 
    # 'e', 
    # 'f', 
    # 'g', 
    # 'h', 
    # 'i', 
    # 'j', 
    # 'k',
    # 'l',
    # 'm',
    # 'n',
    # ]

deck = [
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
71, 72, 73, 74, 75, 76, 77
    ]


# riffles:

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


# cuts:

def strip_shuf():
    cut_point = random.randint(1, len(deck) - 1)
    a, b = deck[:cut_point], deck[cut_point:]
    return b + a

def half_cut(deck):
    mid = len(deck)//2+ random.randint(-2,2)
    a,b = deck[:mid], deck[mid:]
    return b, a

def cut_and_middle(deck):    
    mid = len(deck)//2 + random.randint(-1,1)
    a,b = deck[:mid], deck[mid:]
    a_mid = len(a)//2 + random.randint(-2,2)
    a1, a2 = a[:a_mid], a[a_mid:]    
    return a1 + b + a2


# 1000:

def thousand_cuts(deck):
    i=0
    shuf_deck = deck
    while i < 100:
        shuf_deck = cut_and_middle(deck)
        i+=1
        print(shuf_deck)
    return shuf_deck
    
    
def thou_cut_with_riffles(deck):
    i=0
    while i < 1000:
        shuf_deck = cut_and_middle(deck)
        shuf_deck = sloppy_riffle(shuf_deck)
        i+=1
        print(shuf_deck, '\n')
    return shuf_deck

def thou_strip(deck): 
    i=0
    shuf_deck = deck
    while i < 1000:
        shuf_deck = strip_shuf()
        i+=1
        print(shuf_deck)
    return shuf_deck
    
    
        
        
        

def lambda_shuffler(deck, n, shuffle):
    return reduce(lambda d, _: shuffle(d), range(n), deck)



def main():
    
    print('stripthou: ', thou_strip(deck))    
    
    # print('close: ', lambda_shuffler(deck, 9, close_riffle))
    # print('sloppy: ', lambda_shuffler(deck, 9, sloppy_riffle))
    # print('perf:', lambda_shuffler(deck, 9, perfect_riffle))

if __name__ == "__main__":
    main()