import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
# The official documentation for turtle is here: https://docs.python.org/3.3/library/turtle.html.

def chatgpt_1(myturtle):
    # Prompt: In the following program, add code to some_turtle_function to produce nice art.

    # Drawing a complex pattern
    for _ in range(6):  # Loop to create 6 shapes forming a circle
        for _ in range(6):  # Loop to create a hexagon
            for _ in range(6):  # Loop to create a small triangle inside the hexagon
                myturtle.forward(50)
                myturtle.right(60)
            myturtle.right(60)
        myturtle.right(10)  # Turning to draw the next shape



def main():
    myturtle = turtle.Turtle()  # create an object of type Turtle
    myturtle.speed(0)  # Increase the drawing speed for faster rendering
    chatgpt_1(myturtle)
    turtle.done()  # keeps the turtle window open after the program is done


if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()

