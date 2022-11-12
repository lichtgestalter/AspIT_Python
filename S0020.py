"""
Exercise "Tom the Turtle":

Copy this file into your own solution directory. Write your solution into the copy.

The function demo introduces you to all commands you need, to interact with Tom in the following exercises.

Part 1:
write a function square which accepts a parameter "length".
calling this function causes the turtle to draw a square with a side length of "length" pixels.

Part 2:
write a for loop in the main program, which calls square()
in order to draw several squares of different sizes in different positions.

Part 3:
write a function that produces patterns similar to this:
https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Part 4:
write a function that produces patterns similar to this:
https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/

Part 5:
Create your own function that produces a cool pattern.
Later, if you like, present your pattern on the big screen to the others.

When your program is complete, push it to your github repository
then send this Teams message to your teacher: I am done with exercise "Tom the Turtle"
Thereafter go on with the next file in numerical order in the teacher's exercise repository after the current exercise.
"""

import turtle    # this imports a library called "random". A library is (someone else's) python code, that you can use in your own program.


def demo():  # demonstration of basic turtle commands
    tom.speed(1)  # fastest: 10, slowest: 1
    tom.forward(100)  # move 100 pixels
    tom.left(45)  # turn 45 degrees left
    tom.penup()  # do not draw while moving
    tom.forward(50)
    tom.pendown()  # draw while moving
    tom.pencolor("red")  # from now on, draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(100)
    tom.home()  # return to the original position in the middle of the window


tom = turtle.Turtle()  # define a variable tom of type Turtle
demo()
turtle.done()  # keeps the turtle window open after the program is done
