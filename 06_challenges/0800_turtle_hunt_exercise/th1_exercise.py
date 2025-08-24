"""Opgave "Turtle Hunt":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

-------

Spillet:
    Denne øvelse er et spil for 2 spillere.
    3 skildpadder (jægere) forsøger at fange en anden skildpadde (bytte) så hurtigt som muligt.
    Den ene spiller styrer byttet, den anden spiller styrer jægerne. Derefter bytter spillerne roller.
    I hver tur bestemmer spillerne, hvor mange grader deres skildpadde(r) roterer. Dette er spillerens eneste opgave.
    Byttet får et point for hver tur, før det bliver fanget.
    Hvis byttet stadig er på flugt efter MAX_TURNS omgange, fordobles pointene, og jagten slutter.


Koden til spillet er allerede skrevet i th2_main.py og th3_service.py. Du må ikke ændre disse filer.

Din opgave er at få skildpadderne til at rotere smartere.

Kopier alle 4 turtle_hunt-filer til din egen løsningsmappe.
Skriv din løsning ind i din kopi af th4_classes_constants.py.

Filstruktur:
    Koden er opdelt i 3 filer for at gøre det klart, hvilken del af koden
    du skal ændre, og hvilken del af koden du skal lade være uændret.

    th2_main.py:
        Dette er hovedprogrammet.
        Du må ikke foretage ændringer heri.
        Kør det for at starte spillet.

    th3_service.py:
        Indeholder nogle servicefunktioner, som vil være nyttige for dig.
        Du må ikke foretage ændringer heri.

    th4_classes_constants.py:
        Alt din programmering til denne øvelse foregår i denne fil.

Delopgaver:
Trin 1:
    Kig på programkoden.
    Du behøver ikke at forstå alle detaljer i hovedprogrammet.
    Find ud af, hvordan de tre filer importerer hinandens kode med "import".
    Find ud af, hvornår og hvordan metoderne rotate_prey() og rotate_hunt() bruges.

Trin 2:
    Ændr navnet på klassen PlayerName1 i den første linje i dens klassedefinition til dit personlige klasses navn.
    Nederst i denne fil skal du sætte variablerne class1 og class2 til dit personlige klasses navn.

Trin 3:
    I din personlige klasse skal du gøre metoderne rotate_prey og rotate_hunter smartere.
    Eventuelt vil du også tilføje nogle attributter og/eller metoder til din klasse.
    Du må dog ikke manipulere (f.eks. flytte) skildpadderne med din kode.
    Køretiden for dine metoder rotate_prey og rotate_hunter skal være mindre end 0,1 sekunder pr. iteration.

Trin 4:
    Find en sparringspartner i din studiegruppe.
    Som med alt andet skal du bede din lærer om hjælp, hvis det er nødvendigt.
    I din kode skal du erstatte hele klassen PlayerName2 med din sparringspartners klasse.
    Nederst i denne fil indstiller du variablen class2 til din sparringpartners klasses navn.
    Lad de 2 klasser kæmpe og lær af resultaterne for at forbedre din kode.
    Gentag dette trin indtil du er tilfreds :-)

Trin 5:
    Når dit program er færdigt, skal du skubbe det til dit github-repository.
    Send derefter denne Teams-besked til din lærer: <filename> done
    Derefter fortsætter du med den næste fil.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for skildpaddegrafikken:
    https://docs.python.org/3.3/library/turtle.html

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository."""

