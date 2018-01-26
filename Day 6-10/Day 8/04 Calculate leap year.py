def isLeapYear(year_entered):
    check_divisible_by_4 = year_entered % 4
    check_divisible_by_100 = year_entered % 100
    if check_divisible_by_4 == 0 and check_divisible_by_100 != 0:
        print("Yes it's a leap year")

    elif check_divisible_by_4 == 0 and check_divisible_by_100 == 0:
        check_divisible_by_400 = year_entered % 400
        if check_divisible_by_100 == 0 and check_divisible_by_400 != 0:
            print("No, it's not a leap year")
        else:
            print("Yes it's a leap year")
    else:
        print("No, it's not a leap year")
    return


print("Enter years below")
while True:
    yearEntered = int(input())
    isLeapYear(yearEntered)
