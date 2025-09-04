# **Projekt Musikinstrument**

Skab et musikinstrument.

Skriv et program, der omsætter håndbevægelser eller håndpositioner eller fingerbevægelser til musik.

Der er mange forskellige måder, du kan bruge håndstillinger eller lignende som input til dit program. Disse varierer betydeligt i sværhedsgraden af deres implementering. Du kan også kombinere forskellige inputmuligheder.

Eksempler på inputmuligheder:

- En eller to ultralydssensorer måler afstanden til en hånd eller finger i en eller to dimensioner. Hvis du gør det for begge hænder på samme tid, kan du skabe fire uafhængige inputs med fire ultralydssensorer. (Start med at google "ultrasonic sensor arduino hc-sr04".)

- Du holder en lys genstand i din hånd (eller en i hver hånd). Din computers kamera bestemmer det lyse objekts x- og y-position i kamerabilledet. På den måde skaber du op til fire uafhængige inputs. (Start med at google fx ”image feature extraction” eller ” image processing webcams”.)

- Du laver bevægelser (f.eks. "tommelfinger op" eller "knyttet næve") med dine fingre og får dem genkendt af en kunstig intelligens. De forskellige bevægelser kan f.eks. vælge forskellige musikinstrumenter. 

Tænk over, hvilke lydegenskaber du vil påvirke med dit input. Eksempler på lydegenskaber kunne f.eks. være:

- Frekvens/tonehøjde
- Rytme eller rytmehastighed
- Lydbølgernes form (sinus, savtak, rektangel, trekant) 
- Lydstyrke

Tænk over, hvilke basislyde du vil ændre/påvirke med dit input. Det kan være simple sinusbølger, men også lydeksempler, f.eks. fra musikinstrumenter eller andre lydkilder.

Carsten er musiker. Diskutér med ham, hvad dit program skal kunne. Carsten kan hjælpe dig med at beslutte, hvilke basislyde du vil bruge, og hvilke egenskaber ved lydene du vil ændre med dit input.