myCreditCardNumber = input("Enter a credit card number: ")

if len(myCreditCardNumber) != 16:
    print("The number should be 16 digits")

doubleOfDigits = []

def doubleAlternateDigits(number):
    for i in range(0, len(number)):
        if(i % 2 == 0):
            doubleOfDigits.append(int(number[i])*2)


doubleAlternateDigits(myCreditCardNumber)

print(doubleOfDigits)

def validationStep2():
    for i in range(0, len(doubleOfDigits)):
        addDigits(doubleOfDigits[i])


def validationStep3():
