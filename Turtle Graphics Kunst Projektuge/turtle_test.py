import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
# The official documentation for turtle is here: https://docs.python.org/3.3/library/turtle.html.


def some_turtle_function(myturtle):
    myturtle.right(90)
    myturtle.forward(150)
    myturtle.right(70)
    myturtle.forward(50)

def main():
    myturtle = turtle.Turtle()  # create an object of type Turtle
    # myturtle.speed(0)  # Increase the drawing speed for faster rendering
    some_turtle_function(myturtle)
    turtle.done()  # keeps the turtle window open after the program is done


if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()

