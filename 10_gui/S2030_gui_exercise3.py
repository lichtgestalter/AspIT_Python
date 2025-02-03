"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
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
from tkinter import ttk


def clear():
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)

padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

labelframe = tk.LabelFrame(main_window, text="Container")
labelframe.grid(column=0, row=0, padx=padx, pady=pady)

frame1 = tk.Frame(labelframe)
frame1.grid(column=0, row=0, padx=padx, pady=pady)

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

tree_1_scrollbar = tk.Scrollbar(frame1)
tree_1_scrollbar.grid(row=5, column=6, padx=0, pady=pady, sticky='ns')
tree_1 = ttk.Treeview(frame1, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=5, column=5, padx=0, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("id", "weight", "destination")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("id", anchor=tk.E, width=90)
tree_1.column("weight", anchor=tk.W, width=130)
tree_1.column("destination", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("id", text="Id", anchor=tk.CENTER)
tree_1.heading("weight", text="Weight", anchor=tk.CENTER)
tree_1.heading("destination", text="Destination", anchor=tk.CENTER)

frame2 = tk.Frame(labelframe)
frame2.grid(column=0, row=1, padx=padx, pady=pady)

id_label = tk.Label(frame2, text="Id")
id_label.grid(column=0, row=0, padx=padx, pady=pady)
id_entry = tk.Entry(frame2, width=4)
id_entry.grid(column=0, row=1, padx=padx, pady=pady)

weight_label = tk.Label(frame2, text="Weight")
weight_label.grid(column=1, row=0, padx=padx, pady=pady)
weight_entry = tk.Entry(frame2, width=10)
weight_entry.grid(column=1, row=1, padx=padx, pady=pady)

destination_label = tk.Label(frame2, text="Destination")
destination_label.grid(column=2, row=0, padx=padx, pady=pady)
destination_entry = tk.Entry(frame2, width=20)
destination_entry.grid(column=2, row=1, padx=padx, pady=pady)

weather_label = tk.Label(frame2, text="Weather")
weather_label.grid(column=3, row=0, padx=padx, pady=pady)
weather_entry = tk.Entry(frame2, width=16)
weather_entry.grid(column=3, row=1, padx=padx, pady=pady)

frame3 = tk.Frame(labelframe)
frame3.grid(column=0, row=2, padx=padx, pady=pady)

create_button = tk.Button(frame3, text="Create")
create_button.grid(column=0, row=0, padx=padx, pady=pady)

update_button = tk.Button(frame3, text="Update")
update_button.grid(column=1, row=0, padx=padx, pady=pady)

delete_button = tk.Button(frame3, text="Delete")
delete_button.grid(column=2, row=0, padx=padx, pady=pady)

clear_button = tk.Button(frame3, text="Clear Entry Boxes", command=clear)
clear_button.grid(column=3, row=0, padx=padx, pady=pady)


main_window.mainloop()
