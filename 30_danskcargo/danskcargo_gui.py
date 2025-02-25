import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import danskcargo_data as dcd
import danskcargo_sql as dcsql
import danskcargo_func as dcf


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

#region container functions
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

#region aircraft functions
def read_aircraft_entries():
    return entry_aircraft_id.get(), entry_aircraft_max_cargo_weight.get(), entry_aircraft_registration.get(),


def clear_aircraft_entries():
    entry_aircraft_id.delete(0, tk.END)
    entry_aircraft_max_cargo_weight.delete(0, tk.END)
    entry_aircraft_registration.delete(0, tk.END)

def write_aircraft_entries(values):
    entry_aircraft_id.insert(0, values[0])
    entry_aircraft_max_cargo_weight.insert(0, values[1])
    entry_aircraft_registration.insert(0, values[2])


def edit_aircraft(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_aircraft_entries()
    write_aircraft_entries(values)

def create_aircraft(tree, record):
    aircraft = dcd.Aircraft.convert_from_tuple(record)
    dcsql.create_record(aircraft)
    clear_aircraft_entries()
    refresh_treeview(tree, dcd.Aircraft)

def update_aircraft(tree, record):
    aircraft = dcd.Aircraft.convert_from_tuple(record)
    dcsql.update_aircraft(aircraft)
    clear_aircraft_entries()
    refresh_treeview(tree, dcd.Aircraft)

def delete_aircraft(tree, record):
    aircraft = dcd.Aircraft.convert_from_tuple(record)
    dcsql.delete_soft_aircraft(aircraft)
    clear_aircraft_entries()
    refresh_treeview(tree, dcd.Aircraft)

# endregion container functions

#region transport functions
def read_transport_entries():
    return entry_transport_id.get(), entry_transport_date.get(), entry_transport_container_id.get(), entry_transport_aircraft_id.get(),


def clear_transport_entries():
    entry_transport_id.delete(0, tk.END)
    entry_transport_date.delete(0, tk.END)
    entry_transport_container_id.delete(0, tk.END)
    entry_transport_aircraft_id.delete(0, tk.END)

def write_transport_entries(values):
    entry_transport_id.insert(0, values[0])
    entry_transport_date.insert(0, values[1])
    entry_transport_container_id.insert(0, values[2])
    entry_transport_aircraft_id.insert(0, values[3])


def edit_transport(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_transport_entries()
    write_transport_entries(values)

def create_transport(tree, record):
    transport = dcd.Transport.convert_from_tuple(record)  # Convert tuple to Transport
    capacity_ok = dcf.capacity_available(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    destination_ok = dcf.max_one_destination(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    if destination_ok:
        if capacity_ok:
            dcsql.create_record(transport)  # Update database
            clear_transport_entries()  # Clear entry boxes
            refresh_treeview(tree, dcd.Transport)  # Refresh treeview table
        else:
            messagebox.showwarning("", "Not enough capacity on aircraft!")
    else:
        messagebox.showwarning("", "Aircraft already has another destination!")


def update_transport(tree, record):
    transport = dcd.Transport.convert_from_tuple(record)  # Convert tuple to Transport
    print(transport)
    print(dcsql.get_record(dcd.Aircraft, transport.aircraft_id))
    print(dcsql.get_record(dcd.Container, transport.container_id))
    capacity_ok = dcf.capacity_available(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    destination_ok = dcf.max_one_destination(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    if destination_ok:
        if capacity_ok:
            dcsql.update_transport(transport)  # Update database
            clear_transport_entries()  # Clear entry boxes
            refresh_treeview(tree, dcd.Transport)  # Refresh treeview table
        else:
            messagebox.showwarning("", "Not enough capacity on aircraft!")
    else:
        messagebox.showwarning("", "Aircraft already has another destination!")


def delete_transport(tree, record):
    transport = dcd.Container.convert_from_tuple(record)
    dcsql.delete_soft_Transport(transport)
    clear_transport_entries()
    refresh_treeview(tree, dcd.Transport)

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
main_window.geometry("1200x500")

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

# region aircraft widgets
frame_aircraft = tk.LabelFrame(main_window, text="Aircraft")
frame_aircraft.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)

tree_frame_aircraft = tk.Frame(frame_aircraft)
tree_frame_aircraft.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_aircraft = tk.Scrollbar(tree_frame_aircraft)
tree_scroll_aircraft.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_aircraft = ttk.Treeview(tree_frame_aircraft, yscrollcommand=tree_scroll_aircraft.set, selectmode="browse")
tree_aircraft.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_aircraft.config(command=tree_aircraft.yview)

tree_aircraft['columns'] = ("id", "max_cargo_weight", "registration")
tree_aircraft.column("#0", width=0, stretch=tk.NO)
tree_aircraft.column("id", anchor=tk.E, width=40)
tree_aircraft.column("max_cargo_weight", anchor=tk.E, width=100)
tree_aircraft.column("registration", anchor=tk.W, width=100)

tree_aircraft.heading("#0", text="", anchor=tk.W)
tree_aircraft.heading("id", text="Id", anchor=tk.CENTER)
tree_aircraft.heading("max_cargo_weight", text="Max.Carg.Wgt", anchor=tk.CENTER)
tree_aircraft.heading("registration", text="Registration", anchor=tk.CENTER)
tree_aircraft.tag_configure('oddrow', background=oddrow)
tree_aircraft.tag_configure('evenrow', background=evenrow)

tree_aircraft.bind("<ButtonRelease-1>", lambda event: edit_aircraft(event, tree_aircraft))

controls_frame_aircraft = tk.Frame(frame_aircraft)
controls_frame_aircraft.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_aircraft = tk.Frame(controls_frame_aircraft)
edit_frame_aircraft.grid(row=0, column=0, padx=padx, pady=pady)

label_aircraft_id = tk.Label(edit_frame_aircraft, text="Id")
label_aircraft_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_aircraft_id = tk.Entry(edit_frame_aircraft, width=4, justify="right")
entry_aircraft_id.grid(row=1, column=0, padx=padx, pady=pady)

label_aircraft_max_cargo_weight = tk.Label(edit_frame_aircraft, text="Max.Carg.Wgt")
label_aircraft_max_cargo_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_aircraft_max_cargo_weight = tk.Entry(edit_frame_aircraft, width=8, justify="right")
entry_aircraft_max_cargo_weight.grid(row=1, column=1, padx=padx, pady=pady)

label_aircraft_registration = tk.Label(edit_frame_aircraft, text="Registration")
label_aircraft_registration.grid(row=0, column=2, padx=padx, pady=pady)
entry_aircraft_registration = tk.Entry(edit_frame_aircraft, width=20)
entry_aircraft_registration.grid(row=1, column=2, padx=padx, pady=pady)

button_frame_aircraft = tk.Frame(controls_frame_aircraft)
button_frame_aircraft.grid(row=1, column=0, padx=padx, pady=pady)

button_create_aircraft = tk.Button(button_frame_aircraft, text="Create", command=lambda: create_aircraft(tree_aircraft, read_aircraft_entries()))
button_create_aircraft.grid(row=0, column=1, padx=padx, pady=pady)
button_update_aircraft = tk.Button(button_frame_aircraft, text="Update", command=lambda: update_aircraft(tree_aircraft, read_aircraft_entries()))
button_update_aircraft.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_aircraft = tk.Button(button_frame_aircraft, text="Delete", command=lambda: delete_aircraft(tree_aircraft, read_aircraft_entries()))
button_delete_aircraft.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_aircraft, text="Clear Entry Boxes", command=clear_aircraft_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)

# endregion aircraft widgets

# region transport widgets
frame_transport = tk.LabelFrame(main_window, text="Transport")
frame_transport.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)

tree_frame_transport = tk.Frame(frame_transport)
tree_frame_transport.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_transport = tk.Scrollbar(tree_frame_transport)
tree_scroll_transport.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_transport = ttk.Treeview(tree_frame_transport, yscrollcommand=tree_scroll_transport.set, selectmode="browse")
tree_transport.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_transport.config(command=tree_transport.yview)

tree_transport['columns'] = ("id", "date", "container_id", "aircraft_id")
tree_transport.column("#0", width=0, stretch=tk.NO)
tree_transport.column("id", anchor=tk.E, width=40)
tree_transport.column("date", anchor=tk.E, width=80)
tree_transport.column("container_id", anchor=tk.W, width=80)
tree_transport.column("aircraft_id", anchor=tk.W, width=80)

tree_transport.heading("#0", text="", anchor=tk.W)
tree_transport.heading("id", text="Id", anchor=tk.CENTER)
tree_transport.heading("date", text="Date", anchor=tk.CENTER)
tree_transport.heading("container_id", text="Container Id", anchor=tk.CENTER)
tree_transport.heading("aircraft_id", text="Aircraft Id", anchor=tk.CENTER)
tree_transport.tag_configure('oddrow', background=oddrow)
tree_transport.tag_configure('evenrow', background=evenrow)

tree_transport.bind("<ButtonRelease-1>", lambda event: edit_transport(event, tree_transport))

controls_frame_transport = tk.Frame(frame_transport)
controls_frame_transport.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_transport = tk.Frame(controls_frame_transport)
edit_frame_transport.grid(row=0, column=0, padx=padx, pady=pady)

label_transport_id = tk.Label(edit_frame_transport, text="Id")
label_transport_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_transport_id = tk.Entry(edit_frame_transport, width=4, justify="right")
entry_transport_id.grid(row=1, column=0, padx=padx, pady=pady)

label_transport_date = tk.Label(edit_frame_transport, text="Date")
label_transport_date.grid(row=0, column=1, padx=padx, pady=pady)
entry_transport_date = tk.Entry(edit_frame_transport, width=8, justify="right")
entry_transport_date.grid(row=1, column=1, padx=padx, pady=pady)

label_transport_container_id = tk.Label(edit_frame_transport, text="Container Id")
label_transport_container_id.grid(row=0, column=2, padx=padx, pady=pady)
entry_transport_container_id = tk.Entry(edit_frame_transport, width=20)
entry_transport_container_id.grid(row=1, column=2, padx=padx, pady=pady)

label_transport_aircraft_id = tk.Label(edit_frame_transport, text="Aircraft Id")
label_transport_aircraft_id.grid(row=0, column=3, padx=padx, pady=pady)
entry_transport_aircraft_id = tk.Entry(edit_frame_transport, width=14)
entry_transport_aircraft_id.grid(row=1, column=3, padx=padx, pady=pady)

button_frame_transport = tk.Frame(controls_frame_transport)
button_frame_transport.grid(row=1, column=0, padx=padx, pady=pady)

button_create_transport = tk.Button(button_frame_transport, text="Create", command=lambda: create_transport(tree_transport, read_transport_entries()))
button_create_transport.grid(row=0, column=1, padx=padx, pady=pady)
button_update_transport = tk.Button(button_frame_transport, text="Update", command=lambda: update_transport(tree_transport, read_transport_entries()))
button_update_transport.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_transport = tk.Button(button_frame_transport, text="Delete", command=lambda: delete_transport(tree_transport, read_transport_entries()))
button_delete_transport.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_transport, text="Clear Entry Boxes", command=clear_transport_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)

# endregion transport widgets

# region main program
if __name__ == "__main__":
    refresh_treeview(tree_container, dcd.Container)
    refresh_treeview(tree_aircraft, dcd.Aircraft)
    refresh_treeview(tree_transport, dcd.Transport)

    main_window.mainloop()
# endregion main program
