import tkinter as tk
from hmac import digest_size
from tkinter import ttk

import danskcargo_data as dcd
import danskcargo_sql as dcsql

# region global constants
padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"
# endregion global constants
def read_container_entries():
    return entry_container_id.get(), entry_container_weight.get(), entry_container_destination.get(),


def clear_container_entries():
    entry_container_id.delete(0, tk.END)
    entry_container_weight.delete(0, tk.END)
    entry_container_destination.delete(0, tk.END)
    entry_container_weather.delete(0, tk.END)


def write_container_entries(values):
    entry_container_id.insert(0, values[0])
    entry_container_weight.insert(0, values[1])
    entry_container_destination.insert(0, values[2])


def edit_container(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_container_entries()
    write_container_entries(values)

def create_container(tree, record):
    container = dcd.Container.convert_from_tuple(record)
    dcsql.create_record(container)
    clear_container_entries()
    refresh_treeview(tree, dcd.Container)

def update_container(tree, record):
    container = dcd.Container.convert_from_tuple(record)
    dcsql.update_container(container)
    clear_container_entries()
    refresh_treeview(tree, dcd.Container)

def delete_container(tree, record):
    container = dcd.Container.convert_from_tuple(record)
    dcsql.delete_soft_container(container)
    clear_container_entries()
    refresh_treeview(tree, dcd.Container)

# endregion container functions

# region common functions
def read_table(tree, class_):
    count = 0
    result = dcsql.select_all(class_)
    for record in result:
        if record.valid():
            if count % 2 == 0:
               tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))
            else:
               tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))
            count += 1
def empty_treeview(tree):
    tree.delete(*tree.get_children())

def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)

# endregion common functions

# region common widgets
main_window = tk.Tk()
main_window.title("Aspit S2: DanskCargo")
main_window.geometry("500x500")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map("Treeview", background=[('selected', treeview_selected)])
# endregion common widgets

# region container widgets
frame_container = tk.LabelFrame(main_window, text="Container")
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)

tree_container['columns'] = ("id", "weight", "destination")
tree_container.column("#0", width=0, stretch=tk.NO)
tree_container.column("id", anchor=tk.E, width=40)
tree_container.column("weight", anchor=tk.E, width=80)
tree_container.column("destination", anchor=tk.W, width=200)

tree_container.heading("#0", text="", anchor=tk.W)
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("weight", text="Weight", anchor=tk.CENTER)
tree_container.heading("destination", text="Destination", anchor=tk.CENTER)
tree_container.tag_configure('oddrow', background=oddrow)
tree_container.tag_configure('evenrow', background=evenrow)

tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree_container))

controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_container = tk.Frame(controls_frame_container)
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)

label_container_id = tk.Label(edit_frame_container, text="Id")
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)

label_container_weight = tk.Label(edit_frame_container, text="Weight")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)

label_container_destination = tk.Label(edit_frame_container, text="Destination")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)

label_container_weather = tk.Label(edit_frame_container, text="Weather")
label_container_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_container_weather = tk.Entry(edit_frame_container, width=14)
entry_container_weather.grid(row=1, column=3, padx=padx, pady=pady)

button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)

button_create_container = tk.Button(button_frame_container, text="Create", command=lambda: create_container(tree_container, read_container_entries()))
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update", command=lambda: update_container(tree_container, read_container_entries()))
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete", command=lambda: delete_container(tree_container, read_container_entries()))
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_container, text="Clear Entry Boxes", command=clear_container_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)

# endregion container widgets

# region main program
if __name__ == "__main__":
    refresh_treeview(tree_container, dcd.Container)
    main_window.mainloop()
# endregion main program
