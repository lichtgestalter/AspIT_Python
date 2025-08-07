"""Inspicer følgende kode i detaljer. Især hvis du ikke selv har fundet på en løsning.
Find ud af, hvad hver række kode gør. F.eks. ved at ændre koden en smule og derefter
køre/debugge programmet.

Så send denne Teams-besked til din lærer: Jeg er færdig med opgave "rollespil 1"
Derefter går du videre med den næste fil."""


class Character:

    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attackpower = attackpower

    def __repr__(self):
        return f"Character: {self.name=:11}   {self.max_health=:4}     {self._current_health=:4}     {self.attackpower=:3}"

    def hit(self, other):
        print("\n", self.name, "hits", other.name, "for", self.attackpower, "damage", "\n")
        other.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        self._current_health -= attackpower

    def get_healed(self, healpower):
        self._current_health += healpower


class Healer(Character):
    
    def __init__(self, name, health, healpower):
        super().__init__(name, health, 0)
        self.healpower = healpower

    def heal(self, other):
        print("\n", self.name, "heals", other.name, "for", self.healpower, "damage", "\n")
        other.get_healed(self.healpower)


hero1 = Character("Bozeto", 100, 20)
hero2 = Character("Andananda", 110, 24)
hero3 = Healer("DoctorX", 75, 15)
print(hero1)
print(hero2)
print(hero3)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)

















