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

import S0058_turtle_hunt_classes_constants as Tclass
import S0058_turtle_hunt_library as Tlib


score1 = score2 = 0
for r in range(Tclass.ROUNDS):
    score1 += Tlib.hunt(Tclass.class1, Tclass.class2, "red")
    score2 += Tlib.hunt(Tclass.class2, Tclass.class1, "green")  # hunter class and prey class have switched roles now!
    print(f"Score after round {r + 1}: {Tclass.class1.__name__}: {score1}    {Tclass.class2.__name__}: {score2}")
# turtle.done()  # keeps the turtle window open after the program is done
