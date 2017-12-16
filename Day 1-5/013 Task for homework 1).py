#Tasks for homework
# 1) What if its a new born baby? Greet him/her.
# 2) What if someone's age comes up as 100! congratulate him/her.
# 3) What if someone's age is between 13 and 19? Say hello to the teenager.
# 4) If the person is 10, 20, 30... invite them to a new decade
# 5) If the person's age is a prime number, tell them about it
# 6) Add up the digits in their birth year

birthYear = int(input("Enter your birth year"))
currentYear = int(input("What year are we in now?"))
age = currentYear-birthYear

if birthYear == currentYear:
    print("Welcome to the world")

if currentYear == birthYear + 100:
    print("Congratulations on 100 years of day")

if age >= 13 and age<=19:
    print("hello teenager")

if age == 10 or age == 20 or age == 30 or age == 40 or age == 50 or age == 60 or age == 70 or age == 80 or age == 90 or age == 100 or age == 110:
    print("Welcome to a new decade")

if age == 2 or age == 3  or age== 5 or age== 7 or age== 11 or age== 13 or age== 17 or age== 19 or age== 23 or age== 29 or age== 31 or age== 37 or age== 41 or age== 43 or age== 47 or age== 53 or age== 59 or age== 61 or age== 67 or age== 71 or age== 73 or age== 79 or age== 83 or age== 89 or age== 97 or age== 101 or age== 103 or age== 107 or age== 109 or age== 113:
    print("Your age is a prime number")
