# Object oriented role playing game:

# define a class Character with properties name, max_health, _current_health, attackpower.
# _current_health shall be a private property, it is not meant to be changed from outside the class

# add a constructor (__init__) which accepts the classes' properties as parameters
# add a method for printing out class objects (__repr__)
# add a method hit which reduces _current_health of another character by attackpower.

# the method hit may not change the private property _current_health off a (potentially) foreign class
# for this reason we define another method get_hit which reduces _current_health of the object it belongs to by attackpower.

#

class Character:

    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attackpower = attackpower

    def __repr__(self):
        return f"Character: {self.name=}   {self.max_health=}   {self._current_health=}   {self.attackpower=}"

    def hit(self, other):
        print(self.name, "hits", other.name, "for", self.attackpower, "damage")
        other.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        self._current_health -= attackpower

    def get_healed(self, healpower):
        self._current_health += healpower


class Healer(Character):
    
    def __init__(self, name, health, healpower):
        super().__init__(name, health, 0)
        self.healpower = healpower

    def heal(self, other):
        print(self.name, "xxxxxheals", other.name, "for", self.attackpower, "damage")
        other.get_healed(self.healpower)


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

