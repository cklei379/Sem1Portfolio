#Chloe 
#1/7/25
#Rock Paper Scissors

#Init
#Functions
import random
score1=0
score2=0
#Shows wins and losts between player and computer
def win():
    global score1
    global score2
    score1 = score1+1
    score2 = score2+0
    print("Player " +str(score1)+ ", Computer " + str(score2))
def lose():
    global score1
    global score2
    score1 = score1+0
    score2 = score2+1
    print("Player " +str(score1)+ ", Computer " + str(score2))
def tie():
    global score1
    global score2
    score1 = score1+0
    score2 = score2+0
    print("Player " +str(score1)+ ", Computer " + str(score2))

def rpsgame():
    while True:
        global win
        global lose
        global tie
        #Step 1: welcomes player into game and asks for their move
        print("Welcome to Rock Paper Scissors")
        move = input("Enter your move (rock, paper, scissors, or stop to stop playing!): ")
        move = move.lower()
        if move =="stop":
            break
        if move =="rock" or "paper" or "scissors":
            print("Plater: " +str(move))

        #Step 2: generates computer's move
        #this function generates random numbers
        x= random.randint(1,3)
        if x == 1:
            x = "rock"
        if x == 2:
            x = "paper"
        if x == 3:
            x = "scissors"
        print("Computer plays: " +str(x))

        #Step 3: outcome
        if move==x:
            print("It's a tie!")
            tie()
        if move=="rock" and x=="paper":
            print("You lost!")
            lose()
        if move=="paper" and x=="scissors":
            print("You lost!")
            lose()
        if move=="scissors" and x=="rock":
            print("You lost!")
            lose()
        if move=="rock" and x=="scissors":
            print("You won!")
            win()
        if move=="paper" and x=="rock":
            print("You won!")
            win()
        if move=="scissors" and x=="paper":
            print("You won!")
            win()
        if move=="stop":
            break
#Main
rpsgame()
