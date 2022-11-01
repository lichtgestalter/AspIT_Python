# Læs https://www.freecodecamp.org/news/the-python-handbook/#classesinpython

# now we write the same program again,
# but in an object oriented way.

class Vehicle:  # this starts the definition of a class

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle()  # car1 is now defined as an object of type Vehicle
car1.wheels = 4  # the property wheels is now defined for the object car1 of class Vehicle
car1.max_speed = 160  # the property maxspeed is now defined for the object car1 of class Vehicle
car1.drive()  # the method drive of the class Vehicle is called on the object car1

print(1, type(car1))
print(2, car1)
print(3, "wheels", car1.wheels)
print(4, "maximum speed", car1.max_speed)
