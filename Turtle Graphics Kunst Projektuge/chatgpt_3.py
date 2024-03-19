import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
# The official documentation for turtle is here: https://docs.python.org/3.3/library/turtle.html.

def chatgpt_3(myturtle):
    # Prompt: Change the function so the farm house and trees are shown from the perspective of someone standing on the ground.
    myturtle.speed(10)  # Increase the drawing speed for faster rendering

    # Drawing the farmhouse
    myturtle.penup()
    myturtle.goto(-200, -150)
    myturtle.pendown()
    myturtle.color("brown")
    myturtle.begin_fill()
    for _ in range(4):
        myturtle.forward(100)
        myturtle.right(90)
    myturtle.end_fill()

    # Drawing the roof
    myturtle.color("red")
    myturtle.begin_fill()
    myturtle.goto(-200, -50)
    myturtle.setheading(45)
    myturtle.forward(70)
    myturtle.setheading(315)
    myturtle.forward(70)
    myturtle.end_fill()

    # Drawing the door
    myturtle.penup()
    myturtle.goto(-160, -150)
    myturtle.pendown()
    myturtle.color("brown")
    myturtle.begin_fill()
    myturtle.setheading(90)
    myturtle.forward(50)
    myturtle.setheading(0)
    myturtle.forward(30)
    myturtle.setheading(270)
    myturtle.forward(50)
    myturtle.end_fill()

    # Drawing the birch trees
    tree_positions = [(100, -150), (20, -180), (-60, -170)]
    for x, y in tree_positions:
        draw_birch_tree(myturtle, x, y)


def draw_birch_tree(myturtle, x, y):
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()

    # Draw birch tree trunk
    myturtle.color("brown")
    myturtle.begin_fill()
    myturtle.setheading(90)
    myturtle.forward(20)
    myturtle.setheading(270)
    myturtle.circle(10, 180)
    myturtle.end_fill()

    # Drawing the birch tree tops
    myturtle.penup()
    myturtle.setheading(90)
    myturtle.forward(20)
    myturtle.pendown()
    myturtle.color("green")
    myturtle.begin_fill()
    myturtle.circle(30)
    myturtle.end_fill()

    myturtle.penup()
    myturtle.setheading(270)
    myturtle.forward(20)
    myturtle.setheading(90)
    myturtle.forward(30)
    myturtle.setheading(270)
    myturtle.pendown()
    myturtle.begin_fill()
    myturtle.circle(20)
    myturtle.end_fill()


def some_other_turtle_function(myturtle):
    myturtle.right(90)
    myturtle.forward(150)
    myturtle.right(70)
    myturtle.forward(50)

def main():
    myturtle = turtle.Turtle()  # create an object of type Turtle
    myturtle.speed(0)  # Increase the drawing speed for faster rendering
    chatgpt_3(myturtle)
    turtle.done()  # keeps the turtle window open after the program is done


if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()

