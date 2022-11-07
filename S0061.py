# Exercise: Object oriented role playing game, part 1 :

# Copy this file into your own solution directory. Write your solution into the copy.

# define a class Character with attributes name, max_health, _current_health, attackpower.
# _current_health shall be a private attribute, it is not meant to be changed from outside the class

# add a constructor (__init__) which accepts the classes' attributes as parameters
# add a method for printing out class objects (__repr__)

# add a method hit which reduces _current_health of another character by attackpower.
# example: _current_health=80 and attackpower=10: a hit reduces _current_health to 70.

# the method hit may not change the private attribute _current_health off a (potentially) foreign class
# for this reason we define another method get_hit which reduces _current_health of the object it belongs to by attackpower.

# if you get stuck, ask google, the other pupils or the teacher (in this order).
# if you are still stuck, open S0065.py and compare it with your solution

# when your program is complete, push it to your github repository and
# compare it to the teacher's solution in S006565.py
# then send this Teams message to your teacher: i am done with exercise "role playing game 1"
# thereafter go on with the next file in numerical order in the teacher's exercise repository after the current exercise.


class Character:

    def __init__(self, name, health, attackpower):
        0

    def __repr__(self):
        return ""

    def hit(self, other):
        0

    def get_hit(self, attackpower):
        0

    def get_healed(self, healpower):
        0


class Healer(Character):
    
    def __init__(self, name, health, healpower):
        0

    def heal(self, other):
        0


hero1 = Character("Bozeto", 100, 20)
hero2 = Character("Andananda", 110, 24)
hero3 = Healer("DoctorX", 75, 15)
print(hero1)
print(hero2)
print(hero3)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)

