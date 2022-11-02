# Object oriented role playing game:

# define a class Character with properties name, health, power and mana
# add a constructor (__init__)
# add a method for printing out class objects (__repr__)
# add a method hit(other).

class Character:

    def __init__(self, name, health, power, mana=0):
        self.name = name
        self.health = health
        self.power = power
        self.mana = mana

    def __repr__(self):
        return f"Character: {self.name=} {self.health=} {self.power=} {self.mana=} "

    def hit(self, other):
        other.health -= self.power

    def heal(self, other):
        other.health += self.power


hero1 = Character("Brunhilde", 100, 10, 15)
print(hero1)