from random import randrange


def guessTheNumberGameFunction():
    randomNumber = randrange(1, 1000)
    return randomNumber



def guessTheNumberGameDriver(playerInput):
    myNumber = guessTheNumberGameFunction()
    print("Here!!",myNumber)

    high = "Too high. Try Again"
    low = "Too low. Try Again"
    win = "Congratulations. You guessed my number!"
    game_result = ""
    flag = True
    while flag:

        #playerInput = int(input("Guess my number between 1 and 1000 with the fewest guess: "))

        game_result = f"{high if playerInput > myNumber else low if playerInput != myNumber else win} "
        if game_result == win:
            print(game_result)
            flag = False
        else: print(game_result)

    return game_result