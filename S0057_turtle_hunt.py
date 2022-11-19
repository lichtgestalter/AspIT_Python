"""
Exercise "Turtle Hunt":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Part 1:
    Understand the program code as it is now.

Part 2:
     Define your own class Turtle_yourname.
     Make sure that all students picked an unique class name.

Part 3:

Part 4:

Part 5:

Part 6:

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import math
import random


class TurtleExample1(turtle.Turtle):

    def prey_move(self, hunters_):
        return 0

    def hunter_move(self, prey_):
        return 0


class TurtleExample2(turtle.Turtle):

    def prey_move(self, hunters_):
        return -10

    def hunter_move(self, prey_):
        return 10


def distance(pos1, pos2):
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


def move(turtle_):
    turtle_.forward(STEP_SIZE)
    x, y = turtle_.position()
    if x > MAX_POS or y > MAX_POS:
        turtle_.right(180)
        turtle_.forward(BOUNCE_STEP_SIZE)
        turtle_.right(180)


def caught(turtles_, max_distance):
    positions = [t.position() for t in turtles_]  # this is list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
    for hunter_position in positions[1:]:
        if distance(positions[0], hunter_position) < max_distance:
            return True
    return False


def init_positions(turtles_):
    for turtle_ in turtles_:
        turtle_.right(random.randint(0, 360))
        turtle_.forward(MAX_POS*0.7)


def hunt(prey_class_, hunter_class_):
    screen = turtle.Screen()
    screen.setup(2 * MAX_POS, 2 * MAX_POS)
    prey = prey_class_()
    hunter1 = hunter_class_()
    hunter2 = hunter_class_()
    hunter3 = hunter_class_()
    hunters = [hunter1, hunter2, hunter3]
    turtles = [prey, hunter1, hunter2, hunter3]
    prey.pencolor("red")  # draw in red
    for t in turtles:
        t.speed(SPEED)
    init_positions(turtles)
    turn = 0
    while caught(turtles, CAUGHT_DISTANCE):  # debug not
        turn += 1
        for h in hunters:
            h.right(h.hunter_move(prey))
        prey.right(prey.prey_move(hunters))
        for t in turtles:
            move(t)
        print(prey, "is now at", prey.position())

    print("Caught after", turn, "turns")
    for t in turtles:
        print(t, "is now at", t.position())
    return turn


MAX_POS = 300  # x and y coordinates must be between -MAX_POS and +MAX_POS. (0, 0) is in the center of the screen.
STEP_SIZE = 3  # distance each turtle moves in one turn
SPEED = 0  # fastest: 10, slowest: 1, max speed: 0
CAUGHT_DISTANCE = 360  #
BOUNCE_STEP_SIZE = 5

prey_class = TurtleExample1
hunter_class = TurtleExample2

hunt(prey_class, hunter_class)
turtle.done()  # keeps the turtle window open after the program is done
