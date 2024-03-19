# Write a python  turtle graphics program that draws a a landscape with a few houses, trees, shrubs and a blue sky
# with some white clouds. All houses have a visible 3D-structure which is drawn in correct perspective.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Function to draw a house
def draw_house(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Draw the base of the house
    pen.begin_fill()
    pen.color("lightgrey")
    for _ in range(4):
        pen.forward(80 * size)
        pen.right(90)
    pen.end_fill()

    # Draw the roof
    pen.goto(x - 20 * size, y + 80 * size)
    pen.begin_fill()
    pen.color("brown")
    pen.goto(x + 100 * size, y + 80 * size)
    pen.goto(x, y + 140 * size)
    pen.end_fill()

    # Draw the door
    pen.penup()
    pen.goto(x + 30 * size, y)
    pen.pendown()
    pen.begin_fill()
    pen.color("lightblue")
    pen.setheading(90)
    pen.forward(80 * size)
    pen.right(90)
    pen.forward(40 * size)
    pen.right(90)
    pen.forward(80 * size)
    pen.end_fill()

# Function to draw a tree
def draw_tree(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.begin_fill()
    pen.color("brown")
    pen.setheading(90)
    pen.forward(50)
    pen.setheading(225)
    pen.forward(30)
    pen.setheading(0)
    pen.forward(30)
    pen.setheading(315)
    pen.forward(30)
    pen.setheading(90)
    pen.forward(70)
    pen.end_fill()

    pen.color("green")
    pen.setheading(90)
    pen.forward(70)
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

# Function to draw a cloud
def draw_cloud(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.circle(30, extent=180)
    pen.circle(40, extent=180)
    pen.circle(50, extent=180)
    pen.end_fill()

# Draw houses
draw_house(-250, -200, 1)
draw_house(-100, -200, 0.8)
draw_house(100, -200, 1.2)
draw_house(250, -200, 0.9)

# Draw trees
draw_tree(-200, -250)
draw_tree(-50, -250)
draw_tree(100, -250)
draw_tree(250, -250)

# Draw clouds
draw_cloud(-200, 150)
draw_cloud(100, 200)
draw_cloud(-300, 200)

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()
