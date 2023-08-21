"""
Opgave "print_pattern":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide om funktioner for at løse denne øvelse, finder du i jupiter-notesbogen S0040_basics.ipynb

Skriv en funktion med navnet "print_repeatedly".
Rul ned for at finde det sted i denne fil, hvor du skal skrive funktionen ind.

Funktionen print_repeatedly skal ...
    have 2 parametre ved navn "string" og "repetitions".
    udskrive parameteren "string" "repetitions" gange
Eksempel: print_repeatedly("xy", 3) udskriver "xyxyxyxy"
Tip: brug end="" som anden parameter i print() for at undgå at få udskrevet hver string i en ny linje. Mere om det: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/ .

Skriv en anden funktion med navnet "print_pattern".
Funktionen print_pattern skal ...
    have 2 parametre ved navn "string" og "repetition_list". "repetition_list" er en liste over integer tal.
    kald funktionen print_repeatedly() flere gange med hvert medlem af "repetition_list" som anden parameter. Den første parameter er altid "string".

Eksempel:
    print_pattern("xy", [3, 2, 4]) kalder print_repeatedly("xy", 3), print_repeatedly("xy", 2) og print_repeatedly("xy", 4)
    Dette resulterer i følgende udskrift:
        xyxyxy
        xyxy
        xyxyxyxy

I hovedprogrammet...
    Skriv en kodelinje, der kalder print_pattern() med argumenterne "abc" og [4, 2, 1].

Kør programmet.
I konsollen skal der udskrives:
    abcabcabcabc
    abcabc
    abc

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

#  Write your functions below this line.


# Here starts the main program. From the main program you can call your functions.
