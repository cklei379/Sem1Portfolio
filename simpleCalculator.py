#Simple Calculator
#Chloe 

#Init
#Function
#adds two numbers together and prints the results
def add(num1,num2):
    sum = num1 + num2
    print(sum)
#subtracts two numbers together and prints the results
def subtract(numb1,numb2):
    diff = numb1-numb2
    print(diff)
#multiplies two numbers together and prints the results
def multiply(x1,x2):
    answ = x1*x2
    print(answ)
#divides two numbers together and prints the results
def divide(y1,y2):
    quotient = y1/y2
    print(quotient)

def calc():
    print("Welcome to simple calculator")
    while True:
        print("Please select an operation: ")
        print("""1: Add
2: Subtract
3: Multiply
4: Divide
5: Quit""")
        operation = input("(1-5) Option: ")
        if operation == "1":
            int1= int(input("Enter the first number"))
            int2= int(input("Ender the second number"))
            add(int1,int2)
        if operation =="2":
            var1 = int(input("enter the first number"))
            var2 = int(input("enter the second number"))
            subtract(var1,var2)
        if operation == "3":
            xx1= int(input("Enter the first number"))
            xx2= int(input("Ender the second number"))
            multiply(xx1,xx2)
        if operation == "4":
            yy1= int(input("Enter the first number"))
            yy2= int(input("Ender the second number"))
            divide(yy1,yy2)
        if operation == "5":
            break

#main
calc()
