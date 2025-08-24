"""
Opgave "spell_backwards":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Forandre koden i funktionen spell_backwards() sådan at den gør hvad der står i dens dokumentation.

Brug koden i funktion spell() som inspiration.
Leg med koden i funktion spell() for at finde ud af, hvad præcis den gør.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


def spell(text):
    for letter in text:
        print(letter, end=".")
    print()


def spell_backwards(text):
    """Spells/prints text backwards"""
    0


spell("Test")
spell_backwards("Hello world")  # should print "dlrow olleH"