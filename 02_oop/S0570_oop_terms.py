"""
Denne fil er beregnet til at give dig et overblik over de
de vigtigste termer inden for objektorienteret programmering.

Læs den omhyggeligt og brug den som opslagstavle, når du løser de følgende opgaver."""


class ClassName:
    def __init__(self, parameter1, parameter2):  # constructor, magic function
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def __repr__(self):  # magic function, defines how objects are printed. Magic function names always start and end with two underscores.
        return f"ClassName: {self.attribute1=} {self.attribute2=}"

    def method1(self):
        print("This is method1")
        self._protected_method()  # Calling the protected method from inside its class. This is ok.

    def _protected_method(self):  # encapsulation: protected method or attribute names always start with one underscore
        print("This is a protected method. Call it only from inside its class.")


class ClassName2(ClassName):  # ClassName2 inherits all methods and attributes from ClassName

    def method1(self):
        print("This is another method1")


print("--- Class: ClassName, Object: Object1 ---")
object1 = ClassName(4, 160)  # creates an instance/object by calling the constructor __init__
object1.method1()  # calls method1 on object1
object1._protected_method()  # don't do this
print(object1)  # calls internally __repr__ on object1

print("\n--- Class: ClassName2, Object: Object2 ---")
object2 = ClassName2(12, 99)  # creates an instance of class ClassName2.  ClassName2 doesn't have its own function __init__, so it uses the inherited __init__ of class ClassName
print(object2)  # calls internally __repr__ on object1
object2.method1()  # calls method1 on object2

print("\n--- Example for polymorphism ---")
objectlist = [object1, object2]
for obj in objectlist:
    obj.method1()  # calls different versions of method1(). Example for polymorphism.
