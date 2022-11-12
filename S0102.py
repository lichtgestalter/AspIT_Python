"""
Exercise "The inventory sequence" (solution)

Inspect this code in detail. Especially if you did not come up with a solution yourself.
Find out what every row of code does. For example by changing the code a bit.
Then send this Teams message to your teacher: I am done with exercise "cars" (in a language of your choice) :-)
thereafter go on with the next file in numerical order in the teacher's exercise repository after the current exercise.
"""


def count_number(number):
    counter = 0
    for row_ in rows:
        counter += row_.count_number(number)
    return counter


def inventory(max_row):
    for row_number in range(max_row):
        row = []
        rows.append(row)
        column = 0
        frequency = count_number(column)
        while frequency > 0:
            row.append(frequency)
            column += 1
            frequency = count_number(column)
        row.append(0)
        print(row)


rows = []
inventory(6)
