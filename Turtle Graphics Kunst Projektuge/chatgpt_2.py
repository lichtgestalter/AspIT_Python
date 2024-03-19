import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
# The official documentation for turtle is here: https://docs.python.org/3.3/library/turtle.html.


def chatgpt_2(myturtle):
    # Prompt: Change some_turtle_function() so that it draws a landscape with a farmhouse and some birch trees.
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
    myturtle.penup()
    myturtle.goto(100, -150)
    myturtle.pendown()
    myturtle.color("brown")
    myturtle.begin_fill()
    myturtle.setheading(90)
    myturtle.forward(50)
    myturtle.setheading(0)
    myturtle.forward(20)
    myturtle.setheading(270)
    myturtle.forward(50)
    myturtle.end_fill()

    # Draw birch tree trunks
    myturtle.color("brown")
    for _ in range(3):
        myturtle.penup()
        myturtle.goto(100, -150)
        myturtle.setheading(90)
        myturtle.forward(50)
        myturtle.pendown()
        myturtle.begin_fill()
        myturtle.setheading(270)
        myturtle.circle(20, 180)
        myturtle.end_fill()
        myturtle.left(120)

    # Drawing the birch tree tops
    myturtle.penup()
    myturtle.goto(100, -100)
    myturtle.pendown()
    myturtle.color("green")
    myturtle.begin_fill()
    myturtle.circle(50)
    myturtle.end_fill()

    myturtle.penup()
    myturtle.goto(130, -50)
    myturtle.pendown()
    myturtle.begin_fill()
    myturtle.circle(30)
    myturtle.end_fill()

    myturtle.penup()
    myturtle.goto(80, -25)
    myturtle.pendown()
    myturtle.begin_fill()
    myturtle.circle(20)
    myturtle.end_fill()


def main():
    myturtle = turtle.Turtle()  # create an object of type Turtle
    myturtle.speed(0)  # Increase the drawing speed for faster rendering
    chatgpt_2(myturtle)
    turtle.done()  # keeps the turtle window open after the program is done


if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()

