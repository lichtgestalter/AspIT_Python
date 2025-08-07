""" Opgave "The inventory sequence" (løsning)

Inspicer følgende kode i detaljer. Især hvis du ikke selv har fundet på en løsning.
Find ud af, hvad hver række kode gør. F.eks. ved at ændre koden en smule og derefter2
køre/debugge programmet.

Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


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
