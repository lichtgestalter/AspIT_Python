"""
Opgave "Variable Scope 2":

Hvis du har en funktion, der kalder en anden funktion, og den kaldte funktion skal bruge variabler fra
den kaldende funktion, så er det bedst, hvis du sender disse variabler som parametre.

Det er god programmeringsskik, at undgå globale variabler og at hovedprogrammet bare indeholder
en enkel linje, som kalder funktionen main.

Kør programmet og find ud af, hvad der skete.
Hvorfor fremkalder print(x) forskellige resultater?
Læs kommentarerne i koden.
"""

def some_function():
  x = "This is a local variable inside the function some_function"  # x is local here and shadows the global variable x in outer scope
  print(x)


def another_function(x):
  print(x, ", which was handed to another function as an argument.")  # uses the parameter x


def main():
  x = "This is a local variable inside the function main"
  some_function()
  another_function(x)
  print(x)


main()
