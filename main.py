

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press CTRL + MouseWheel for font size changes
# Turtle module for star graphics

import turtle
sc = turtle.Screen()
sc.setup(500, 500)
spiral = turtle.Turtle()
spiral.speed(5)
sc.bgcolor("white")
col = ("yellow", "green", "blue", "red")
c = 0

for i in range(60):
    spiral.forward(i+10)
    spiral.right(144)          # use 134 or 144
    spiral.color(col[c])
    if c == 3:
        c = 0
    else:
        c += 1
