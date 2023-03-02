#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    rem = floor % 6
    if (rem > 2):
        painter.color("blue")
    if (floor >= 21):
        painter.goto(-80, y)
    if (floor >= 42):
        painter.goto(-10, y)
    if (floor == 20):
        y = -150
    if (floor == 41):
        y = -150

    y = y + 5
    floor = floor + 1

    #draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()
