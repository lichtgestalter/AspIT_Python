"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

padx = 8
pady = 8

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

frame = tk.LabelFrame(main_window, text="Container")
frame.grid(column=0, row=0)

label = tk.Label(frame, text="id")
label.grid(column=0, row=0, padx=padx, pady=pady)

entry = tk.Entry(frame, width=4)
entry.grid(column=0, row=1, padx=padx, pady=pady)

button = tk.Button(frame, text="Create")
button.grid(column=0, row=2, padx=padx, pady=pady)


main_window.mainloop()