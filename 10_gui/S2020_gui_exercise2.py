""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

def clear():
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)

padx = 8
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

labelframe = tk.LabelFrame(main_window, text="Container")
labelframe.grid(column=0, row=0, padx=padx, pady=pady)

frame1 = tk.Frame(labelframe)
frame1.grid(column=0, row=0, padx=padx, pady=pady)

id_label = tk.Label(frame1, text="Id")
id_label.grid(column=0, row=0, padx=padx, pady=pady)
id_entry = tk.Entry(frame1, width=4)
id_entry.grid(column=0, row=1, padx=padx, pady=pady)

weight_label = tk.Label(frame1, text="Weight")
weight_label.grid(column=1, row=0, padx=padx, pady=pady)
weight_entry = tk.Entry(frame1, width=10)
weight_entry.grid(column=1, row=1, padx=padx, pady=pady)

destination_label = tk.Label(frame1, text="Destination")
destination_label.grid(column=2, row=0, padx=padx, pady=pady)
destination_entry = tk.Entry(frame1, width=20)
destination_entry.grid(column=2, row=1, padx=padx, pady=pady)

weather_label = tk.Label(frame1, text="Weather")
weather_label.grid(column=3, row=0, padx=padx, pady=pady)
weather_entry = tk.Entry(frame1, width=16)
weather_entry.grid(column=3, row=1, padx=padx, pady=pady)

frame2 = tk.Frame(labelframe)
frame2.grid(column=0, row=1, padx=padx, pady=pady)

create_button = tk.Button(frame2, text="Create")
create_button.grid(column=0, row=0, padx=padx, pady=pady)

update_button = tk.Button(frame2, text="Update")
update_button.grid(column=1, row=0, padx=padx, pady=pady)

delete_button = tk.Button(frame2, text="Delete")
delete_button.grid(column=2, row=0, padx=padx, pady=pady)

clear_button = tk.Button(frame2, text="Clear Entry Boxes", command=clear)
clear_button.grid(column=3, row=0, padx=padx, pady=pady)


main_window.mainloop()