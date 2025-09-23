# GUI Code Organization

- Det er almindeligt at definere hele GUI'en i hovedprogrammet, fordi alle 
GUI-elementer så bliver globale variabler.
- Dermed har alle funktioner adgang til alle GUI-elementer.
- Det er praktisk i starten, men bliver hurtigt meget uoverskueligt.
- Desuden risikerer man altid, når man bruger globale variabler, at lave 
  programmeringsfejl, der er svære at finde.


### Eksempel for en traditionel løsning  
- Se her i mappen 10_gui i undermappen milestones. 
- A local image, starting with an exclamation mark, then [some alternate 
  text in brackets](../images/gui_files.png):

- Der finder du blandt andet milestone_2040.py.
- Dette er en mønsterløsning af opgave S2040_gui_exercise4.py på traditionel 
  vis med hele GUI'en i hovedprogrammet.


### En bedre løsning
- Sammenlign milestone_2040.py med milestone_2050.py.
- Begge programmer har nøjagtig samme funktionalitet, men i milestone_2050.py 
  defineres hele GUI'en i konstruktøren (__init__) af en klasse.
- Hele programmet klarer sig uden globale variabler.
- I funktionen main defineres GUI'en og gemmes i variablen gui.
- Denne variabel gives derefter som parameter til de funktioner, der har brug 
  for adgang til GUI-elementer.
