# Red \& Black Knights

## Indledning
- __Se hele [videoen](https://www.youtube.com/watch?v=UiX4CFIiegM)__.
- __Forstå de regler__, der gælder for placeringen af de sorte og røde 
  springere 
  på brættet (4:28 – 8:18 i videoen), og som er blevet brugt til at generere
  - billedet med 100.000 felter (9:36) 
  - og billedet med 1.000.000 felter (10:37).
- __Tal med din lærer__, hvis du ikke har forstået reglerne fuldt ud.
- Først når du har forstået reglerne helt, skal du også __se denne [video](https://www.youtube.com/watch?v=VgmDuBCayPw)__.

## Projektopgave

- __Generer billeder som dem i videoen__.
- __Bonusopgave 1__: Generer billeder med selvopfundne startkonstellationer, 
  som hverken findes i videoen eller i denne [billedsamling](https://jonka364.github.io/stendhal/stendhal.html).
- __Bonusopgave 2__: Generer billeder med selvopfundne regelændringer eller 
  -udvidelser. Hvis det lykkes, kan det være, at vi sender dine resultater til berømte matematikere :) Mindst til [Neil Sloane](https://en.wikipedia.org/wiki/Neil_Sloane).


## Læringsmål

Undervejs vil du helt automatisk lære en masse om

- Problemløsningsteknikker
- Datastrukturer
- Algoritmer


## Fremgangsmåde

### Før du skriver kode, har du brug for en plan!

- Skriv __delproblemer__ ned, som du skal løse.
- Indeholder disse delproblemer yderligere delproblemer? Skriv dem under det tilhørende delproblem.
- Hvilke delproblemer kan i første omgang programmeres og testes uafhængigt af hinanden?
- Fastlæg en foreløbig __rækkefølge__, hvori du vil løse problemerne.
- __Diskutér din plan med din lærer__. Få hjælp af din lærer i 
  planlægningsfasen.


### Din kode

- __Start simpelt__. Løs kun ét delproblem for et simpelt tilfælde.
- I starten behøver dit program ikke at være fleksibelt.
- Hav alligevel allerede et øje på de første punkter i den næste afsnit 
  "Fleksibilitet"


### Fleksibilitet

Hav i dine beslutninger fokus på, at programmet gerne skal være så fleksibelt som muligt og måske endda kunne håndtere udvidelser/ændringer af spilmekanikken med lille indsats.

- Fleksibel størrelse på spiralen (spillebrættet)
- Fleksibelt antal og rækkefølge af spillebrikker
- Fleksible typer af spillebrikker (med andre bevægelsesregler)
- Regeludvidelse: Spillebrikkerne kan starte fra et andet felt end det først mulige
- Regelændring: Et felt er kun forbudt, hvis det trues af _alle_ andre spillebrikker
- Regelændring: Spillebrikken placeres ikke på det første (mindst mulige), men på det n-te ikke-truede felt (f.eks. n=2)
- Alle disse variationer bør nemt kunne styres fra ét centralt sted i din kode (få linjer)
