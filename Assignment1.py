import random
jackpot=random.randint(0,100)
userInput=int(input("Enter the Number"))
i=1
while userInput!=jackpot:
    if userInput>jackpot:
     print("guess lower")
     userInput=int(input("Enter the Number"))
    else:
       print("guess higher")
       userInput=int(input("Enter the Number"))
    i+=1

print("coreected")
print("you took",i ,"attempts")

    
