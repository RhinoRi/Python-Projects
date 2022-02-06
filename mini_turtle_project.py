# mini drawing project created in python module called turtle!
import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for each_color in ['blue', 'yellow', 'green', 'orange', 'purple', 'white', 'red']:
        turtle.color(each_color)
        turtle.circle(130)
        turtle.right(10)  # Angle 50 because number of colors I added are 7 if it is 6 angle will be 60
turtle.done()  # Allows the screen to stay
