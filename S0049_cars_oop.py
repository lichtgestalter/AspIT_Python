"""
Constructor:

Now we use a constructor to more elegantly define the cars and their attributes.

Inspect the following code in detail. Find out what every row of code does.
For example by changing the code a bit and then running/debugging the program.

Thereafter go on with the next file.
"""


class Vehicle:  # this starts the definition of a class

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an instance/object of a class
        self.wheels = wheels  # wheels is called an attribute. A attribute is a variable that belongs to an object of a class.
        self.max_speed = max_speed  # Another attribute.

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle(4, 160)  # car1 is now defined as an instance/object of type Vehicle. Also its attributes are already defined.
car2 = Vehicle(8, 100)

print("wheels", car1.wheels, "maximum speed", car1.max_speed)  # print out the attributes of car1
print("wheels", car2.wheels, "maximum speed", car2.max_speed)  # print out the attributes of car2
car1.drive()  # the method drive of the class Vehicle is called on the object car1
