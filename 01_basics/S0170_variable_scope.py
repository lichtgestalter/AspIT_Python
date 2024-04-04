"""
Opgave "Variable Scope":

Læs https://www.w3schools.com/python/python_scope.asp.

I den tekst, der er linket til ovenfor, forklares nøgleordet "global" blandt andet.
Undgå helst at bruge dette nøgleord i din egen kode.  Det ville være dårlig programmeringsskik og gøre dit program sårbart over for fejl.

Kør programmet og find ud af, hvad der skete.
Hvorfor fremkalder print(x) forskellige resultater indenfor og udenfor funktionen?
Læs kommentarerne i koden.

Skift nu til variable_scope_2.py
"""

def some_function():
  x = "This is a local variable inside the function"  # x is local here and shadows the global variable x in outer scope
  print(x)


x = "This is a global variable outside the function"
some_function()
print(x)
