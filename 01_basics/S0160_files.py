"""
Skrivning til og læsning fra en fil

Undersøg denne kode i detaljer.
Find ud af, hvad hver kodelinje gør. Fx ved at ændre koden en smule og køre den igen.
Fortsæt herefter med den næste fil.
"""

mydata = ["Hi,\n", "this is a text file.\n", "It has 3 rows.\n", "test"]  # this is a list of strings
myfile = "S0161_input.txt"  # the name of the file.

# Writing to a file
with open(myfile, "w") as file:  # 'w' stands for "write"
    file.writelines(mydata)  # writes the whole list of strings at once

# Reading from a file (method 1)
with open(myfile) as file:  # when the program exits the with-block, the file is automatically closed
    lines = file.readlines()  # reads the whole file at once
line_number = 0
for line in lines:
    line_number += 1
    print(f"Line {line_number}: {line.strip()}")  # .strip cleans the beginning and end of a string from spaces, carriage returns and similar characters
print()


# Reading from a file (method 2)
line_number = 0
with open(myfile) as file:
    for line in file:  # reads one line at a time
        line_number += 1
        print(f"Line {line_number}: {line.strip()}")
    print()
