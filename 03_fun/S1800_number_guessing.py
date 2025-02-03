""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

from random import randint

number = list(map(int, str(randint(1000, 9999))))
guess = []
guesses = 0

while guess != number:
    guess = list(map(int, input("Guess a number ")))
    guesses += 1

    black_coin = 0
    white_coin = 0

    for i in range(len(guess)):
        if number[i] == guess[i]:
            black_coin += 1
        elif number.count(guess[i]) >= 1:
            white_coin += 1

    print(f"sorte mønter: {black_coin}")
    print(f"hvide mønter: {white_coin}")


print(f"du gættede rigtet på {guesses} forsøg")


