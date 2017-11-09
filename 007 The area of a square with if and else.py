print ("This program calculates the area of a square.")
side1 = float(input("Enter side number one: "))
side2 = float(input("Enter side number two:"))
print("The area is:", side1*side2)
if side1<0:
    print("You have entered a negative first number")
else:
    print("The first number is ok")

if side2<0:
    print("You have entered a negative second number")
else:
    print("The second number is ok")
