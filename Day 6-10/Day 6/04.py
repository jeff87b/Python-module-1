# Read file:
myDataFile = open("shopping.txt", 'a')
myDataFile.close()


def readMyDataFile(shoppingListFile):
    with open(shoppingListFile, mode='r') as myDataFile:
        print(type(myDataFile))
        items = myDataFile.read().splitlines()
        return items

readMyDataFile("shopping.txt")

print(type(readMyDataFile))

def writeDataToANewList(shoppingList):
    with open("shopping.txt", 'w') as myDataFile:
        for element in shoppingList:
            myDataFile.write(element+'\n')



shoppingList = ['Banana', 'Apple', 'Tacos']
writeDataToANewList(shoppingList)


# def seeIfItemExists(item):
#     with open("shopping.txt", 'r') as ifSomethingIsInFile:
#         elementsInFile = ifSomethingIsInFile.read().splitlines()
#         for element in elementsInFile:
#             print(element)
#             if element == item:
#                 print("The item exists in my shopping list")
#             else:
#                 print("The item doesnt exist in my shopping list")
#
# seeIfItemExists("Apple")

def doesElementExistInShoppingList(item):
    myShoppingList = readMyDataFile("shopping.txt")
    for myItem in myShoppingList:
        print(myItem)
        if myItem == item:
            print("This exists in my shopping list")
            return myItem
    print("The item does not exist in my shopping list")


#doesElementExistInShoppingList("Apple")

print(doesElementExistInShoppingList("Apple"))
