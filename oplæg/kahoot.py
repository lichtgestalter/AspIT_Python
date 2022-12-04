# for i in range(3):
#     i
#
# for i in range(1, 30, 3):
#     print(i)
#
# print()
#
#
# for i in range(1, 30, 3):
#     if i % 5 == 0:
#         print(i)
#
# print()
#
# for i in range(30):
#     if i % 7 == 0:
#         print(i)
#
# print("x")
#
# for i in range(2, 6, -1):
#     print(i)
#

# x = 64.7
# print(f'{x=}  {type(x)=}')
#
# print("-----")
#
# x = 64.7
# x = int(x)
# print(f'{x=}  {type(x)=}')
#
# print("-----")
#
# x = 64.7
# x = str(x)
# print(f'{x=}  {type(x)=}')

# a = 3
# b = 7
# c = 2
# print((a+b)*c)
#
# print("-----")
#
# a = 3
# b = 7
# c = 2
# print(a+b*c)
#
# print("-----")
#
# x = 13
# y = 5
# print(f'{x / y =}   {x // y =}    {x % y =}')
#
# print("-----")
#
# x = 2
# y = 5
# print(f'{x ** y =}   {type(x ** y) =}')
#
#
# numbers = [8, 12, 3]
# for number in numbers:
#     print(number)
#
#
# print("-----")
#
# print(3>1)
#
# print("-----")
#
# print(type(3>1))
#
# print("-----")
#
# print(3==1)
#
# print("-----")
#
# print(3!=1)
#
# print("-----")
#
# print(3==1 or 5>0)
#
# print("-----")
#
# print(3!=1 and 4>2)
#
# print("-----")
#
# print(not 2<7)
#
# print("-----")
#
# print(not (2<7 or 4>=1))
#
# print("-----")
#
# print(not False)
#
# print("-----")
#
# dark = True
# if dark==True:
#     print("Night!")
#
# print("-----")
#
# dark = True
# if dark:
#     print("Night!")
#
# print("-----")
#
# dark = False
# if dark:
#     print("Night!")
#
# print("-----")
#
# dark = False
# if dark:
#     print("Night!")
# else:
#     print("Day!")
#
#
# print("-----")
#
# dark = not False
# if dark:
#     print("Night!")
# else:
#     print("Day!")
#
# print("-----")
#
# def animal(name):
#     return name in ["cat", "dog", "pig"]
#
# print(animal("mouse"))
#
# print("-----")
#
# def animal(name):
#     return name in ["cat", "dog", "pig"]
#
# print(animal("mouse") or animal("cat"))
#
# print("-----")
#
# def animal(name):
#     return name in ["cat", "dog", "pig"]
#
# if animal("dog"):
#     print("known animal")
# else:
#     print("unknown name")
#
# print("-----")
# print()
#
# print("-----")
# print()
#
# print("-----")
#
# print()
#
# print("-----")
#
# print()
#
# print("-----")
#
# print("-----")



class Vehicle:
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed

    def __repr__(self):
        return f"Vehicle: {self.wheels=} {self.max_speed=}"

    def drive(self):
        print("WROOOOOOOOM!")
        self._top_secret()

    def _top_secret(self):
        print("Don't call this method from outside this class!")


car1 = Vehicle(4, 160)
car1.drive()
car1._top_secret()
print(car1)


"""
attribute
method
member
protected/private member
class
inheritance
"""
