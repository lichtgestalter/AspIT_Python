"""
Exercise "Number pyramid" (Solution):

Inspect this code in detail. Especially if you did not come up with a solution yourself.
Find out what every row of code does. For example by changing the code a bit and running it again.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


def pyramid2(lines, start):
    strings = start.split(" ")  # split start into a list of strings
    numbers = []  # numbers is a list and will later contain numbers
    for s in strings:
        if len(s) > 0:
            numbers.append(int(s.strip()))  # strip removes white spaces and similar characters from the beginning and end of string
    number_lists = [numbers]  # number_lists is a list and will later contain lists of numbers
    for line in range(lines):
        number_lists.append(number_lists[line].copy())  # copy the last element in number_lists and appended it to number_lists
        print("row " + str(line+1), end=": ")
        print(number_lists[line])
        index_shift = 0  # the last line keeps growing while we edit it. this variable helps us to keep track where we have to insert the next number.
        for n in range(len(number_lists[line])-1):
            if number_lists[line][n] + number_lists[line][n + 1] == line + 2:  # is the criterion for insertion of a new number met?
                number_lists[line+1].insert(n + index_shift + 1, line + 2)
                index_shift += 1


# some alternative solutions:
def pyramid2a(lines, start):
    numbers = [int(i) for i in str(start)]
    numbers2 = [i for i in numbers]
    for line in range(lines):
        print("row " + str(line+1), end=": ")
        print(numbers2)
        index_shift = 0
        for n in range(len(numbers)-1):
            if numbers[n] + numbers[n + 1] == line + 2:
                numbers2.insert(n + index_shift + 1, line + 2)
                index_shift += 1
        numbers = [i for i in numbers2]


def pyramid2b(lines, start):
    number_lists = [[int(i) for i in str(start)]]
    for line in range(lines):
        number_lists.append([i for i in number_lists[line]])
        print("row " + str(line+1), end=": ")
        print(number_lists[line])
        index_shift = 0
        for n in range(len(number_lists[line])-1):
            if number_lists[line][n] + number_lists[line][n + 1] == line + 2:
                number_lists[line+1].insert(n + index_shift + 1, line + 2)
                index_shift += 1


def pyramid2c(lines, start):
    number_lists = [[int(i) for i in str(start)]]
    for line in range(lines):
        number_lists.append(number_lists[line].copy())
        print("row " + str(line+1), end=": ")
        print(number_lists[line])
        index_shift = 0
        for n in range(len(number_lists[line])-1):
            if number_lists[line][n] + number_lists[line][n + 1] == line + 2:
                number_lists[line+1].insert(n + index_shift + 1, line + 2)
                index_shift += 1


# start_input = int(input("Enter the first row of the pyramid: "))
# lines_input = int(input("Enter the number of rows to print: "))
# pyramid2a(lines_input, start_input)
# pyramid2b(lines_input, start_input)
# pyramid2c(lines_input, start_input)

start_input = input("Enter the first row of the pyramid. (Separate the individual numbers with spaces.): ")
lines_input = int(input("Enter the number of rows to print: "))
pyramid2(lines_input, start_input)
