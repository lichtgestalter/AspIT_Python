"""Opgave "Turtle Hunt": hovedprogram

Du må ikke redigere denne fil!

Kør denne fil for at starte skildpaddejagten.

Læs øvelsesbeskrivelsen i th1_exercise.py."""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random
import th4_classes_constants as Tclass
from th3_service import distance

# do NOT change these global constants!
MAX_POS = 300    # x and y coordinates must be between -MAX_POS and +MAX_POS. (0, 0) is in the center of the screen.
BOUNCE_STEP_SIZE = 2 * Tclass.STEP_SIZE  # a turtle trying to leave the window, gets thrown back so many pixels
START_ANGLES_MIN = [0, 90, 180, 270]     # minimum initial right rotation of each turtle
START_ANGLES_MAX = [30, 120, 210, 300]   # maximum initial right rotation of each turtle
START_DISTANCE_MIN = int(MAX_POS * 0.6)  # minimum initial move of all turtles
START_DISTANCE_MAX = int(MAX_POS * 0.9)  # maximum initial move of all turtles


def move(turtle_):  # move the turtle and bounce it back if it crosses the window border
    turtle_.forward(Tclass.STEP_SIZE)
    x, y = turtle_.position()
    if abs(x) > MAX_POS or abs(y) > MAX_POS:
        turtle_.right(180)
        turtle_.forward(BOUNCE_STEP_SIZE)
        turtle_.right(180)  # now the turtle points in the original direction again


def caught(turtles_, max_distance):  # is a hunter near enough to the prey?
    positions = [t.position() for t in turtles_]  # this is list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
    for hunter_position in positions[1:]:  # checks all the hunteres to see if there are ind range of prey
        if distance(positions[0], hunter_position) < max_distance:
            return True
    return False


def init_positions(turtles_):  # move turtles to their initial random positions
    for turtle_, min_angle, max_angle in zip(turtles_, START_ANGLES_MIN, START_ANGLES_MAX):
        angle = random.randint(min_angle, max_angle)
        turtle_.right(angle)  # turn turtle a random angle
        turtle_.penup()  # do not draw while moving from now on
        turtle_.forward(random.randint(START_DISTANCE_MIN, START_DISTANCE_MAX))  # move turtle a random distance
        turtle_.right(-angle)  # now the turtle points in the original direction again (the x-axis direction, also called east)
        turtle_.pendown()  # draw while moving from now on


def hunt(hunter_class, prey_class, color):  # execute the hunt
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
        # if turn % 30 == 0:
        #     input()
        #     print(direction(prey, hunter1), direction(hunter1, prey))
    # hunt results:
    turtle.clearscreen()
    if turn < Tclass.MAX_TURNS:
        print(f'Caught after {turn} turns.')
    else:
        print(f'Prey not caught after {turn} turns. Prey receives {turn} bonus points on top.')
        turn *= 2
    return turn


score1 = score2 = 0
for r in range(Tclass.ROUNDS):
    print(f"{Tclass.class1.__name__} is hunting {Tclass.class2.__name__}")
    score2 += hunt(Tclass.class1, Tclass.class2, "red")
    print(f"{Tclass.class2.__name__} is hunting {Tclass.class1.__name__}")
    score1 += hunt(Tclass.class2, Tclass.class1, "green")  # hunter class and prey class have switched roles now!
    print(f"##### Score after round {r + 1}: {Tclass.class1.__name__}: {score1}    {Tclass.class2.__name__}: {score2} #####")
# turtle.done()  # keeps the turtle window open after the program is done
