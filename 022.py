#defining a function

def celciusToFahrenheit():
    myInput = int(input("Enter a temperature in celcius: "))
    tempInFahrenheit = (myInput * 9 + 160) / 5
    print("The temp of","in Fahrenheit")

def fahrenheitToCelcius():
    myInput = int(input("Enter a temperature in Fahrenheit: "))
    tempInCelcius = ((myInput - 32) / 9) *5
    print("The temp of ", myInput, "in Fahrenheit is")
        tempInCelcius,"in celcius"

#calling a function
celciusToFahrenheit()
