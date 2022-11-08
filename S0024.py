# Exercise "Number pyramid" (Solution):

# Inspect this code in detail. Especially if you did not come up with a solution yourself.
# Find out what every line of code does. For example by changing the code a bit.
# Then send this Teams message to your teacher: i am done with exercise "Number pyramid" (in a language of your choice) :-)
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
