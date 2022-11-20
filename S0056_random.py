"""
Random numbers:

Inspect this code in detail.
Find out what every row of code does. For example by changing the code a bit and running it again.
Thereafter go on with the next file.
"""

import random  # this imports a library called "random". A library is (someone else's) python code, that you can use in your own program.

for i in range(3):
    print(f"A random number between 0 and 1: {random.random()}")
print()

minimum = 2
maximum = 4
for i in range(5):
    print(f"A random integer number between {minimum} and {maximum}: {random.randint(minimum, maximum)}")  #
print()

first_seed = 5
random.seed(first_seed)  # use seed() to create reproducible random numbers
for i in range(3):
    print(f"A random number between 0 and 1 with seed {first_seed}: {random.random()}")
print()

second_seed = 7  # another seed
random.seed(second_seed)
for i in range(3):
    print(f"A random number between 0 and 1 with seed {second_seed}: {random.random()}")
print()

random.seed(first_seed)  # same seed from before
for i in range(3):
    print(f"A random number between 0 and 1 with seed {first_seed}: {random.random()}")  # using the first seed again still creates the same random numbers
print()

max_number = 8
for i in range(3):
    print(f"A random number between 0 and {max_number}: {random.random()*max_number}")
