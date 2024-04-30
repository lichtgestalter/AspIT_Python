"""
Opgave "Mere tips&tricks til pycharm":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe og løs opgaven dér.


1) Debugger:
Se denne video: https://youtu.be/j0Wz_uBaDmo?si=pSeDspIym1BIBHeB&t=61
Brug debuggeren med eksempelkoden nedenfor.
    Sæt fx et breakpoint i begyndelsen af for-løkken og klik på billen for at starte programmet i debuggertilstand.
    Tryk på F8 eller F7 flere gange og se hvad der sker efter hvert enkelt trin.
    Hvad er forskellen mellem F8 og F7?


2) Refactoring:
Se denne video: https://www.youtube.com/watch?v=4kzEbqaT2DY&t=56s
Ændr eksempelkoden nedenfor ved at refaktorisere.
    Ændr fx funktionens navn fra eksempel til ny_eksempel.
    Skift fx navnet på funktionsparameteren fra number til some_number.
    Tilføj en anden parameter til funktionen.

3) Shortcuts
Vend tilbage til S0105_pycharm_tips.py og prøv nogle shortcuts i eksempelkoden nedenfor.

"""

# Den følgende kode tjener som legeplads for de ovenstående opgaver.

def eksempel(number):
    result = 0
    for n in range(number, 2 * number, 3):
        result += n
    result *= 10
    return result


print("Start")
print(f"{eksempel(4)=}")
print(f"{eksempel(7)=}")
print("End")
