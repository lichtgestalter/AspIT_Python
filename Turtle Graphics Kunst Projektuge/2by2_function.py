import turtle
from random import random, randint


def two_by_two_function(myturtle, iterations, scale):
    x = 0.0
    y = 0.0
    hop = 250
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(0, -300)
    color = "green"

    for i in range(iterations):
        r = random()
        if r < 0.15:
            if color == "green":
                turtle.pendown()
            xn = randint(0, hop)
            yn = randint(0, hop)
            color ="red"
        elif r < 0.3:
            if color == "green":
                turtle.pendown()
            xn = randint(-hop, 0)
            yn = randint(-hop, 0)
            color ="blue"
        elif r < 0.5:
            if color == "green":
                turtle.pendown()
            xn = randint(-hop*0.3, hop*0.3)
            yn = randint(-hop, 0)
            color ="purple"
        else:
            xn =  0.15 * x +  0.28 * y -  26
            yn =  0.26 * x +  0.24 * y +  44
            color ="green"

        turtle.color("lightgrey")
        turtle.setpos(xn * scale, yn * scale)  # Scale up the coordinates for better visibility
        turtle.dot(12, color)
        turtle.penup()

        x = xn
        y = yn
        print(i, x, y)



def main():
    turtle.setup(width=1400, height=900)
    iterations = 600
    myturtle = turtle.Turtle()  # create an object of type Turtle
    myturtle.speed(0)  # Increase the drawing speed for faster rendering
    two_by_two_function(myturtle, iterations, scale=1.7)
    turtle.done()  # keeps the turtle window open after the program is done


if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()
