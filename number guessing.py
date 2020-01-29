import random
chance=10
randomnumber=random.randint(1,99)
print("enter the number from 1 to 99:")
while chance!=0:
    guess=int(input())
    if (guess<randomnumber):
        print("the guess is too low:")
    elif(guess>randomnumber):
        print("the guess is too high:")
    else:
        print("the guess is equal:")
        break
    chance=chance-1
print("game over")
    
