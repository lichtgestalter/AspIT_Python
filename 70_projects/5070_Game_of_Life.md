# Projekt Game of Life

## Projektmål

Programmer John Conways **Game of Life**.

Programmet skal simulere et todimensionelt gitter af celler. Hver celle er 
enten levende eller død. I hver generation bestemmes cellernes næste 
tilstand ud fra deres naboer.  

Start med at se denne [video](https://www.youtube.com/watch?v=rBaK4-EoF_8) fra 
0:00 til 2:44. 

Programmet skal som minimum kunne:

- oprette et spillebræt med en valgfri størrelse
- starte med en valgt (eller tilfaldig) startkonfiguration
- beregne næste generation
- vise generationerne på en overskuelig måde
- lade brugeren starte, stoppe og nulstille simuleringen
- gemme og indlæse en startkonfiguration

Du skal selv beslutte, hvordan programmet viser simuleringen. Det kan f.eks. være tekstbaseret, grafisk eller som en animation.

## Læringsmål

Undervejs arbejder du blandt andet med:

- datastrukturer
- algoritmer og iteration
- koordinater og naboskab
- tilstandsændringer
- fejlfinding og test

## Fremgangsmåde

Lav først en plan over delproblemerne.

Start med en version, der kun kan beregne én ny generation. Test den grundigt, før du bygger brugergrænsefladen.

Vær særlig opmærksom på, at den nye generation skal beregnes ud fra den 
**gamle** generation. Du må ikke lade ændringer i enkelte celler påvirke 
beregningen af andre celler i samme generation.  

## Udvidelser

- Lad brugeren tegne startkonfigurationen med musen.
- Implementer hastighedskontrol.
- Implementer forskellige kantbetingelser, f.eks. at venstre og højre side hænger sammen.
- Find og vis periodiske mønstre.
- Mål programmets hastighed for forskellige brætstørrelser.
- Undersøg, hvor stor forskel forskellige datastrukturer gør for programmets hastighed.
