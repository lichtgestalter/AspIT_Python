"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner:
    turn = 0
    sleepiness = 0
    thirst = 0
    hunger = 0
    whisky = 0
    gold = 0

    def __repr__(self):
        return f"Turn:       {self.turn}/1000\nSleepiness: {self.sleepiness}/100\nThirst:     {self.thirst}/100\nHunger:     {self.hunger}/100\nWhisky:     {self.whisky}/10\nGold:       {self.gold}"

    def change_attributes(self, sleepines, thirst, hunger, whisky=0, gold=0):
        self.sleepiness += sleepines
        self.thirst += thirst
        self.hunger += hunger
        self.whisky += whisky
        self.gold += gold

    def sleep(self):
        self.change_attributes(-10, 1, 1)

    def mine(self):
        self.change_attributes(5, 5, 5, 0, 5)

    def eat(self):
        self.change_attributes(5, -5, -20, 0, -2)

    def buy_whisky(self):
        self.change_attributes(5, 1, 1, 1, -1)

    def drink(self):
        self.change_attributes(5, -15, -1, -1)

    def dead(self):
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100

    def attributes(self):
        if self.sleepiness < 0:
            self.sleepiness = 0
        if self.thirst < 0:
            self.thirst = 0
        if self.hunger < 0:
            self.hunger = 0
        if self.whisky > 10:
            self.whisky = 10

    def each_turn(self, func):
        while not self.dead() and self.turn < 1000:
            self.turn += 1
            func()
            self.attributes()


morris = Miner()


@morris.each_turn
def turn():
    if morris.sleepiness > 90:
        morris.sleep()
    elif morris.hunger > 90:
        morris.eat()
    elif morris.thirst > 90:
        if morris.whisky == 0:
            morris.buy_whisky()
        else:
            morris.drink()
    else:
        morris.mine()


print(morris)
