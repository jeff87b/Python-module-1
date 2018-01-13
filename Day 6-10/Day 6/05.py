unpwlist = ['Sam;Password123\nTom;Password345\nCarla;Password856\n']
myDataFile = open("password.txt", 'w')
myDataFile.write(unpwlist[0])
myDataFile.close()

def readMyDataFile(fileName):
    with open(fileName, mode='r') as myDataFile:
        print(type(myDataFile))
        items = myDataFile.read().splitlines()
        return items


def checkPassword(username, myDataFile):
    for passwords in readMyDataFile(myDataFile):
        password = passwords.split(';')
        #print(password)
        if password[0] == username:
            print("Username is in the list")
            print(password)
            return
    print("Username is not in the list")



checkPassword("Sam", "password.txt")
