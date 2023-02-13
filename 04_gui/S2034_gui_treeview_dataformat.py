"""
The treeview has been formatted to show the data rows in alternating colors. To achieve this,
    (1) the variables oddrow and evenrow have been added
    (2) the function read_table has been extended
    (3) the treeview definition has been extended with 2 tags (tree_1.tag_configure)
To make it easier to find the new code, the above numbers have been added to the comments ((1), (2), ...)

Run the program.
Read all the comments.
Find out what every row of code does. For example by changing the code a bit and running it again.
Pay special attention to the newly added code.
"""
import tkinter as tk
from tkinter import ttk   # we need this additional import for our treeview widget


def empty_entry():  # Delete text in the entry box
    print("button_1 was pressed")
    entry_1.delete(0, tk.END)


def read_table(tree):  # fill tree with test data
    count = 0  # Use counter to keep track of odd and even rows, because these will be colored differently. (2)
    for record in test_data_list:
        if count % 2 == 0:  # even
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))  # Insert one row into the data table
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))  # Insert one row into the data table
        count += 1


padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
oddrow = "#ddeedd"  # color of odd row in treeview (1)
evenrow = "#cce0cc"  # color of even row in treeview

# add test data by hard coding a list of tuples
test_data_list = []
test_data_list.append(("1", "hello", 7000))
test_data_list.append(("2", "data!", 3000))
test_data_list.append(("3", "tests", 3000))
test_data_list.append(("4", "users", 8000))
test_data_list.append(("1", "hello", 6000))
test_data_list.append(("2", "data!", 2000))
test_data_list.append(("3", "tests", 1000))
test_data_list.append(("4", "users", 3000))
test_data_list.append(("1", "hello", 4000))
test_data_list.append(("2", "data!", 5000))
test_data_list.append(("3", "tests", 9000))
test_data_list.append(("4", "users", 7000))

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("900x500")

style = ttk.Style()  # Configure treeview style and colors
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

tree_1_scrollbar = tk.Scrollbar(main_window)  # create a scrollbar and a treeview
tree_1_scrollbar.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree_1 = ttk.Treeview(main_window, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=5, column=5, padx=0, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("col1", "col2", "col3")  # Define treeview columns
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=90)
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W) # Create treeview column headings
tree_1.heading("col1", text="col1 heading", anchor=tk.CENTER)
tree_1.heading("col2", text="col2 heading", anchor=tk.CENTER)
tree_1.heading("col3", text="col3 heading", anchor=tk.CENTER)

tree_1.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors (3)
tree_1.tag_configure('evenrow', background=evenrow)

frame_1 = tk.LabelFrame(main_window, text="this is the label of the label frame")  # Create a label frame
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

empty_entry_button = tk.Button(main_window, text="Click me, I am a button", command=empty_entry)  # Create a button
empty_entry_button.grid(row=0, column=1, padx=padx, pady=pady)

label_1 = tk.Label(frame_1, text="this is a label")  # Create a label
label_1.grid(row=2, column=3, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_1, width=24, justify="right")  # Create an entry
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")

read_table(tree_1)  # read the test data into the treeview

if __name__ == "__main__":
    main_window.mainloop()
