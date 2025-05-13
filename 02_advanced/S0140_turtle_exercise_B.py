"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Denne opgave findes i varianterne A og B. Spørg din lærer, hvilken variant du skal arbejde med.

Del 0:
    Funktionen demo introducerer dig til alle de kommandoer, du skal bruge
    for at interagere med Tom the Turtle i de følgende øvelser.
    Find ud af hvad funktionen gør ved at lege med funktionskoden.
    Hvad gør fx funktionerne forward(), left(), right(), done()?

Del 1:
    Skriv en funktion "circle", som accepterer en parameter "radius".
    Funktionen skal tegne en cirkel med den tilsvarende radius.

Del 2:
    Skriv en funktion "move_to", som accepterer 2 parametre x og y.
    Funktionen skal flytte skildpadden til de angivne koordinater x og y
    uden at tegne.

Del 3:
    Skriv en funktion "square", som accepterer en parameter "length".
    Når denne funktion kaldes, skal skildpadden tegne en firkant med en
    sidelængde på "længde" pixels.
    Test funktionen ved at kalde den i hovedprogrammet. (Dette gælder
    også for funktionerne i de øvrige dele af opgaven).

Del 4:
    Skriv en funktion "triangle", som accepterer en parameter "length".
    Når denne funktion kaldes, skal skildpadden tegne en ligesidet trekant
    med en sidelængde på "længde" pixels.

Del 5:
    Dupliker koden for funktionen "triangle". Omdøb den duplikerede funktion
    til "coloured_triangle". Tilføj en parameter "color", som styrer med
    hvilken farve skildpadden tegnes.

Del 6:
    Brug dine funktioner "circle" og "move_to" til at tegne 10 cirkler.
    Du bestemmer, hvor stor cirklerne er, og hvor de befinder sig.

Del 7:
    Skriv en funktion "draw_square_at", som accepterer tre parametre:
    "length", "x" og "y". Funktionen skal tegne en firkant med den givne
    sidelængde. Det øverste venstre hjørne af firkanten skal ligge på de
    angivne koordinater x, y. Brug din tidligere funktion "square".

Del 8:
    Skriv en funktion "many_squares" med en for-loop, som kalder funktionen
    "square" gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse
    i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 9:
    Lav en funktion "draw_grid", der tegner et gitter (fx 5x5 firkanter).
    Funktionen skal tage parametre for antal rækker, antalkolonner og
    firkantens størrelse.

Del 10:
    Lav en funktion draw_house, som tegner et simpelt hus bestående af en
    firkant (husets krop) og en trekant (taget). Funktionen skal tage
    parametre for størrelse og farver.

Del 11:
    Opret din egen funktion, der producerer et sejt mønster.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.

def demo():  # demonstration of basic turtle commands
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.circle(50)  # draw a circle with radius 50
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.goto(-100, -200)  # move to coordinates -100, -200  (0, 0 is the middle of the screen)
    tom.home()  # return to the original position in the middle of the window


tom = turtle.Turtle()  # create an object named tom of type Turtle
demo()
turtle.done()  # keep the turtle window open after the program is done
