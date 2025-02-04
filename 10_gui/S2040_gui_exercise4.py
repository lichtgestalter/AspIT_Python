""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

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

def read_table(tree, data):  # fill tree with test data
    tree.delete(*tree.get_children())
    count = 0
    for record in data:
        if count % 2 == 0:  # even
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1

def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    id_entry.delete(0, tk.END)
    id_entry.insert(0, values[0])
    weight_entry.delete(0, tk.END)
    weight_entry.insert(0, values[1])
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, values[2])

def update_record():
    index_selected = tree_1.focus()
    index = tree_1.index(index_selected)
    test_data_list[index] = (id_entry.get(), weight_entry.get(), destination_entry.get())
    read_table(tree_1, test_data_list)

def delete_record():
    index_selected = tree_1.focus()
    index = tree_1.index(index_selected)
    del test_data_list[index]
    read_table(tree_1, test_data_list)

def create_record():
    index_selected = tree_1.focus()
    test_data_list.append((id_entry.get(), weight_entry.get(), destination_entry.get()))
    read_table(tree_1, test_data_list)

padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
oddrow = "#ddeedd"
evenrow = "#cce0cc"

test_data_list = []
test_data_list.append(("1", "1000", "oslo"))
test_data_list.append(("2", "2000", "chicago"))
test_data_list.append(("3", "3000", "milano"))
test_data_list.append(("4", "4000", "amsterdam"))

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

tree_1.tag_configure('oddrow', background=oddrow)
tree_1.tag_configure('evenrow', background=evenrow)

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))
read_table(tree_1, test_data_list)

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

create_button = tk.Button(frame3, text="Create", command=create_record)
create_button.grid(column=0, row=0, padx=padx, pady=pady)

update_button = tk.Button(frame3, text="Update", command=update_record)
update_button.grid(column=1, row=0, padx=padx, pady=pady)

delete_button = tk.Button(frame3, text="Delete", command=delete_record)
delete_button.grid(column=2, row=0, padx=padx, pady=pady)

clear_button = tk.Button(frame3, text="Clear Entry Boxes", command=clear)
clear_button.grid(column=3, row=0, padx=padx, pady=pady)


main_window.mainloop()
