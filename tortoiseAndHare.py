from itertools import repeat
from random import randrange, randint


def tortoise():
    i = randrange(1, 11)
    if 1 >= i <= 5:
        return "fast plod"
    elif 6 >= i <= 7:
        return "slip"
    else:return  "slow plod"


def hare():
    some_moves = ("Sleep", "Big Hop", "Small slip")
    move = randrange(len(some_moves))
    some_move = some_moves[move]
    print("inner_move: ",move)
    print(some_moves[move])
    i = randrange(1, 11)
    print(i)
    if 1 <= i <= 2:
        return  some_move
    elif 5 == i:
        return "Big slip"
    elif 8 <= i <= 10:
        return  "slow plod"

