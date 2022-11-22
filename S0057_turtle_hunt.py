"""
Exercise "Turtle Hunt":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Step 1:
    Understand the program code as it is now.
    Find out what the code does. For example by changing the code a bit and running it again.

Step 2:
    Change the name of class PlayerName1 in the first line of it's class definition to your personal class name.
    Near the bottom of this script, set the variables class1 and class2 to your personal class name.
    In your personal class, make the methods rotate_prey and rotate_hunter smarter.
    Possibly you'll also want to add some attributes and/or methods to your class.

Step 3:
    Find a sparring partner in your study group.
    As with everything else, ask your teacher for help, if needed.
    In your code, replace the whole class PlayerName2 with your sparring partner's class.
    Set the variable class2 to your sparring partner's class name.
    Let the 2 classes fight and learn from the results in order to improve your code.
    Repeat this step until you are happy :-)

Step 4:
    When your program is complete, push it to your github repository.
    Then send this Teams message to your teacher: <filename> done
    Thereafter go on with the next file.

Later:
    When everyone is done with this exercise, we will hold a tournament
    to find out, who programmed the smartest turtles :)

"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import math
import random

# region edit this


class PlayerName1(turtle.Turtle):

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # self: the turtle that shall be rotated
        # positions: a list of tuples. Each tuple is a pair of coordinates (x,y).
        # positions[0] is the coordinate tuple of the prey. positions[0][0] is the x-coordinate of the prey.
        # positions[1], positions[2], positions[3] refer to the hunters.
        degree = 3
        # print(positions[0][1])
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = -0.5
        return degree


class PlayerName2(turtle.Turtle):

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = 2.2
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        degree = 1
        return degree
# endregion

# region do not edit this


def distance(pos1, pos2):  # calculate the distance between 2 points with the Pythagorean equation
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


def direction(start_turtle, end_turtle):
    # returns the direction from start_turtle to end_turtle in degrees
    # 0° is east (plus x-axis), which is also the direction of each turtle at the beginning of each hunt.
    # 90° is south (minus y-axis), 180° is west (minus x-axis), 270° is north (plus y-axis)
    delta_x = end_turtle.position()[0] - start_turtle.position()[0]
    delta_y = end_turtle.position()[1] - start_turtle.position()[1]
    angle = math.atan2(delta_y, delta_x) * 180 / math.pi
    if delta_y < 0:
        return -angle
    else:
        return 360 - angle


def move(turtle_):  # move the turtle and bounce it back when it crosses the window border
    turtle_.forward(STEP_SIZE)
    x, y = turtle_.position()
    if abs(x) > MAX_POS or abs(y) > MAX_POS:
        turtle_.right(180)
        turtle_.forward(BOUNCE_STEP_SIZE)
        turtle_.right(180)


def caught(turtles_, max_distance):  # is a hunter near enough to the prey?
    positions = [t.position() for t in turtles_]  # this is list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
    for hunter_position in positions[1:]:
        if distance(positions[0], hunter_position) < max_distance:
            return True
    return False


def init_positions(turtles_):  # move turtles to their initial random positions
    for turtle_, min_angle, max_angle in zip(turtles_, START_ANGLES_MIN, START_ANGLES_MAX):
        angle = random.randint(min_angle, max_angle)
        turtle_.right(angle)  # turn turtle a random angle
        turtle_.penup()
        turtle_.forward(random.randint(START_DISTANCE_MIN, START_DISTANCE_MAX))  # move turtle a random distance
        turtle_.right(-angle)  # now the turtle points in the original direction again (the x-axis direction, also called east)
        turtle_.pendown()


def hunt(prey_class, hunter_class, color):  # execute the hunt
    # initialize screen:
    screen = turtle.Screen()
    screen.setup(2 * MAX_POS, 2 * MAX_POS)
    # initialize turtles:
    prey = prey_class()
    hunter1 = hunter_class()
    hunter2 = hunter_class()
    hunter3 = hunter_class()
    hunters = [hunter1, hunter2, hunter3]
    turtles = [prey, hunter1, hunter2, hunter3]
    prey.pencolor(color)
    for t in turtles:
        t.speed(SPEED)
        t.shape("turtle")
    init_positions(turtles)

    # the hunt:
    turn = 0
    positions = [t.position() for t in turtles]  # this is list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
    while not caught(turtles, CAUGHT_DISTANCE) and turn < MAX_TURNS:
        turn += 1
        for h in hunters:
            h.right(h.rotate_hunter(positions))
        prey.right(prey.rotate_prey(positions))
        for t in turtles:
            move(t)
            positions = [t.position() for t in turtles]  # this is list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
        # print(prey, "is now at", prey.position())
        # if turn % 15 == 0:
        #     print(direction(prey, hunter1), direction(hunter1, prey))
    # hunt results:
    turtle.clearscreen()
    if turn < MAX_TURNS:
        print(f'Caught after {turn} turns.')
    else:
        print(f'Prey not caught after {turn} turns. Prey receives {turn} bonus points on top.')
        turn *= 2
    return turn
# endregion


# region edit this
# edit these global constants only for debugging purposes:
MAX_TURNS = 100       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.

random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes
class1 = PlayerName1  # (red prey) Replace PlayerName1 by your own class name here.
class2 = PlayerName2  # (green prey) For testing your code, replace PlayerName2 by your own class name here. Later replace this by your sparring partner's class name.
# endregion


# region do not edit this
# Global constants
MAX_POS = 300    # x and y coordinates must be between -MAX_POS and +MAX_POS. (0, 0) is in the center of the screen.
BOUNCE_STEP_SIZE = 2 * STEP_SIZE         # a turtle trying to leave the window, gets thrown back so many pixels
START_ANGLES_MIN = [0, 90, 180, 270]     # minimum initial right rotation of each turtle
START_ANGLES_MAX = [30, 120, 210, 300]   # maximum initial right rotation of each turtle
START_DISTANCE_MIN = int(MAX_POS * 0.6)  # minimum initial move of all turtles
START_DISTANCE_MAX = int(MAX_POS * 0.9)  # maximum initial move of all turtles

score1 = score2 = 0
for r in range(ROUNDS):
    score1 += hunt(class1, class2, "red")
    score2 += hunt(class2, class1, "green")  # hunter class and prey class have switched roles now!
    print(f"Score after round {r + 1}: {class1.__name__}: {score1}    {class2.__name__}: {score2}")
# turtle.done()  # keeps the turtle window open after the program is done
# endregion
