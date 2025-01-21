"""
Opgave "Cars":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen drive_car()

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne S0420_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du stadig er gået i stå, skal du åbne S0430_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Team-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


def drive_car():
    print("roooaar")


car1_wheels = 4
car1_maxspeed = 300
car2_wheels = 6
car2_maxspeed = 280

print("Car 1:")
print(f"    Wheels:     {car1_wheels}")
print(f"    Max speed:  {car1_maxspeed}\n")
print("Car 2:")
print(f"    Wheels:     {car2_wheels}")
print(f"    Max speed:  {car2_maxspeed}")

drive_car()