import tkinter as tk
from tkinter import ttk

class GUIElements:

    def __init__(self, container_list):
        self.padx = 8  # Horizontal distance to neighboring objects
        self.pady = 4  # Vertical distance to neighboring objects
        self.rowheight = 24  # rowheight in treeview
        self.treeview_background = "#eeeeee"  # color of background in treeview
        self.treeview_foreground = "black"  # color of foreground in treeview
        self.treeview_selected = "#206030"  # color of selected row in treeview
        self.oddrow = "#dddddd"  # color of odd row in treeview
        self.evenrow = "#cccccc"  # color of even row in treeview

        # region common widgets
        self.main_window = tk.Tk()  # Define the main window
        self.main_window.title('my first GUI')  # Text shown in the top window bar
        self.main_window.geometry("500x500")  # window size

        self.style = ttk.Style()  # Add style
        self.style.theme_use('default')  # Pick theme

        # Configure treeview colors and formatting. A treeview is an object that can contain a data table.
        self.style.configure("Treeview", background=self.treeview_background, foreground=self.treeview_foreground, rowheight=self.rowheight, fieldbackground=self.treeview_background)
        self.style.map('Treeview', background=[('selected', self.treeview_selected)])  # Define color of selected row in treeview
        # endregion common widgets

        # region container widgets
        # Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
        self.frame_container = tk.LabelFrame(self.main_window, text="Container")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
        self.frame_container.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

        # Define data table (Treeview) and its scrollbar. Put them in a Frame.
        self.tree_frame_container = tk.Frame(self.frame_container)  # https://www.tutorialspoint.com/python/tk_frame.htm
        self.tree_frame_container.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.tree_scroll_container = tk.Scrollbar(self.tree_frame_container)
        self.tree_scroll_container.grid(row=0, column=1, padx=0, pady=self.pady, sticky='ns')
        self.tree_container = ttk.Treeview(self.tree_frame_container, yscrollcommand=self.tree_scroll_container.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
        self.tree_container.grid(row=0, column=0, padx=0, pady=self.pady)
        self.tree_scroll_container.config(command=self.tree_container.yview)

        # Define the data table's formatting and content
        self.tree_container['columns'] = ("id", "weight", "destination")  # Define columns
        self.tree_container.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the annoying first empty column.
        self.tree_container.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
        self.tree_container.column("weight", anchor=tk.E, width=80)
        self.tree_container.column("destination", anchor=tk.W, width=200)
        self.tree_container.heading("#0", text="", anchor=tk.W)  # Create column headings
        self.tree_container.heading("id", text="Id", anchor=tk.CENTER)
        self.tree_container.heading("weight", text="Weight", anchor=tk.CENTER)
        self.tree_container.heading("destination", text="Destination", anchor=tk.CENTER)
        self.tree_container.tag_configure('oddrow', background=self.oddrow)  # Create tags for rows in 2 different colors
        self.tree_container.tag_configure('evenrow', background=self.evenrow)

        self.tree_container.bind("<ButtonRelease-1>", lambda event: edit_container(event, self.tree_container, self))  # Define function to be called, when an item is selected.

        # Define Frame which contains labels, entries and buttons
        self.controls_frame_container = tk.Frame(self.frame_container)
        self.controls_frame_container.grid(row=3, column=0, padx=self.padx, pady=self.pady)

        # Define Frame which contains labels (text fields) and entries (input fields)
        self.edit_frame_container = tk.Frame(self.controls_frame_container)  # Add tuple entry boxes
        self.edit_frame_container.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        # label and entry for container id
        self.label_container_id = tk.Label(self.edit_frame_container, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
        self.label_container_id.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.entry_container_id = tk.Entry(self.edit_frame_container, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
        self.entry_container_id.grid(row=1, column=0, padx=self.padx, pady=self.pady)
        # label and entry for container weight
        self.label_container_weight = tk.Label(self.edit_frame_container, text="Weight")
        self.label_container_weight.grid(row=0, column=1, padx=self.padx, pady=self.pady)
        self.entry_container_weight = tk.Entry(self.edit_frame_container, width=8, justify="right")
        self.entry_container_weight.grid(row=1, column=1, padx=self.padx, pady=self.pady)
        # label and entry for container destination
        self.label_container_destination = tk.Label(self.edit_frame_container, text="Destination")
        self.label_container_destination.grid(row=0, column=2, padx=self.padx, pady=self.pady)
        self.entry_container_destination = tk.Entry(self.edit_frame_container, width=20)
        self.entry_container_destination.grid(row=1, column=2, padx=self.padx, pady=self.pady)
        # label and entry for container destination
        self.label_container_weather = tk.Label(self.edit_frame_container, text="Weather")
        self.label_container_weather.grid(row=0, column=3, padx=self.padx, pady=self.pady)
        self.entry_container_weather = tk.Entry(self.edit_frame_container, width=14)
        self.entry_container_weather.grid(row=1, column=3, padx=self.padx, pady=self.pady)

        # Define Frame which contains buttons
        self.button_frame_container = tk.Frame(self.controls_frame_container)
        self.button_frame_container.grid(row=1, column=0, padx=self.padx, pady=self.pady)
        # Define buttons
        self.button_create_container = tk.Button(self.button_frame_container, text="Create", command=lambda: create_container(self.tree_container, read_container_entries(self), self, container_list))
        self.button_create_container.grid(row=0, column=1, padx=self.padx, pady=self.pady)
        self.button_update_container = tk.Button(self.button_frame_container, text="Update", command=lambda: update_container(self.tree_container, read_container_entries(self), self, container_list))
        self.button_update_container.grid(row=0, column=2, padx=self.padx, pady=self.pady)
        self.button_delete_container = tk.Button(self.button_frame_container, text="Delete", command=lambda: delete_container(self.tree_container, read_container_entries(self), self, container_list))
        self.button_delete_container.grid(row=0, column=3, padx=self.padx, pady=self.pady)
        self.select_record_button = tk.Button(self.button_frame_container, text="Clear Entry Boxes", command=lambda: clear_container_entries(self))
        self.select_record_button.grid(row=0, column=4, padx=self.padx, pady=self.pady)
        # endregion container widgets


class Container:

    def __init__(self, id, weight, destination):
        self.id = id
        self.weight = weight
        self.destination = destination

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Container({self.id=:4}    {self.weight=:16}    {self.destination=})"

    def convert_to_tuple(self):  # Convert Container to tuple
        return self.id, self.weight, self.destination

    def valid(self):
        try:
            value = int(self.weight)
        except ValueError:
            return False
        return value >= 0

    @classmethod
    def convert_from_tuple(cls, tuple_):  # Convert tuple to Container
        container = cls(id=tuple_[0], weight=tuple_[1], destination=tuple_[2])
        return container


# region container functions


def read_container_entries(gui):  # Read content of entry boxes
    return gui.entry_container_id.get(), gui.entry_container_weight.get(), gui.entry_container_destination.get(),


def clear_container_entries(gui):  # Clear entry boxes
    gui.entry_container_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    gui.entry_container_weight.delete(0, tk.END)
    gui.entry_container_destination.delete(0, tk.END)
    gui.entry_container_weather.delete(0, tk.END)


def write_container_entries(values, gui):  # Fill entry boxes
    gui.entry_container_id.insert(0, values[0])
    gui.entry_container_weight.insert(0, values[1])
    gui.entry_container_destination.insert(0, values[2])


def edit_container(event, tree, gui):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_container_entries(gui)  # Clear entry boxes
    write_container_entries(values, gui)  # Fill entry boxes


def create_container(tree, record, gui, container_list):  # add new tuple to database
    container = Container.convert_from_tuple(record)  # Convert tuple to Container
    container_list.append(container)  # add container to database
    clear_container_entries(gui)  # Clear entry boxes
    refresh_treeview(tree, container_list)  # Refresh treeview table


def update_container(tree, record, gui, container_list):  # update tuple in database
    container = Container.convert_from_tuple(record)  # Convert tuple to Container
    for c in container_list:  # Update database
        if c.id == container.id:
            c.weight = container.weight
            c.destination = container.destination
    clear_container_entries(gui)  # Clear entry boxes
    refresh_treeview(tree, container_list)  # Refresh treeview table


def delete_container(tree, record, gui, container_list):  # delete tuple in database
    container = Container.convert_from_tuple(record)  # Convert tuple to Container
    for c in container_list:  # Update database
        if c.id == container.id:
            c.weight = -1
    clear_container_entries(gui)  # Clear entry boxes
    refresh_treeview(tree, container_list)  # Refresh treeview table


def read_table(tree, container_list):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    for record in container_list:  # Read all containers from database
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1


# endregion container functions

# region common functions

def refresh_treeview(tree, container_list):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, container_list)  # Fill treeview from database


def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())

# endregion common functions

def make_dummy_database():
    container_list = []
    container_list.append(Container("1", "1000", "oslo"))
    container_list.append(Container("2", "2000", "chicago"))
    container_list.append(Container("3", "3000", "milano"))
    container_list.append(Container("4", "4000", "amsterdam"))
    container_list.append(Container("1", "1000", "oslo"))
    container_list.append(Container("2", "2000", "chicago"))
    container_list.append(Container("3", "3000", "milano"))
    container_list.append(Container("4", "4000", "amsterdam"))
    container_list.append(Container("1", "1000", "oslo"))
    container_list.append(Container("2", "2000", "chicago"))
    container_list.append(Container("3", "3000", "milano"))
    container_list.append(Container("4", "4000", "amsterdam"))
    container_list.append(Container("1", "1000", "oslo"))
    container_list.append(Container("2", "2000", "chicago"))
    container_list.append(Container("3", "3000", "milano"))
    container_list.append(Container("4", "4000", "amsterdam"))
    container_list.append(Container("1", "1000", "oslo"))
    container_list.append(Container("2", "2000", "chicago"))
    container_list.append(Container("3", "3000", "milano"))
    container_list.append(Container("4", "4000", "amsterdam"))
    container_list.append(Container("1", "1000", "oslo"))
    container_list.append(Container("2", "2000", "chicago"))
    container_list.append(Container("3", "3000", "milano"))
    container_list.append(Container("4", "4000", "amsterdam"))
    return container_list


def main():
    container_list = make_dummy_database()
    gui = GUIElements(container_list)
    refresh_treeview(gui.tree_container, container_list)  # Load data from database
    gui.main_window.mainloop()  # Wait for button clicks and act upon them


main()
