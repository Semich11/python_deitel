from random import randrange


def randomNumberGenerator():
    firstNumber = randrange(1,11)
    secondNumber = randrange(1,11)
    return firstNumber, secondNumber


# firstNumber, secondNumber = randomNumberGenerator()
#
# correctAnswer = firstNumber * secondNumber
# print(correctAnswer)
#
# studentAnswer = int(input(f"How much is {firstNumber} times {secondNumber}? "))
# print(studentAnswer)
#
# if studentAnswer == correctAnswer:
#     print("Very good!")

flag = True

while flag:
    firstNumber, secondNumber = randomNumberGenerator()
    correctAnswer = firstNumber * secondNumber
    studentAnswer = int(input(f"How much is {firstNumber} times {secondNumber}? "))
    if studentAnswer == correctAnswer:
        print("Very good!")
        flag = False
    else:
        print("No. Please try again.")
        while studentAnswer != correctAnswer:
            studentAnswer = int(input(f"How much is {firstNumber} times {secondNumber}? "))
            if studentAnswer == correctAnswer:
                print("Very good!")
                flag = False
