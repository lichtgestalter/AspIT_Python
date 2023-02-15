"""
Exercise "print_pattern":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

All you need to know about functions in order to solve this exercise, you'll find in the jupiter notebook S0040_basics.ipynb.

Write a function named "print_repeatedly".
Scroll down to find the place in this file, where to write the function in.

The function print_repeatedly shall ...
    have 2 parameters named "string" and "repetitions".
    print the parameter "string" "repetitions" times
        Tip: use end="" as a second parameter of print() to avoid getting printed every string in a new line. See also https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/ .
Example: print_repeatedly("xy", 3) prints out "xyxyxy"

Write another function named "print_pattern".
The function print_pattern shall ...
    have 2 parameters named "string" and "repetition_list". "repetition_list" is a list of integer numbers.
    call the function print_repeatedly() several times using every member of "repetition_list" as its second parameter. The first parameter is always "string".
Example:
    print_pattern("xy", [3, 2, 4])  calls print_repeatedly("xy", 3), print_repeatedly("xy", 2)  and print_repeatedly("xy", 4)
    This results in the following print out:
        xyxyxy
        xyxy
        xyxyxyxy

In the main program...
    Write a line of code calling print_pattern() with the arguments "abc" and [4, 2, 1].

Run the program.
In the console should be printed:
    abcabcabcabc
    abcabc
    abc

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

#  Write your functions below this line.


# Here starts the main program. From the main program you can call your functions.
