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

def race():
    print("BANG !!!!! \nAND THERE ARE OFF !!!!!")
    fast = 4
    hair = 5

    h = "H"
    t = "T"

    # if fast < hair:
    #     temp = h
    #     h = t
    #     t = temp

    pos1 = hair - fast
    sym = "-"
    num = 7 - hair
    # if fast > hair:
    #     pos2 = fast - hair
    #     sym = "-"
    #     num = 7 - fast
    #     print(f"{f"{h}":{sym}>{hair}}{f"{t}":{sym}>{pos2}}{"":{sym}>{num}}")
    # else:
    print(f"{f"{h}":{sym}>{fast}}{f"{t}":{sym}>{pos1}}{"":{sym}>{num}}")

    print(f"")




    # print("Diamond".repeat(10))
    tortoisePosition = 1
    harePosition = 1

    tortoiseMove = tortoise()
    hareMove = hare()

    # if



print(race())

# some_moves = ("Sleep", "Big Hop", "Small slip")
# for move in range(len(some_moves) ):
#     print("fish: ",some_moves[move], ": Stop")
#     print("index: ",move)
# print(some_moves[2])