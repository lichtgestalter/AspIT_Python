# Exercise "Number pyramid" (Solution):

# Copy this file into your own solution directory. Write your solution into the copy.

# watch the first 93 seconds of this video: https://www.youtube.com/watch?v=NsjsLwYRW8o

# write a function "pyramid" which produces the numbers shown in the video
# the function accepts a parameter defining how many number lines to produce
# the function prints out the numbers of each line and also their sum

# in the main program, call the function with 1, 2, 3, ..., 10 as an argument.

# run the program with shift+f10 (or click on the green arrow)

# add a more general function pyramid2
# this function accepts as a second parameter a list with the numbers of
# the pyramid's topmost line

# in the main program, call pyramid2 with 1, 2, 3, ..., 10 as the first argument
# and a list of numbers of your choice as the second argument.
# try out different lists as the second argument.

# run the program with shift+f10 (or click on the green arrow)

# if you have no idea how to begin, open S0021.py and start from there

# when your program is complete, push it to your github repository
# then send this Teams message to your teacher: i am done with exercise "Number pyramid" (in a language of your choice) :-)
# thereafter go on with the next file in numerical order in the teacher's exercise repository after the current exercise.


def pyramid2_uli(lines, start):
    numbers = [int(i) for i in str(start)]
    numbers2 = [i for i in numbers]
    for line in range(lines):
        print("line " + str(line+1), end=": ")
        print(numbers2)
        index_shift = 0
        for n in range(len(numbers)-1):
            if numbers[n] + numbers[n + 1] == line + 2:
                numbers2.insert(n + index_shift + 1, line + 2)
                index_shift += 1
        numbers = [i for i in numbers2]


startInput = int(input("Enter the numbers to start the pyramid sequence: "))
linesInput = int(input("Enter the number of lines to print: "))
pyramid2_uli(linesInput, startInput)
