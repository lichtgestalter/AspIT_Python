# define a function that prints a car's motor sound (for example "roooaar")

# in the main program:
# define variables which represent the number of wheels and the maximum speed of 2 different cars
# print out these properties of both cars
# then call the motor sound function

# run the program with shift+f10 (or click on the green arrow)

def drive_car():
    print("WROOOOOOOOM!")


car1_wheels = 4  # define number of wheels for car1
car1_maxspeed = 160  # define maximum speed for car1
car2_wheels = 8  # define number of wheels for car2
car2_maxspeed = 100  # define maximum speed for car2

print("wheels", car1_wheels, "maximum speed", car1_maxspeed)  # print out the properties of car1
print("wheels", car2_wheels, "maximum speed", car2_maxspeed)  # print out the properties of car2

drive_car()
