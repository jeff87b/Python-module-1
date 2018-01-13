
#var1 = "hello"

#print(type(var1))


myNumber = int(input("Enter a number: "))


print(type(myNumber))


sumOfDigits = 0

while myNumber > 0:
    sumOfDigits = sumOfDigits + myNumber % 10
    myNumber = int(myNumber / 10)
    print("sumOfDigits =", sumOfDigits, "myNumber =", myNumber)

print("Sum of digits is " + str(sumOfDigits))

print(5%3)
print(5/3)
