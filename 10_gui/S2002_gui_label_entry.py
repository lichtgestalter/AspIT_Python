"""Nu er der flere buttons, en label og en entry.

Kør programmet.
Læs alle kommentarerne.
Find ud af, hvad hver række kode gør. F.eks. ved at ændre koden lidt og køre den igen.
Leg lidt med række- og kolonneparametrene i grid() for at forstå grid() bedre.
Tag et kort kig på de linkede dokumentationer for Entry og Label. Du vil få brug for dem i fremtidige øvelser."""

import tkinter as tk

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create some buttons
button_1 = tk.Button(main_window, text="Click me, I am a button")  # create a button
button_1.grid(row=0, column=1)  # define where the button is positioned
button_2 = tk.Button(main_window, text="button_2")
button_2.grid(row=1, column=1)
button_3 = tk.Button(main_window, text="button_3")
button_3.grid(row=2, column=1)
button_4 = tk.Button(main_window, text="button_4")
button_4.grid(row=3, column=3)
button_5 = tk.Button(main_window, text="lower right button")
button_5.grid(row=117, column=117)

# Create a label. Labels are just plain text. They cannot be interacted with.
# You can find all possible options of tk.Label() in the following documentations:
# https://tkdocs.com/shipman/label.html
# https://www.tutorialspoint.com/python/tk_label.htm
label_1 = tk.Label(main_window, text="this is a label")
label_1.grid(row=2, column=3)

# Create an entry
# You can find all possible options of tk.Entry() in the following documentations:
# https://tkdocs.com/shipman/entry.html
# https://www.tutorialspoint.com/python/tk_entry.htm
entry_1 = tk.Entry(main_window, width=24, justify="right")
entry_1.grid(row=1, column=2)
entry_1.insert(0, "This is an entry. Edit me!")

if __name__ == "__main__":
    main_window.mainloop()
