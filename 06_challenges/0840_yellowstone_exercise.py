"""Opgave "Yellowstone"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.


Skriv en funktion som beregner Yellowstone-følgen. For at nå det, løs de følgende delopgaver:

Del 1:
    Se de første 4 minutter og 16 sekunder af denne video:
    https://www.youtube.com/watch?v=DUaqiM1bGX4

    Hvis du hellere vil have reglerne på skrift:
    Definer en række positive heltal ved hjælp af reglerne, at
        a(1) = 1, a(2) = 2, a(3) = 3,
        og for n ≥ 4 er a(n) det mindste tal, der ikke allerede er i rækken,
        som har en fælles faktor med a(n - 2), men som er relativt primtal i forhold til a(n - 1).
Del 2:
    Skriv en funktion prime_list(n), der returnerer de første n primtal som en list.

Del 3:
    Skriv en funktion prime_factorization(number), der returnerer
    en list over primfaktorerne for number.

    Prime factorization eller integer factorization af et tal er at nedbryde et
    tal til et sæt af primtal, som ganges sammen for at resultere i det oprindelige tal.
    Dette er også kendt som prime decomposition.
    Eksempel: 2, 2, 5 er primfaktoriseringen af 20.

Del 4:
    Skriv en funktion greatest_common_divisor(number1, number2), der returnerer den største fælles divisor for de to tal.
    Eksempel: Den største fælles divisor for 20 og 70 er 10 (fordi 20 og 70 har de fælles primfaktorer 2 og 5).

Del 5:
    Skriv en funktion relative_prime(number1, number2), der returnerer True, hvis de to tal er relative primtal
    til hinanden, ellers False.
    Relativt primtal betyder, at den største fælles divisor for de to tal er 1.

Del 6:
    Skriv en funktion yellowstone(n), der returnerer de første n elementer af Yellowstone-følgen som en list.
    Brug denne liste til at kontrollere din løsning: https://oeis.org/A098550/b098550.txt

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
