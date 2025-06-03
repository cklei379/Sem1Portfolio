#Chloe Lei
#1/29/25
#Slot Machine

#init
import random
symb=["7","✿","✾","✶","✷","✼","✹"]
random.choices(symb, weights=[1,8,8,8,8,8,8], k=3)
global cred
cred=100
#func
#main
print("Come play our slot machine game!\nStarting Credits:100")
while True:
    try:
        if cred>0:
            play=int(input("Do you want to spin or quit? (1: Spin, 2: Quit) "))
            if play==2:
                break
            bet=int(input("Do you want to bet credits? 1: Yes, 2: No "))
            if bet==1:
                bamt=int(input("How many credits do you want to bet? "))
                if bamt>1500 and bamt<cred:
                    random.choices(symb, weights=[5,8,8,6,8,6,6], k=3)
                if 1000<bamt<1500 and bamt<cred:
                    random.choices(symb, weights=[3,8,6,8,8,6,8], k=3)
                if 500<bamt<1000 and bamt<cred:
                    random.choices(symb, weights=[2,8,8,6,8,8,8], k=3)
                elif bamt>cred:
                    print("You do not have enough credits *spin without bets*")
                else:
                    random.choices(symb, weights=[1,8,8,8,8,8,8], k=3)
            if play==1:
                x=random.choice(symb)
                y=random.choice(symb)
                z=random.choice(symb)
                print("[" +str(x)+ "," +str(y)+ ","+str(z)+ "]")
                if x=="7" and y=="7" and z=="7":
                    print("Jackpot!")
                    cred=cred-1
                    cred=cred*50
                    print("Remaining Credits: "+str(cred))
                elif x==y or y==z or x==z:
                    print("Two-of-a-Kind Win!")
                    cred=cred-1
                    cred=cred*2
                    print("Remaining Credits: "+str(cred))
                elif x==y and y==z and x==z:
                    print("Three-of-a-Kind Win!")
                    cred=cred-1
                    cred=cred*10
                    print("Remaining Credits: "+str(cred))
                else:
                    print("Lose :(")
                    cred=cred-1
                    print("Remaining Credits: "+str(cred))
        else:
            print("You have no more credits. You are unable to continue playing.")
    except:
        print("ERROR: Must input a number.")
