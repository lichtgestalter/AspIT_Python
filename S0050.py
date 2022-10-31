# Læs https://www.freecodecamp.org/news/the-python-handbook/#classesinpython

class Vehicle:  # this starts the definition of a class

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle()  # car1 is now defined as an object of type Vehicle
print(type(car1))
print(car1)
car1.wheels = 4  # the property wheels is now defined for the object car1 of class Vehicle
print("wheels", car1.wheels)
car1.maxspeed = 160  # the property maxspeed is now defined for the object car1 of class Vehicle
print("maximum speed", car1.maxspeed)
car1.drive()  # the method drive of the class Vehicle is called on the object car1
