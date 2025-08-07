"""
Nedarvning og polymorphisme:

Nu ønsker vi at repræsentere en elbil med klassen ElectricVehicle.
Dens attributter og metoder ligner klassen Vehicle, men er ikke identiske.
Tilsammen kaldes attributter og metoder for klassens medlemmer.
Vi behøver ikke at copy&paste klassekoden fra Vehicle. I stedet definerer vi klassen ElectricVehicle på grundlag af klassen Vehicle.
På denne måde arver ElectricVehicle sine attributter og metoder fra Vehicle.

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


class ElectricVehicle(Vehicle):  # class ElectricVehicle inherits from class Vehicle

    def __init__(self, wheels, max_speed, battery_capacity):
        super().__init__(wheels, max_speed)  # super() refers to the parent class (Vehicle). That way we can reuse the code of Vehicle.__init__
        # Vehicle.__init__(self, wheels, max_speed)  # would do exactly the same as the line above but is not as flexible
        self.battery_capacity = battery_capacity

    def __repr__(self):
        return f"ElectricVehicle: {self.wheels} wheels, {self.max_speed} km/h maximum speed, {self.battery_capacity} kW capacity"

    def drive(self):  # this replaces the function drive from the parent class (Vehicle). This is called method overriding.
        print("ssssssssss")


car1 = Vehicle(4, 160)
ecar = ElectricVehicle(8, 100, 90)

print(car1)
car1.drive()
print(ecar)
ecar.drive()  # polymorphism
# we seem to just have called the same function "drive" for objects of different types
# in reality we called Vehicle.drive() and ElectricVehicle.drive()
# this is called polymorphism (= many forms). It makes life a lot easier for programmers
# for example can we now have objects of different types in a list and process them conveniently in a for loop:
print("\nfor loop:")
cars = [car1, ecar]
for car in cars:
    car.drive()
