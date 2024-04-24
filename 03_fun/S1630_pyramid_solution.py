"""Opgave "Number pyramid" (løsning):

Inspicer følgende kode i detaljer. Især hvis du ikke selv har fundet på en løsning.
Find ud af, hvad hver række kode gør. Fx ved at ændre koden en smule og derefter
køre/debugge programmet.

Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


def pyramid2a(lines, firstline):
    strings = firstline.split(" ")  # split firstline into a list of strings
    numbers = []  # numbers is a list and will later contain numbers
    for s in strings:
        if len(s) > 0:
            numbers.append(int(s.strip()))  # strip removes white spaces and similar characters from the beginning and end of string
    number_lists = [numbers]  # number_lists is a list and will later contain lists of numbers
    for line in range(lines):
        number_lists.append(number_lists[line].copy())  # copy the last element in number_lists and append it to number_lists
        print("row " + str(line+1), end=": ")
        print(number_lists[line])
        index_shift = 0  # the last line keeps growing while we edit it. this variable helps us to keep track where we have to insert the next number.
        for n in range(len(number_lists[line])-1):
            if number_lists[line][n] + number_lists[line][n + 1] == line + 2:  # is the criterion for insertion of a new number met?
                number_lists[line+1].insert(n + index_shift + 1, line + 2)
                index_shift += 1


def pyramid2b(lines, firstline):
    """
    This version is much more elegant, but uses the advanced concept
    "list comprehension" and the function "zip".
    """
    current_line = [int(i) for i in str(firstline)]  # list of integers. Input must not contain blanks!
    next_line = []  # we build the next line of the pyramid in this variable
    for line_number in range(2, lines + 1):
        for left, right in zip(current_line[:-1], current_line[1:]):  # 2 for loops run parallel now: left iterates through current_line[:-1] and right iterates through current_line[1:]
            next_line.append(left)
            if left + right == line_number:
                next_line.append(line_number)
        next_line.append(current_line[-1])  # add the last element of current_line
        print(f"row {line_number}: {next_line}")
        current_line = next_line
        next_line = []


firstline_input = input("Enter the first row of the pyramid. (Just type some integers. Use blanks to separate the numbers): ")
lines_input = int(input("Enter the number of rows to print: "))
pyramid2a(lines_input, firstline_input)

firstline_input = input("Enter the first row of the pyramid. (Just type some integers. This time, DO NOT use blanks or something else to separate the numbers): ")
lines_input = int(input("Enter the number of rows to print: "))
pyramid2b(lines_input, firstline_input)
