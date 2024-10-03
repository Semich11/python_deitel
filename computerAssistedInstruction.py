from random import randrange


def randomNumberGenerator(digitLength):
    if digitLength == 1:
        stop = 10
    else: stop = 100
    firstNumber = randrange(1, stop)
    secondNumber = randrange(1, stop)
    return firstNumber, secondNumber

flag = True

correctComments = ["Very good", "Nice work", "Keep up the good work!"]
wrongComments = ["No. Please try again.", "Wrong. Try once more.", "No. Keep trying."]



difficulty = int(input("Choose a difficulty level (1 = easy, 2 = medium): "))
while difficulty != 1 and difficulty != 2:
    difficulty = int(input("Choose a difficulty level (1 = easy, 2 = medium): "))




while flag:
    firstNumber, secondNumber = randomNumberGenerator(difficulty)
    correctAnswer = firstNumber * secondNumber
    studentAnswer = int(input(f"How much is {firstNumber} times {secondNumber}? "))
    if studentAnswer == correctAnswer:
        correctComment = randrange(3)
        print(correctComments[correctComment])
        flag = False
    else:
        print("No. Please try again.")
        while studentAnswer != correctAnswer:
            studentAnswer = int(input(f"How much is {firstNumber} times {secondNumber}? "))
            if studentAnswer == correctAnswer:
                flag = False
                wrongComment = randrange(3)
                print(wrongComments[wrongComment])
                print("{0} {1} {0}".format("fab", "chris"))
