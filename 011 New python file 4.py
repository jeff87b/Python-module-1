import random

minimum = int(input("Enter the lower range"))
maximum = int(input("Enter å higher range"))
maxTries = 5

myRandomNumber = (random.randint(minimum, maximum))
print("Guess a number betwin",minimum,"and", maximum)
theNumberGuessed = int(input())
#print(myRandomNumber)
tries = 0

while(tries < maxTries):
    if(theNumberGuessed != myRandomNumber):
        print("Incorrct : Try again!")
        tries = tries + 1
        theNumberGuessed = int(input("Guess again"))
    if(theNumberGuessed == myRandomNumber):
        print("Wohoo!!")
        exit(0)


print("Unfortunately all the guesses were Wrong")

#What if we enter numbers outside the range
#Make a way to continue playing the game
