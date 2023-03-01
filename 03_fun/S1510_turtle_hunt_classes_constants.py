"""
Exercise "Turtle Hunt":

As always, read the whole exercise description carefully before you begin to solve the exercise.

The game:
    This exercise is a game for 2 players.
    3 Turtles (hunters) are trying to catch another turtle (prey) as fast as possible.
    One player controls the prey, the other player controls the hunters. Then the players switch roles.
    In each turn the players decide how many degrees their turtle(s) rotate(s). This is the player's only task.
    The prey gets one point for every turn before it gets caught.
    If the prey is still on the run after MAX_TURNS turns, the points double and the hunt ends.


The code for the game is already written in S1530_turtle_hunt_main.py and S1520_turtle_hunt_service.py. Do not change these files.

Your job is to make the turtles rotate smarter.

Copy all 3 turtle_hunt files into your own solution directory.
Write your solution into your copy of S1510_turtle_hunt_classes_constants.py.

File structure:
    The code is divided into 3 files in order to make it clear which part of the code
    you are supposed to change and which part of the code you shall leave unchanged.

    S1530_turtle_hunt_main.py:
        This is the main program.
        Do not make changes therein.
        Run it in order to start the game.

    S1520_turtle_hunt_service.py:
        Contains some service functions that will be useful to you.
        Do not make changes therein.

    This file (S1510_turtle_hunt_classes_constants.py):
        All your programming for this exercise happens in this file.

Step 1:
    Understand the program code as it is now.
    You do not need to understand every detail of the main program though.
    Understand when and how the methods rotate_prey() and rotate_hunt() are used.
    From now on, all your programming for this exercise happens in this file here.

Step 2:
    Change the name of class PlayerName1 in the first line of it's class definition to your personal class name.
    At the bottom of this file, set the variables class1 and class2 to your personal class name.

Step 3:
    In your personal class, make the methods rotate_prey and rotate_hunter smarter.
    Possibly you'll also want to add some attributes and/or methods to your class.
    You may not manipulate (e.g. move) the turtles with your code though.
    The runtime of your methods rotate_prey and rotate_hunter must be less than 0.1 seconds per iteration.

Step 4:
    Find a sparring partner in your study group.
    As with everything else, ask your teacher for help, if needed.
    In your code, replace the whole class PlayerName2 with your sparring partner's class.
    At the bottom of this file, set the variable class2 to your sparring partner's class name.
    Let the 2 classes fight and learn from the results in order to improve your code.
    Repeat this step until you are happy :-)

Step 5:
    When your program is complete, push it to your github repository.
    Then send this Teams message to your teacher: <filename> done
    Thereafter go on with the next file.

Later:
    When everyone is done with this exercise, we will hold a tournament
    to find out, who programmed the smartest turtles :)

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random
from S1520_turtle_hunt_service import distance, direction


class PlayerName1(turtle.Turtle):

    def __init__(self):
        super().__init__()  # Here, this is equivalent to turtle.Turtle.__init__(self)
        self.orientation = 0  # used to keep track of the turtle's current orientation (the direction it is heading)

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # self: the turtle that shall be rotated
        # positions: a list of tuples. Each tuple is a pair of coordinates (x,y).
        # positions[0] is the coordinate tuple of the prey. positions[0][0] is the x-coordinate of the prey.
        # positions[1], positions[2], positions[3] refer to the hunters.
        # for example is positions[3][1] the y-coordinate of the third hunter.

        # Example for use of the service functions distance() and direction
        # print(f'{distance(positions[0], positions[1])=}   {direction(positions[0], positions[1])=}')  # print distance and direction from prey to hunter1

        degree = 3  # When the turtle rotates the same amount each turn,  it will just run in a circle. Make this function smarter!
        self.orientation += degree
        self.orientation %= 360
        # print(self.orientation)
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # Example for use of the service functions distance() and direction
        # print(f'{distance(self.position(), positions[0])=}   {direction(self.position(), positions[0])=}')  # print distance and direction from the current hunter to the prey
        degree = -0.5  # When the turtle rotates the same amount each turn,  it will just run in a circle. Make this function smarter!
        self.orientation += degree
        self.orientation %= 360
        # print(self.orientation)
        return degree


#  Insert the code of your sparring partner's turtle class here:
#
#
#
#


# change these global constants only for debugging purposes:
MAX_TURNS = 100       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.


random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes. You may change the argument of seed().


class1 = PlayerName1  # (red prey) Replace PlayerName1 by your own class name here.
class2 = PlayerName1  # (green prey) For testing your code, replace PlayerName1 by your own class name here. Later replace this by your sparring partner's class name.
