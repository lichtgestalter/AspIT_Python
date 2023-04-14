"""
Indkapsling:

Nogle gange ønsker vi at holde attributter eller metoder private for en klasse.
Det betyder, at disse attributter eller metoder kun kan bruges af den klasse, der ejer dem.
I python er en privat attribut eller metode markeret med en ledende enkelt understregning (_).
I python er det teknisk set muligt at kalde private metoder fra uden for deres klasse, men det anses for uklogt.
Private medlemmer kaldes også for beskyttede medlemmer.

Undersøg følgende kode i detaljer. Find ud af, hvad hver række kode gør.
F.eks. ved at ændre koden en smule og derefter køre/debugging af programmet.

Læs mere om objektorienteret programmering her:
https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

Send derefter denne Teams-meddelelse til din lærer: <filename> done

Derefter går du videre med den næste fil."""


class Vehicle:
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed

    def __repr__(self):
        return f"Vehicle: {self.wheels} wheels, {self.max_speed} km/h maximum speed"

    def drive(self):
        print("WROOOOOOOOM!")
        self._top_secret()  # this is ok

    def _top_secret(self):
        print("Don't call this method from outside this class!")


car1 = Vehicle(4, 160)
car1.drive()
car1._top_secret()  # this is NOT ok!

