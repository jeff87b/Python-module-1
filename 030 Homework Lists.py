#Homework after day 4
#1) Write a Python function to sum all the items in a list.
#2) Write a Python function to multiply all the items in a list.
#3) Write a Python function to get the largest number from a list.
#4) Write a Python function to print every third number from a list of numbers until the list becomes empty.
#5) Write a Python function to get the third side of right angled triangle from two given sides. (Pythagorous theorem anyone?)
import math
myList = [1, 2, 3, 57, 8, 13, 25, 50, 30]

def addMyList():
    sumOfList = 0
    for i in range(0, len(myList)):
        sumOfList = sumOfList + myList[i]
    print("Sum of list =", sumOfList)

addMyList()

def multiplyMyList():
    MultiplySum = 1
    for abc in range(0, len(myList)):
        MultiplySum =  MultiplySum * myList[abc]
    print("Multiply sum of list =", MultiplySum)

multiplyMyList()

def highestNumberInList():
    highestNumber = max(myList)
    print("Highest number =", highestNumber)

highestNumberInList()

#alternative 1
def printE3N():
    print (myList[2], myList[5], myList[8])

printE3N()

#alternative 2
def printE3N2():
    for j in range(2, len(myList), 3):
        print (myList[j])

printE3N2()


def hypotenuse():
    a = 50
    b = 50
    print(math.sqrt(a**2 + b**2))

hypotenuse()
