"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en metode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en metode ved navn wag_tail for Dog. Denne metode udskriver i konsollen noget i stil
    med "Hunden Snoopy vifter med sin 32 cm lange hale".
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father) undenfor klassen. Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google hvordan man laver det.

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

from random import choice

class Animal:

    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        gender = "Female" if self.female else "Male"
        return (f"Name: {self.name}, Sound: {self.sound}, "
                f"Height: {self.height}m, Weight: {self.weight}kg, "
                f"Legs: {self.legs}, Gender: {gender}")
    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep
    def __repr__(self):
        base_info = super().__repr__()
        sheep_hunter = "Yes" if self.hunts_sheep else "No"
        return f"{base_info}, Tail Length: {self.tail_length}cm, Hunts Sheep: {sheep_hunter}"
    def __add__(self, other):
        return mate(self, other)
    def wag_tail(self):
        print(f"Hunden Snoopy vifter med sin {self.tail_length} cm lange hale")

def mate(mother: Dog, father: Dog):
    return (
        Dog(
            choice([mother.name, father.name]),
            choice([mother.sound, father.sound]),
            (mother.height + father.height) / 2,
            (mother.weight + father.weight) / 2,
            4,
            choice([mother.female, father.female]),
            (mother.tail_length + father.tail_length) / 2,
            False,
        )
    )



cow = Animal("Cow", "moo", 1.5, 521, 4, True)

cow.make_sound()

shepherd_male = Dog("Shepherd", "Bark", 0.6, 25, 4, False, 30, True)
shepherd_female = Dog("Shepherd", "Bark", 0.4, 15, 4, True, 23, False)


shepherd_male.make_sound()
shepherd_male.wag_tail()

child = shepherd_male + shepherd_female

print(child)
