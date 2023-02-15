"""
Exercise "The inventory sequence" (solution)

Find out what every row of code does. For example by changing the code a bit and running it again.

Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


def count_number(number):
    counter = 0
    for row in rows:
        counter += row.count(number)
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
inventory(16)
