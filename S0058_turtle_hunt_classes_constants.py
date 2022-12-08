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
import random


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


# change these global constants only for debugging purposes:
MAX_TURNS = 100       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.

random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes
class1 = PlayerName1  # (red prey) Replace PlayerName1 by your own class name here.
class2 = PlayerName2  # (green prey) For testing your code, replace PlayerName2 by your own class name here. Later replace this by your sparring partner's class name.


# do NOT change these global constants!
MAX_POS = 300    # x and y coordinates must be between -MAX_POS and +MAX_POS. (0, 0) is in the center of the screen.
BOUNCE_STEP_SIZE = 2 * STEP_SIZE         # a turtle trying to leave the window, gets thrown back so many pixels
START_ANGLES_MIN = [0, 90, 180, 270]     # minimum initial right rotation of each turtle
START_ANGLES_MAX = [30, 120, 210, 300]   # maximum initial right rotation of each turtle
START_DISTANCE_MIN = int(MAX_POS * 0.6)  # minimum initial move of all turtles
START_DISTANCE_MAX = int(MAX_POS * 0.9)  # maximum initial move of all turtles
