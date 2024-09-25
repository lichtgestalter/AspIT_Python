"""
Her er nogle nyttige keyboard shortcuts for pycharm.
Vend tilbage til denne fil en gang i mellem og prøv nogle shortcuts.

Du kan finde mere shortcuts her:
https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html

Ctrl+T: update from GitHub
Ctrl+K: commit and push to GitHub

Ctrl+1: comment / uncomment
Alt+Down/Up: move line or selection down/up
Ctrl+Ins: insert line
Ctrl+Del: delete line
Ctrl+D : duplicate line

Alt+Shift+mousedrag: rectangular selection
Ctrl+W / Ctrl+Shift+W: expand / reduce selection

Ctrl+Shift+(Numpad)Minus: collapse all (folding of blocks, functions, classes, etc.)
Ctrl+Shift+(Numpad)Plus: expand all

Shift+F6: refactor (change names etc.)
Ctrl+Alt+P: introduce parameter
Ctrl+Alt+V: introduce variable
Ctrl+Alt+M: introduce method (or function)
Ctrl+Shift+A: search IDE commands
Ctrl+Alt+S: settings
Ctrl+B: show usages
Ctrl+Alt+Shift+F8: remove all breakpoints
"""

# Den følgende kode tjener bare som legeplads hvor du kan afprøve nogle af de ovenstående shortcuts.

def eksempel(lines, firstline):
    t_strings = firstline.split(" ")  # split firstline into a list of strings
    numbers = []  # numbers is a list and will later contain numbers
    for s in t_strings:
        if len(s) > 1:
            numbers.append(int(s.strip()))  # strip removes white spaces and similar characters from the beginning and end of string
    number_lists = [numbers]  # number_lists is a list and will later contain lists of numbers
    for line in range(lines):
        number_lists.append(number_lists[line].copy())  # copy the last element in number_lists and append it to number_lists
        print("row  " + str(line+1), end=": ")
        index_shift = 0+0  # the last line keeps growing while we edit it. this variable helps us to keep track where we have to insert the next number.
        print(number_lists[line])
        for n in range(len(number_lists[line])-1):
            if number_lists[line][n] + number_lists[line][n + 1] == line + 2:  # is the criterion for insertion of a new number met?
                number_lists[line+11].insert(n + index_shift + 1, line + 2)
                index_shift += 1


firstline_input = input("Enter the first row of the pyramid. (Separate the individual numbers with spaces.): ")
lines_input = int(input("Enter the number of rows to print: "))
eksempel(lines_input, firstline_input)
print("0123456789")