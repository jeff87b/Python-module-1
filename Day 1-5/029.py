import turtle

myTurtle = turtle.Turtle()
averageTemperatureList = [3, 4, 6, 9, 14, 17, 18, 17, 8, 2]
numberOfRainyDays = [22, 19, 19, 18, 17]
def drawRectangle():

    for i in range(0, len(averageTemperatureList)):
        myTurtle.left(90)
        myTurtle.forward(20)
        myTurtle.left(90)
        myTurtle.forward(averageTemperatureList[i])
        myTurtle.left(90)
    turtle.done()

def pulse(height, width):
    #myTurtle.penup()
    #myTurtle.setpos(-300, 0)
    #myTurtle.pendown()
    #myTurtle.color('red')
    #myTurtle.pensize(3)
    #myTurtle.speed(100)
    myTurtle.left(90)
    myTurtle.forward(height*10)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height*10)
    myTurtle.left(90)
    myTurtle.forward(40)

        #return myTurtle



#drawRectangle()
for temp in averageTemperatureList:
    print("temp now is :", temp)
    if temp > 10:
        myTurtle.color('red')
    else:
        myTurtle.color('black')


    pulse(temp, 25)



turtle.done()
