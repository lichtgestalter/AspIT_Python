"""Nogle buttons er blevet fjernet igen for at gøre koden mere kompakt.
Der er blevet tilføjet padding.

Kør programmet.
Læs alle kommentarerne.
Find ud af, hvad hver række kode gør. F.eks. ved at ændre koden lidt og køre den igen.

Leg især med værdierne for padx og pady."""

import tkinter as tk

# The following two variables hold the amount of padding in horizontal and vertical direction.
# Using variables instead of typing in the actual numbers for every
# single GUI object makes the code more compact and easier to change.
padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create a button
button_1 = tk.Button(main_window, text="Click me, I am a button")
button_1.grid(row=0, column=1, padx=padx, pady=pady)  # Padding gives the GUI objects a minimum distance from each other.

# Create a label
label_1 = tk.Label(main_window, text="this is a label")
label_1.grid(row=2, column=3, padx=padx, pady=pady)

# Create an entry
entry_1 = tk.Entry(main_window, width=24, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")


if __name__ == "__main__":
    main_window.mainloop()
