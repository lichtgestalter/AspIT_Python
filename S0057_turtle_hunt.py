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


class PlayerName1(turtle.Turtle):

    def prey_rotation(self, hunters_):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = -2
        return degree

    def hunter_rotation(self, prey_):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = 1.5
        return degree


class PlayerName2(turtle.Turtle):

    def prey_rotation(self, hunters_):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = 2.2
        return degree

    def hunter_rotation(self, prey_):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = 0.5
        return degree


def distance(pos1, pos2):
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


def move(turtle_):
    turtle_.forward(STEP_SIZE)
    x, y = turtle_.position()
    if abs(x) > MAX_POS or abs(y) > MAX_POS:
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
    for turtle_, min_angle, max_angle in zip(turtles_, START_ANGLES_MIN, START_ANGLES_MAX):
        angle = random.randint(min_angle, max_angle)
        turtle_.right(angle)
        turtle_.penup()
        turtle_.forward(random.randint(START_DISTANCE_MIN, START_DISTANCE_MAX))
        turtle_.right(-angle)  # now the turtle points in the original direction again (the x-axis direction)
        turtle_.pendown()


def hunt(prey_class_, hunter_class_, color):
    screen = turtle.Screen()
    screen.setup(2 * MAX_POS, 2 * MAX_POS)
    prey = prey_class_()
    hunter1 = hunter_class_()
    hunter2 = hunter_class_()
    hunter3 = hunter_class_()
    hunters = [hunter1, hunter2, hunter3]
    turtles = [prey, hunter1, hunter2, hunter3]
    prey.pencolor(color)
    for t in turtles:
        t.speed(SPEED)
    init_positions(turtles)
    turn = 0

    while not caught(turtles, CAUGHT_DISTANCE) and turn < MAX_TURNS:
        turn += 1
        for h in hunters:
            h.right(h.hunter_rotation(prey))
        prey.right(prey.prey_rotation(hunters))
        for t in turtles:
            move(t)
        # print(prey, "is now at", prey.position())

    turtle.clearscreen()
    if turn < MAX_TURNS:
        print(f'Caught after {turn} turns.')
    else:
        print(f'Prey not caught after {turn} turns. Prey receives {turn} bonus points on top.')
        turn *= 2
    return turn


MAX_TURNS = 200  #
ROUNDS = 2  #
MAX_POS = 300  # x and y coordinates must be between -MAX_POS and +MAX_POS. (0, 0) is in the center of the screen.
STEP_SIZE = 3  # distance each turtle moves in one turn
SPEED = 0  # fastest: 10, slowest: 1, max speed: 0
CAUGHT_DISTANCE = 270  #
BOUNCE_STEP_SIZE = 15  # a turtle trying to leave the window, gets thrown back so many pixels
START_ANGLES_MIN = [0, 90, 180, 270]
START_ANGLES_MAX = [20, 110, 200, 290]
START_DISTANCE_MIN = int(MAX_POS * 0.7)
START_DISTANCE_MAX = int(MAX_POS * 0.9)


class1 = PlayerName1  # change player name here (red prey)
class2 = PlayerName2  # change player name here (green prey)

score1 = score2 = 0

for r in range(ROUNDS):
    score1 += hunt(class1, class2, "red")
    score2 += hunt(class2, class1, "green")  # hunter class and prey class have switched roles now!
    print(f"Score after round {r + 1}: {class1.__name__}: {score1}    {class2.__name__}: {score2}")
turtle.done()  # keeps the turtle window open after the program is done


# next: maxturns hantieren
