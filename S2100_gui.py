import tkinter as tk
from tkinter import ttk

# region global constants
padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects









# endregion global constants


# region common widgets
main_window = tk.Tk()  # Define the main window
main_window.title('my first GUI')  # Text shown in the top window bar
main_window.geometry("500x500")  # window size

style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme





# endregion common widgets

# region container widgets
# Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
frame_container = tk.LabelFrame(main_window, text="Container")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm























# Define Frame which contains labels, entries and buttons
controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_container = tk.Label(controls_frame_container)  # Add tuple entry boxes
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for container id
label_container_id = tk.Label(edit_frame_container, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)
















# Define Frame which contains buttons
button_frame_container = tk.Label(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_container = tk.Button(button_frame_container, text="Create")
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)







# endregion container widgets

if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    main_window.mainloop()  # Wait for button clicks and act upon them
