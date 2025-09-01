# import modules
from random import randrange as r

# ask how many questions user wants
numQuestions = int(input("How many questions do you want?"))
# set score start at zero
playerScore = 0
# loop through number of questions
for question in range(numQuestions):
    # create two random numbers and calc answer
    numA = r(1, 10)
    numB = r(1, 10)
    correctAnswer = numA * numB
    # show user the question
    userAnswer = int(input(f"What is {numA} * {numB} = "))
    # capture answer and modify user score
    if userAnswer == correctAnswer:
        playerScore = playerScore + 1
        print("You are correct! Time for your next question...\n")
    else:
        print("Sorry, that answer is incorrect. Better luck next time!\n")
# output final score
print(f"Your final score is: {playerScore} out of {numQuestions} correct!")
