"""
Opgave "Animals"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

All you need to know in order to solve this exercise, you'll find in the cars_oop- and rpg1-files.

Define a class named Animal.
Each object of this class shall have the attributes name, sound, height, weight, legs, female.
Name and sound are strings. Height and weight are floating point numbers. Legs is a integer. Female is boolean.

Add to the class meaningful methods __init__ and __repr__.
Call these methods to create objects of the class Animal and to print them out in the main program.

Write a class method named make_noise, which prints out the animal's sound in the console.
Call this method in the main program.

Define another class Dog, which inherits from Animal.
Each object of this class shall have the attributes tail_length and hunts_sheep.
Tail_length is a floating point number. Hunts_sheep is boolean.

Add to the class meaningful methods __init__ and __repr__.
In writing the constructor of Dog, try to reuse code from the class Animal.
Call these methods to create objects of the class Dog and to print them out in the main program.

Call the method make_noise on Dog objects in the main program.

Write a class method named wag_tail for Dog.
This method prints out into the console something like
"The dog Snoopy wags its 32cm long tail"
Call this method in the main program.

Write a function mate(mother, father). Both parameters are of type Dog.
This function shall return a new object of type Dog.
In this function, make meaningful rules for the new dogs attributes.
Make sure that this function only accepts dogs with the correct sex as arguments.

In the main program, call this method and print out the new dog.


Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop- og rpg1-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne navn, lyd, højde, vægt, ben, hunner.
Navn og lyd er strenge. Højde og vægt er flydende tal. Ben er et heltal. Hun er en boolean.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Hund, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length og hunts_sheep.
Tail_length er et flydende tal. Hunts_sheep er en boolean.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktøren for hund skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mor, far). Begge parametre er af typen Hund.
Denne funktion skal returnere et nyt objekt af typen Hund.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

