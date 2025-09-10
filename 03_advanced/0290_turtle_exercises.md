# Opgave "Tom the Turtle":

- De forskellige opgaver varierer meget i sværhedsgrad. 
- Du behøver ikke nødvendigvis at løse alle opgaver. 
- Hvis du er i tvivl, så spørg din lærer.
- Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder 
at løse opgaven.
- Kopier denne fil og eksempelkoden `0292_turtle_example.py` til din egen 
  løsningsmappe. 
- Skriv din løsning ind i din kopie af `0292_turtle_example.py`.
- Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.
- Når dit program er færdigt, skal du skubbe det til dit github-repository.
- Fortsæt derefter med den næste fil.
- Kun hvis du er nysgerrig og elsker detaljer:
Her er den [fulde dokumentation for turtle graphics](https://docs.python.org/3.3/library/turtle.html).

-------

### 0. Demo
- Kig på eksempelkoden `0292_turtle_example.py`.
- Funktionen demo introducerer dig til alle de kommandoer, du skal bruge
for at interagere med Tom the Turtle i de følgende øvelser.  
- Find ud af hvad funktionen gør ved at lege med funktionskoden.  
- Hvad gør fx funktionerne `forward()`, `left()`, `right()`, `done()`?

### 1. Circle
- Skriv en funktion `circle`, som accepterer en parameter `radius`.
- Funktionen skal tegne en cirkel med den tilsvarende radius.
- Test funktionen ved at kalde den i hovedprogrammet. (Dette gælder
også for funktionerne i de øvrige dele af opgaven).

### 2. Move To
- Skriv en funktion `move_to`, som accepterer 2 parametre `x` og `y`.
- Funktionen skal flytte skildpadden til de angivne koordinater `x` og `y`
uden at tegne.

### 3. Square
- Skriv en funktion `square`, som accepterer en parameter `length`.
- Når denne funktion kaldes, skal skildpadden tegne en firkant med en
sidelængde på `length` pixels.

### 4. Triangle
- Skriv en funktion `triangle`, som accepterer en parameter `length`.
- Når denne funktion kaldes, skal skildpadden tegne en ligesidet trekant
med en sidelængde på `length` pixels.

### 5. Coloured Triangle
- Dupliker koden for funktionen `triangle`. 
- Omdøb den duplikerede funktion til `coloured_triangle`. 
- Tilføj en parameter `color`, som styrer med hvilken farve skildpadden tegner.

### 6. Many Squares
- Skriv en funktion `many_squares` med en for-loop, som kalder `square` 
gentagne gange.
- Brug denne funktion til at tegne flere firkanter af forskellig størrelse i 
  forskellige positioner.
- Funktionen skal have 3 parametre:
    - `number_of_squares`: hvor mange firkanter skal der tegnes?
    - `size`: hvor store er firkanterne?
    - `distance`: hvor langt væk fra den sidste firkant er den næste firkant 
placeret?

### 7. Many Circles
- Brug dine funktioner `circle` og `move_to` til at skrive en funktion
`many_circles`, som tegner 10 cirkler. 
- Brug en for-løkke for det.
- Du bestemmer, hvor stor cirklerne er, og hvor de befinder sig.

### 8. Draw Square At
- Skriv en funktion `draw_square_at`, som accepterer tre parametre:
`length`, `x` og `y`. 
- Funktionen skal tegne en firkant med den givne sidelængde. 
- Det øverste venstre hjørne af firkanten skal ligge på de
angivne koordinater `x`, `y`. 
- Brug din tidligere funktion `square`.

### 9. Draw Grid
- Lav en funktion `draw_grid`, der tegner et gitter (fx 5x5 firkanter).
- Funktionen skal tage parametre for antal rækker, antal kolonner og
firkantens størrelse.

### 10. Draw House
- Lav en funktion `draw_house`, som tegner et simpelt hus bestående af en
firkant (husets krop) og en trekant (taget). 
- Funktionen skal tage parametre for størrelse og farver.

### 11. Spiral Square Pattern
- Skriv en funktion, der producerer mønstre, der ligner [dette](https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/).

### 12. Star Polygons
- Skriv en funktion, der producerer mønstre svarende til [dette](https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/).
- Funktionen skal have en parameter, som påvirker mønsterets form.

### 13. Cool Pattern
- Opret din egen funktion, der producerer et sejt mønster.
- Måske har du lyst til at bruge random numbers for det.
