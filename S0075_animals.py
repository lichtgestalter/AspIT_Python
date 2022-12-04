"""
Exercise "Animals"

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

All you need to know in order to solve this exercise, you'll find in the cars_oop- and rpg1-files.

Define a class named Animal.
Each object of this class shall have the attributes name, sound, height, weight, legs, female.
Name and sound are strings. Height and weight are floating point numbers. Legs is a integer. Female is boolean.

Add to the class meaningful methods __init__ and __repr__.
Call these methods to create objects of the class Animal and to print them out in the main program.

Write a class method named make_noise, which prints out the animal's sound in the console.
Call this method in the main program.

Define another class Dog, which inherits from Animal.
Each object of this class shall have the attributes tail_length and hunts_sheep.
Tail_length is a floating point number. Hunts_sheep is boolean.

Add to the class meaningful methods __init__ and __repr__.
In writing the constructor of Dog, try to reuse code from the class Animal.
Call these methods to create objects of the class Dog and to print them out in the main program.

Call the method make_noise on Dog objects in the main program.

Write a class method named wag_tail for Dog.
This method prints out into the console something like
"The dog Snoopy wags its 32cm long tail"
Call this method in the main program.

Write a function mate(mother, father). Both parameters are of type Dog.
This function shall return a new object of type Dog.
In this function, make meaningful rules for the new dogs attributes.
Make sure that this function only accepts dogs with the correct sex as arguments.

In the main program, call this method and print out the new dog.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

