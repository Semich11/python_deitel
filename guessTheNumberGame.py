from random import randrange


def guessTheNumberGameFunction():
    randomNumber = randrange(1, 1000)
    return randomNumber



def guessTheNumberGameDriver():
    myNumber = guessTheNumberGameFunction()
    print("Here!!",myNumber)

    high = "Too high. Try Again"
    low = "Too low. Try Again"
    win = "Congratulations. You guessed my number!"
    game_result = ""
    flag = True
    counter = 0
    while flag:
        if counter > 10:
            print("You should be able to do better!")
            break

        playerInput = int(input("Guess my number between 1 and 1000 with the fewest guess: "))

        game_result = f"{high if playerInput > myNumber else low if playerInput != myNumber else win} "
        if myNumber == playerInput:
            print(game_result)
            flag = False
        else: print(game_result)
        counter += 1


    return game_result

guessTheNumberGameDriver()