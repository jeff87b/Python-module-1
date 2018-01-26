def isLeapYear(year_entered):
    check_divisible_by_4 = year_entered % 4
    check_divisible_by_100 = year_entered % 100
    if check_divisible_by_4 == 0 and check_divisible_by_100 != 0:
        print(lowerRange)

    elif check_divisible_by_4 == 0 and check_divisible_by_100 == 0:
        check_divisible_by_400 = year_entered % 400
        if check_divisible_by_100 == 0 and check_divisible_by_400 != 0:
            print("Special years that is not a leap year = " + str(lowerRange))
        else:
            print(lowerRange)
    else:
        pass
    return


yearEntered = input("Enter year range: ")
while True:
    if yearEntered == "-h":
        print("Help text: x-y")
        yearEntered = input()
    if "-" in yearEntered:
        if not yearEntered == "-h":
            break
    else:
        print("Help text: x-y")
        yearEntered = input()


rangeEntered = yearEntered.split("-")
lowerRange = int(rangeEntered[0])
higherRange = int(rangeEntered[1])

count = 0
while lowerRange < higherRange:
    isLeapYear(lowerRange)
    lowerRange = lowerRange + 1

isLeapYear(higherRange)
