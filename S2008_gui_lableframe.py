"""
The frame has been replaced by a label frame.

Run the program.
Read all the comments.
Find out what every row of code does. For example by changing the code a bit and running it again.
Especially switch the parent windows of the GUI objects between frame_1
and main_window and play with the values of padx and pady.
"""
import tkinter as tk

padx = 8
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create a label frame
# A label frame is used like a frame but its borders are visible
# and on the border is placed a label.
# Find all possible options of tk.LabelFrame() in the following documentations:
# https://tkdocs.com/shipman/labelframe.html
# https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_1 = tk.LabelFrame(main_window, text="this is the label of the label frame")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

# Create a button
button_1 = tk.Button(main_window, text="Click me, I am a button")
button_1.grid(row=0, column=1, padx=padx, pady=pady)

# Create a label
label_1 = tk.Label(frame_1, text="this is a label")
label_1.grid(row=2, column=3, padx=padx, pady=pady)

# Create an entry
entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")


if __name__ == "__main__":
    main_window.mainloop()
