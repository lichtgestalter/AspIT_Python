"""
Exercise "Turtle Hunt":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Step 1:
    Understand the program code as it is now.
    Find out what the code does. For example by changing the code a bit and running it again.
    If you changed the code, copy this file's original into your own solution directory again,
    before you go on with the following steps.

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
import S0058_turtle_hunt_classes_constants as Tclass


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
    turtle_.forward(Tclass.STEP_SIZE)
    x, y = turtle_.position()
    if abs(x) > Tclass.MAX_POS or abs(y) > Tclass.MAX_POS:
        turtle_.right(180)
        turtle_.forward(Tclass.BOUNCE_STEP_SIZE)
        turtle_.right(180)


def caught(turtles_, max_distance):  # is a hunter near enough to the prey?
    positions = [t.position() for t in turtles_]  # this is list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
    for hunter_position in positions[1:]:
        if distance(positions[0], hunter_position) < max_distance:
            return True
    return False


def init_positions(turtles_):  # move turtles to their initial random positions
    for turtle_, min_angle, max_angle in zip(turtles_, Tclass.START_ANGLES_MIN, Tclass.START_ANGLES_MAX):
        angle = random.randint(min_angle, max_angle)
        turtle_.right(angle)  # turn turtle a random angle
        turtle_.penup()
        turtle_.forward(random.randint(Tclass.START_DISTANCE_MIN, Tclass.START_DISTANCE_MAX))  # move turtle a random distance
        turtle_.right(-angle)  # now the turtle points in the original direction again (the x-axis direction, also called east)
        turtle_.pendown()


def hunt(prey_class, hunter_class, color):  # execute the hunt
    # initialize screen:
    screen = turtle.Screen()
    screen.setup(2 * Tclass.MAX_POS, 2 * Tclass.MAX_POS)
    # initialize turtles:
    prey = prey_class()
    hunter1 = hunter_class()
    hunter2 = hunter_class()
    hunter3 = hunter_class()
    hunters = [hunter1, hunter2, hunter3]
    turtles = [prey, hunter1, hunter2, hunter3]
    prey.pencolor(color)
    for t in turtles:
        t.speed(Tclass.SPEED)
        t.shape("turtle")
    init_positions(turtles)

    # the hunt:
    turn = 0
    positions = [t.position() for t in turtles]  # this is list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
    while not caught(turtles, Tclass.CAUGHT_DISTANCE) and turn < Tclass.MAX_TURNS:
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
    if turn < Tclass.MAX_TURNS:
        print(f'Caught after {turn} turns.')
    else:
        print(f'Prey not caught after {turn} turns. Prey receives {turn} bonus points on top.')
        turn *= 2
    return turn
# endregion
