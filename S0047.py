# define a function that prints a car's motor sound (for example "roooaar")
# define another function that prints an electric car's motor sound
# in the main program, define variables which represent the number of wheels and the maximum speed of 2 different cars
# print out the properties of both cars
# then call both motors sound functions

# run the program with shift+f10 (or click on the green arrow)

def drive_car():
    print("WROOOOOOOOM!")


def drive_electric_car():
    print("ssssssss")


car1_wheels = 4  # define number of wheels for car1
car1_maxspeed = 160  # define maximum speed for car1
car2_wheels = 8  # define number of wheels for car2
car2_maxspeed = 100  # define maximum speed for car2

print("wheels", car1_wheels, "maximum speed", car1_maxspeed)  # print out the properties of car1
print("wheels", car2_wheels, "maximum speed", car2_maxspeed)  # print out the properties of car2

drive_car()
drive_electric_car()
