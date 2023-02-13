"""
The treeview has now columns.

Run the program.
Read all the comments.
Find out what every row of code does. For example by changing the code a bit and running it again.
Pay special attention to the options of treeview columns and columns headings. Play around with them.
"""
import tkinter as tk
from tkinter import ttk   # we need this additional import for our treeview widget


def empty_entry():  # Delete text in the entry box
    print("button_1 was pressed")
    entry_1.delete(0, tk.END)


padx = 8
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("900x500")  # we've made the window a bit wider

tree_1_scrollbar = tk.Scrollbar(main_window)  # define the scrollbar
tree_1_scrollbar.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')  # place the scrollbar
tree_1 = ttk.Treeview(main_window, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")  # define the treeview, connect it with the scrollbar
tree_1.grid(row=5, column=5, padx=0, pady=pady)  # place the treeview
tree_1_scrollbar.config(command=tree_1.yview)  # connect the scrollbar with the treeview
# Define treeview columns
tree_1['columns'] = ("col1", "col2", "col3")  # define column names
tree_1.column("#0", width=0, stretch=tk.NO)  # Suppress the annoying first empty column.
tree_1.column("col1", anchor=tk.E, width=90)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)
# Create treeview column headings
tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("col1", text="col1 heading", anchor=tk.CENTER)
tree_1.heading("col2", text="col2 heading", anchor=tk.CENTER)
tree_1.heading("col3", text="col3 heading", anchor=tk.CENTER)

frame_1 = tk.LabelFrame(main_window, text="this is the label of the label frame")  # Create a label frame
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

empty_entry_button = tk.Button(main_window, text="Click me, I am a button", command=empty_entry)  # Create a button
empty_entry_button.grid(row=0, column=1, padx=padx, pady=pady)

label_1 = tk.Label(frame_1, text="this is a label")  # Create a label
label_1.grid(row=2, column=3, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_1, width=24, justify="right")  # Create an entry
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")


if __name__ == "__main__":
    main_window.mainloop()
