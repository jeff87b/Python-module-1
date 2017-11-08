birthYear = int(input("Enter your birth year"))

if (birthYear <= 1900):
    print("Thats to old")
    exit(0)

currentYear = int(input("What year are we in now?"))

if birthYear > currentYear:
    print("You are not yet born")
    exit(0)

yearIEntered = int(input("Enter a year"))

if yearIEntered<birthYear:
    print("I can not calculate your age in the past")
    exit(0)

print("My age in", yearIEntered, "will be" ,yearIEntered-birthYear)

#Tasks for homework
#1) What if its
