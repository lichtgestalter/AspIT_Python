"""
Classes, methods, attributes:

Read https://www.freecodecamp.org/news/the-python-handbook/#classesinpython

Now we write the same cars program again, but in an object oriented way.

Inspect the following code in detail. Find out what every row of code does.
For example by changing the code a bit and then running/debugging the program.

Thereafter go on with the next file.
"""


class Vehicle:  # this starts the definition of a class

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle()  # car1 is now defined as an object of type Vehicle. car1 is an instance of class Vehicle.
car1.wheels = 4  # the attribute wheels is now defined for the instance car1 of class Vehicle
car1.max_speed = 160  # the attribute max_speed is now defined for the instance car1 of class Vehicle

car2 = Vehicle()
car2.wheels = 8
car2.max_speed = 100

print("wheels", car1.wheels, "maximum speed", car1.max_speed)  # print out the attributes of car1
print("wheels", car2.wheels, "maximum speed", car2.max_speed)  # print out the attributes of car2
car1.drive()  # the method drive of the class Vehicle is called on the object car1
