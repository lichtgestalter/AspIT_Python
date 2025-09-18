# Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

------------

### 0. Opret fil
- Opret en ny fil med navnet 0610_animals_exercise.py i din egen 
  løsningsmappe.
- Skriv din løsning ind i denne fil.

### 1. Klasse Animal
- Definer en klasse ved navn Animal.
- Hvert objekt i denne klasse skal have attributterne (I parentes står data typerne, dette attributterne typisk har.)
  - name (str)
  - sound (str)
  - height (float)
  - weight (float)
  - legs (int)
  - female (bool).

### 2: `__init__` og `__repr__`
- Tilføj til klassen meningsfulde metoder `__init__` og `__repr__`.
- Kald disse metoder for at 
  - oprette objekter af klassen Animal og for at
  - udskrive dem i hovedprogrammet.

### 3: make_noise
- Skriv en metode ved navn make_noise, som udskriver dyrets lyd i konsollen.
- Kald denne metode i hovedprogrammet.

### 4: Klasse Dog
- Definer en anden klasse Dog, som arver fra Animal.
- Hvert objekt af denne klasse skal have ekstra attributterne 
  - tail_length (int eller float) og 
  - hunts_sheep (typisk bool)

### 5: `__init__` og `__repr__`
- Tilføj til klassen meningsfulde metoder `__init__` og `__repr__`.
- Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra 
  klassen Animal.
- Kald disse metoder for at 
  - oprette objekter af klassen Hund og for at 
  - udskrive dem i hovedprogrammet.

### 6: make_noise
- Kald metoden make_noise på Dog-objekter i hovedprogrammet.

### 7: wag_tail
- Skriv en metode ved navn wag_tail for Dog. 
- Denne metode udskriver i konsollen noget i stil med "Hunden Snoopy vifter 
  med sin 32 cm lange hale".
- Kald denne metode i hovedprogrammet.

### 8: mate
- Skriv en funktion mate(mother, father) undenfor klassen. 
- Begge parametre er af typen Dog.
- Denne funktion skal returnere et nyt objekt af typen Dog.
- I denne funktion skal du lave meningsfulde regler for den nye hunds 
  attributter.
- Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
- Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som 
  argumenter.
- I hovedprogrammet kalder du denne metode og udskriver den nye hund.

### 9: Plus tegn
- Gør det muligt at skrive `puppy = daisy + brutus` i stedet for `puppy = mate(daisy, brutus)`
for at opnå den samme effekt.  
- Du bliver nok nødt til at google hvordan man laver det.

-----------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.