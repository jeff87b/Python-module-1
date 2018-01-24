yearEntered = int(input("Enter a year: "))

def isLeapYear(year_entered):
    leapYearAlg = year_entered % 4
    if leapYearAlg == 0:
        print("Yes it's a leap year")
    else:
        print("No, it's not a leap year")


isLeapYear(yearEntered)
