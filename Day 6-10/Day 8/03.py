yearEntered = int(input("Enter a year: "))

def isLeapYear(year_entered):
    leapYearAlg_1 = year_entered % 4
    LeapYearAlg_2 = year_entered % 100
    LeapYearAlg_3 = year_entered % 400
    if leapYearAlg_1 == 0 and LeapYearAlg_2 == 0 and LeapYearAlg_3 == 0:
        print("Yes it's a leap year")
    else:
        print("No, it's not a leap year")


isLeapYear(yearEntered)
