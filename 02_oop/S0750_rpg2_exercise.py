"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

from random import choice, random

from six import print_


class Character:
    def __init__(self, name, max_health, attackpower):
        self.poisoned = 0
        self.name = name
        self.max_health = max_health
        self._current_health = max_health
        self.attackpower = attackpower

    def __repr__(self):
        return f"name: {self.name}, current_health: {self._current_health}/{self.max_health}, attackpower: {self.attackpower}"

    def hit(self, character):
        character.get_hit(self)

    def get_hit(self, character):
        self._current_health -= character.attackpower

    def get_healed(self, character):
        self._current_health += character.healpower

    def get_poisoned(self, character):
        self.poisoned += character.attackpower

    def dead(self):
        return self._current_health <= 0

    def turn(self):
        self._current_health -= self.poisoned
        if self.poisoned > 0:
            self.poisoned -= 1


class Healer(Character):
    def __init__(self, name, max_health, healpower):
        super().__init__(name, max_health, 0)
        self.healpower = healpower

    def __repr__(self):
        return f"{super().__repr__()[:-16]}, healpower: {self.healpower}"

    def heal(self, character):
        character.get_healed(self)


class Magician(Character):
    def poison(self, character):
        character.get_poisoned(self)

class Hunter(Character):

    def __init__(self, name, max_health, attackpower, hit_chance):
        super().__init__(name, max_health, attackpower)
        self.hit_chance = hit_chance

    def hit(self, character):
        if random() < self.hit_chance:
            character.get_hit(self)


class Game:
    def __init__(self, characters):
        self.loser = None
        self.characters = characters

    def print_game(self):

        for character in self.characters:
            print(character)

        print()

    def random_character(self, character=None):
        characters = list(self.characters)
        if character is not None:
            characters.remove(character)
        return choice(characters)

    def dead(self):
        for character in self.characters:
            if character.dead():
                return character.name
        return False

    def turn(self, func):
        while not self.dead():
            for character in self.characters:
                character.turn()
            func()
        self.loser = self.dead()


lost = {}

for match in range(100):
    hero1 = Character("hero 1", 1000, 10)
    hero2 = Character("hero 2", 500, 20)

    magician1 = Magician("magician 1", 600, 5)
    magician2 = Magician("magician 2", 400, 10)

    hunter1 = Hunter("hunter 1", 500, 50, 0.5)

    healer1 = Healer("healer 1", 500, 50)

    game = Game([hero1, hero2, magician1, magician2, hunter1, healer1])

    @game.turn
    def turn():
        hero1.hit(game.random_character(hero1))
        hero2.hit(game.random_character(hero2))
        magician1.poison(game.random_character(magician1))
        magician2.poison(game.random_character(magician2))
        hunter1.hit(game.random_character(hunter1))
        healer1.heal(game.random_character())


    if game.loser in lost:
        lost[game.loser] += 1
    else:
        lost[game.loser] = 1
lost = dict(sorted(lost.items()))

for x in lost:
    print(f"{x}: {lost[x]}")

