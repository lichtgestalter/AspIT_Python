import tkinter as tk
from tkinter import ttk

padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects
rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#206030"  # color of selected row in treeview
oddrow = "#dddddd"  # color of odd row in treeview
evenrow = "#cccccc"  # color of even row in treeview
INTERNAL_ERROR_CODE = 0

main_window = tk.Tk()  # Define the main window
main_window.title('my first GUI')  # Text shown in the top window bar
main_window.geometry("500x500")  # window size

style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme

# Configure treeview colors and formatting. A treeview is an object that can contain a data table.
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])  # Define color of selected row in treeview

# Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
frame_container = tk.LabelFrame(main_window, text="Container")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_container = tk.Frame(frame_container)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)

# Define the data table's formatting and content
tree_container['columns'] = ("id", "weight", "destination")  # Define columns
tree_container.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_container.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_container.column("weight", anchor=tk.E, width=80)
tree_container.column("destination", anchor=tk.W, width=200)
tree_container.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("weight", text="Weight", anchor=tk.CENTER)
tree_container.heading("destination", text="Destination", anchor=tk.CENTER)
tree_container.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_container.tag_configure('evenrow', background=evenrow)

# Define Frame which contains labels, entries and buttons
controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_container = tk.Frame(controls_frame_container)  # Add tuple entry boxes
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for container id
label_container_id = tk.Label(edit_frame_container, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for container weight
label_container_weight = tk.Label(edit_frame_container, text="Weight")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for container destination
label_container_destination = tk.Label(edit_frame_container, text="Destination")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for container destination
label_container_weather = tk.Label(edit_frame_container, text="Weather")
label_container_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_container_weather = tk.Entry(edit_frame_container, width=14)
entry_container_weather.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_container = tk.Button(button_frame_container, text="Create")
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update")
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete")
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)
select_record_button = tk.Button(button_frame_container, text="Clear Entry Boxes")
select_record_button.grid(row=0, column=4, padx=padx, pady=pady)


if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    main_window.mainloop()  # Wait for button clicks and act upon them
