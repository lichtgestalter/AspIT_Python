import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Variabler (variables)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Vi kan oprette en ny Python-variabel ved at tildele en værdi til et mærke ved hjælp af tildelingsoperatoren `=`.

    I dette eksempel tildeler vi en streng med værdien `"Hans"` til mærket `name`:
    """)
    return


@app.cell
def _():
    name = "Hans"
    return


@app.cell
def _(mo):
    mo.md(r"""
    Her er et eksempel med et tal:
    """)
    return


@app.cell
def _():
    age = 7
    return


@app.cell
def _(mo):
    mo.md(r"""
    Med denne kode har vi gemt tallet 7 i variablen `age`.

    Et variabelnavn kan bestå af bogstaver, tal og _ understregningstegnet (underscore).
    Det kan ikke starte med et tal.

    Disse er alle gyldige variabelnavne:
    """)
    return


@app.cell
def _():
    test5 = 1
    TEST = 1
    tEST = 1
    abc123 = 1
    my_name_is_a_secret = 1
    _test = 1
    return


@app.cell
def _(mo):
    mo.md(r"""
    Disse er ugyldige variabelnavne:
    """)
    return


@app.cell
def _():
    # Marimo-filer skal være gyldig Python-syntaks, så de ugyldige variabelnavne
    # herunder er pakket ind i en tekststreng og udført med exec(), for at vi
    # stadig kan demonstrere den samme SyntaxError som i den oprindelige notebook.
    invalid_names_code = """
    123 = 1
    8test = 1
    test! = 1
    test% = 1
    """
    try:
        exec(invalid_names_code)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Øvelser

    Udfør den næste celle. Der opstår en fejl. Hvorfor?

    Læs alle kommentarer i cellen.

    Rediger det problematiske variabelnavn for at undgå fejlen.

    Udfør cellen igen indtil den printer ___Success!___.
    """)
    return


@app.cell
def _():
    # Ligesom ovenfor pakker vi koden ind i en tekststreng, så filen forbliver
    # gyldig Python, men fejlen opstår stadig når koden udføres med exec().
    exercise_code = """
    u7 = 6.87  # Cifre er ok. Men ikke som variablenavnens første symbol.
    øøø = "Hans"  # Tilladt. Men bruge helst bare de 26 engelske standard bogstaver i variablenavne.
    5forbudt = 3  # Forbudt.
    Please_dont_do_this = 2  # Brug ikke store bogstaver i variablenavne
    AbsolutelyDontDoThis = 5  # Brug heller ikke CamelCase i variablenavne
    # Det er en konvention (god programmeringsskik) i Python, ikke at benytte store bogstaver i variablenavne.
    print("Success!")
    """
    try:
        exec(exercise_code)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Opfører din notebook sig mærkeligt?

    Marimo er en reaktiv notebook: når du ændrer en celle, genkører marimo automatisk
    alle celler, der afhænger af den. Det betyder, at du normalt undgår de "usynlige"
    fejl, man kan opleve i traditionelle notebooks (som Jupyter/Colab), hvor cellernes
    rækkefølge og tidligere kørsler kan skabe forvirring.

    Hvis din notebook alligevel opfører sig mærkeligt, kan du genstarte kernelen/runtime'en
    via menuen øverst i marimo (fx `Restart kernel`). Dette nulstiller alle variabler og
    kører notebooken forfra.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Forstod/løste du alt på denne side?
    Ellers spørg [W3schools](https://www.w3schools.com/python/), [Google](https://www.google.com),
    [Perplexity](https://perplexity.ai), andre elever eller læreren.

    Arbejd videre med den næste notebook.
    """)
    return


if __name__ == "__main__":
    app.run()
