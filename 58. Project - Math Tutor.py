# import modules
from random import randrange as r
import time

# ask how many questions user wants
numQuestions = int(input("How many questions do you want?: "))
# bonus #2: allow the user to specify how high the numbers used should be
lowerRange = int(input("What should the lower range of numbers be?: "))
upperRange = int(input("What should the upper range of numbers be?: "))
# set score start at zero
playerScore = 0
totalTime = 0.0

answerList = []

# loop through number of questions
for question in range(numQuestions):
    # create two random numbers and calc answer
    numA = r(lowerRange, upperRange)
    numB = r(lowerRange, upperRange)
    correctAnswer = numA * numB
    # show user the question
    # bonus #1: capture time between user inputs
    startTime = time.perf_counter()
    userAnswer = int(input(f"What is {numA} * {numB} = "))
    answerList.append(
        f"{numA} * {numB} = {correctAnswer} --> You guessed: {userAnswer}"
    )
    endTime = time.perf_counter()
    timeTaken = round((endTime - startTime), 2)
    totalTime = round((totalTime + timeTaken), 2)
    # capture answer and modify user score
    if userAnswer == correctAnswer:
        playerScore = playerScore + 1
        print(f"You are correct! You took {timeTaken} seconds to answer.\n")
    else:
        print(
            f"Sorry, that answer is incorrect. The correct answer was {correctAnswer}. Better luck next time!\n"
        )
# output final score
print(
    f"Your final score is: {playerScore} out of {numQuestions} correct!\nYou took {totalTime} seconds to answer all {numQuestions} questions, which is {totalTime/numQuestions} seconds per question!"
)

# bonus #3: print all of the questions and answers
for answer in answerList:
    print(answer)
