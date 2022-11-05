# Exercise: Object oriented role playing game:

# Copy this file into your own solution directory. Write your solution into the copy.

# define a class Character with properties name, max_health, _current_health, attackpower.
# _current_health shall be a private property, it is not meant to be changed from outside the class

# add a constructor (__init__) which accepts the classes' properties as parameters
# add a method for printing out class objects (__repr__)

# add a method hit which reduces _current_health of another character by attackpower.
# example: _current_health=80 and attackpower=10: a hit reduces _current_health to 70.

# the method hit may not change the private property _current_health off a (potentially) foreign class
# for this reason we define another method get_hit which reduces _current_health of the object it belongs to by attackpower.

# if you have no idea how to begin, open S0061.py and start from there


