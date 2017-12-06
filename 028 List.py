myList = [1, 2, 3, 5, 8, 13]


print(myList)

print(myList[1])
def printMyList():
    for i in range(0, len(myList)):
        print(myList[i])


#Calling the function
printMyList()



def addMyList():
    sumOfList = 0
    print("Summing up my list of numbers")
    for i in range(0, len(myList)):
        sumOfList = sumOfList + myList[i]
    print("The sum of myList is", sumOfList)


addMyList()
