"""
__repr__ og f-strings:

Alle klasser i python har en funktion __repr__, der definerer output af udskrivning af et objekt af denne klasse.
Hver klasse i python har automatisk nogle nyttige funktioner, som begynder og slutter med to understregninger.
Vi kan overskrive disse funktioner. De kaldes magiske funktioner eller dunder functions.
I dette eksempel bruger vi såkaldte f-strings. De er meget praktiske.
Læs mere om f-strings her: https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python

Inspicer følgende kode i detaljer. Find ud af, hvad hver række kode gør.
F.eks. ved at ændre koden en smule og derefter køre/debugge programmet.

Derefter går du videre med den næste fil."""


class Vehicle:  # this starts the definition of a class

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an instance/object of a class
        self.wheels = wheels  # wheels is called an attribute. A attribute is a variable that belongs to an object of a class.
        self.max_speed = max_speed  # Another attribute.

    def __repr__(self):
        return f"Vehicle: {self.wheels} wheels, {self.max_speed} km/h maximum speed"

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle(4, 160)  # car1 is now defined as an instance/object of type Vehicle. Also its attributes are already defined.
car2 = Vehicle(8, 100)

print(car1)
print(car2)
car1.drive()  # the method drive of the class Vehicle is called on the object car1
