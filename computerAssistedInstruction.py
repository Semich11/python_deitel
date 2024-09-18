from random import randrange


def randomNumberGenerator():
    firstNumber = randrange(1,11)
    secondNumber = randrange(1,11)
    return firstNumber, secondNumber

flag = True

correctComments = ["Very good", "Nice work", "Keep up the good work!"]
wrongComments = ["No. Please try again.", "Wrong. Try once more.", "No. Keep trying."]

while flag:
    firstNumber, secondNumber = randomNumberGenerator()
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
