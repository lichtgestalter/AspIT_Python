"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.
Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""
from pyfiglet import figlet_format


def change_attributes(player, sleepiness, thirst, hunger, whisky=0, gold=0):
    player["sleepiness"] += sleepiness
    player["thirst"] += thirst
    player["hunger"] += hunger
    player["whisky"] += whisky
    player["gold"] += gold


def sleep(player):
    change_attributes(player, -10, 1, 1)


def mine(player):
    change_attributes(player, 5, 5, 5, 0, 5)


def eat(player):
    change_attributes(player, 5, -5, -20, 0, -2)


def buy_whisky(player):
    change_attributes(player, 5, 1, 1, 1, -1)


def drink(player):
    change_attributes(player, 5, -15, -1, -1)


def dead(player):
    return player["sleepiness"] > 100 or player["thirst"] > 100 or player["hunger"] > 100


def attributes(player):
    for attribute in player:
        if player[attribute] < 0:
            player[attribute] = 0
    if player["whisky"] > 10:
        player["whisky"] = 10


def main():
    morris = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary
    turns = 1000

    while not dead(morris) and morris["turn"] < turns:
        morris["turn"] += 1
        if morris["sleepiness"] > 90:
            sleep(morris)
        elif morris["hunger"] > 90:
            eat(morris)
        elif morris["thirst"] > 90:
            if morris["whisky"] == 0:
                buy_whisky(morris)
            else:
                drink(morris)
        else:
            mine(morris)

        attributes(morris)
        print(morris)

    if dead(morris):
        print(figlet_format("Morris died", font="banner3"))
    else:
        print(figlet_format(f"Morris survived and earned {morris['gold']} gold", font="bulbhead", width=150))


if __name__ == '__main__':
    main()
