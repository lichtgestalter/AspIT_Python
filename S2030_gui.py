# Add padding

import tkinter as tk

# global constants
padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects

main_window = tk.Tk()  # Define the main window
main_window.title('my first GUI')  # Text shown in the top window bar
main_window.geometry("500x500")  # window size

# Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
frame = tk.LabelFrame(main_window, text="Container")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define Frame which contains labels, entries and buttons
controls_frame = tk.Frame(frame)
controls_frame.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame = tk.Label(controls_frame)  # Add tuple entry boxes
edit_frame.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for container id
label_id = tk.Label(edit_frame, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_id = tk.Entry(edit_frame, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_id.grid(row=1, column=0, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame = tk.Label(controls_frame)
button_frame.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create = tk.Button(button_frame, text="Create")
button_create.grid(row=0, column=1, padx=padx, pady=pady)

if __name__ == "__main__":  # Executed only when this file is run.
    main_window.mainloop()  # Wait for button clicks and act upon them
