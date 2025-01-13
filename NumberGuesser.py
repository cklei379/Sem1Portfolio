#Chloe 
#11/8/24
#Number Guesser Game

#init
import random
numb = random.randint(1, 10)
numb = "4"
numbM = random.randint(1, 15)
numbM = "8"
numbH = random.randint(1, 25)
numbH = "21"


#Function
print("Number Guesser Game")
print("Guess the right number to win!")
mode = input("Please choose your difficulty level: easy, medium, hard")
#makes the range of numbers from 1-10
if mode == "easy":
    num = input("Please enter a number between 1-10")
    #tells if the number is too high or low
    if num > str(numb):
        print("Oops! your guess was too high! Please try again.")
    if num<str(numb):
        print("Oops! your guess was too low! Please try again.")
    if num == str(numb):
        print("Congratulations! You have won the game!")
#makes the range of numbers from 1-15
if mode == "medium":
    numM = input("Please enter a number between 1-15")
    #tells if the number is too high or low
    if numM > str(numbM):
        print("Oops! your guess was too high! Please try again.")
    if numM<str(numbM):
        print("Oops! your guess was too low! Please try again.")
    if numM == str(numbM):
        print("Congratulations! You have won the game!")
#makes the range of numbers from 1-25
if mode == "hard":
    numH = input("Please enter a number between 1-25")
    #tells if the number is too high or low
    if numH > str(numbH):
        print("Oops! your guess was too high! Please try again.")
    if numH<str(numbH):
        print("Oops! your guess was too low! Please try again.")
    if numH == str(numbH):
        print("Congratulations! You have won the game!")

