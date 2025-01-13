#Chloe 
#1/9/25
#Multiplication Quiz

#init
import random
score =0
import time
#Function
stime=time.time()
etime=time.time()
eltime=etime-stime
print("Welcome to the multiplication quiz. Test your mathematics knowledge!")
numb = input("Put the amount of questions you wish to take: ")
def correct():
    global score
    score = score+1
    print("Score " + str(score)+ " of "+ str(numb))
def incorrect():
    global score
    score = score+0
    print("Score " + str(score)+ " of "+ str(numb))
random.randint(0,10)
def multi(numb):
    for i in range(numb):
        x = random.randint(0,10)
        y= random.randint(0,10)
        print("Question 1: " + str(x) + "x" + str(y) + "=" )
        answ = input("Answer: ")
        m = x*y
        if  str(m) == str(answ):
            print("Correct.")
            correct()
        else:
            print("Wrong.")
            incorrect()
def ques():
    multi(5)
    print(f"Elasped time:{eltime} seconds")
#Main
ques()


