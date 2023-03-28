"""
This file is meant to give you an overview on the
most important terms in object oriented programming.

Read it carefully and use it as an look up table when solving exercises.
"""


class ClassName:
    def __init__(self, parameter1, parameter2):  # constructor, magic function
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def __repr__(self):  # magic function, defines how objects are printed. Magic function names always start and end with two underscores.
        return f"ClassName: {self.attribute1=} {self.attribute2=}"

    def method1(self):
        print("this is method1")
        self._protected_method()

    def _protected_method(self):  # protected method or attribute names always start with one underscore
        print("Don't call this method from outside this class!")


class ClassName2(ClassName):  # ClassName2 inherits all methods and attributes from ClassName

    def method1(self):
        print("this is another method1")


print("Part 1")
object1 = ClassName(4, 160)  # creates an instance/object by calling the constructor __init__
object1.method1()  # calls method1 on object1
object1._protected_method()  # don't do this
print(object1)  # calls internally __repr__ on object1

print("\nPart 2")
object2 = ClassName2(12, 99)  # creates an instance of class ClassName2.  ClassName2 has own function __init__, so it uses the inherited __init__ of class ClassName
print(object2)  # calls internally __repr__ on object1
object2.method1()  # calls method1 on object2

print("\nPart 3")
objectlist = [object1, object2]
for obj in objectlist:
    obj.method1()  # calls different versions of method1(). Example for polymorphism.
