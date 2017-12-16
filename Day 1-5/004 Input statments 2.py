print ("Please enter the radius of the circle :")

myConstPi=3.14

radius = float(input("Enter a radius: "))

if radius > 0:

  print("You have entered a radius", radius)

  print("Omkrets er ", 2*myConstPi*radius)
else:
  print("Kan ikke finne omkrets negativ tall som radius")
