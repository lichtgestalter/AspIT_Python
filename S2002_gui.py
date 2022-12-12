"""
Now there are more buttons, a label and an entry.

Find out what every row of code does. For example by changing the code a bit and running it again.
Read all the comments.
Play around with the row and column parameters of grid() in order to understand grid() better.
Have a short look at the linked documentations for Entry and Label. You will need them in future exercises.

"""
import tkinter as tk  # import the GUI library

main_window = tk.Tk()  # create the main window
main_window.title('my first GUI')  # text shown in the top window bar
main_window.geometry("500x500")  # window size

# create some buttons
button_1 = tk.Button(main_window, text="Click me, I am a button")  # create a button
button_1.grid(row=0, column=1)  # define where the button is positioned
button_2 = tk.Button(main_window, text="button_2")
button_2.grid(row=1, column=1)
button_3 = tk.Button(main_window, text="button_3")
button_3.grid(row=2, column=1)
button_4 = tk.Button(main_window, text="button_4")
button_4.grid(row=3, column=3)
button_5 = tk.Button(main_window, text="lower right button")
button_5.grid(row=117, column=117)

# create a label
# find all possible options of tk.Label() in the following documentations:
# https://tkdocs.com/shipman/label.html
# https://www.tutorialspoint.com/python/tk_label.htm
label_1 = tk.Label(main_window, text="this is a label")
label_1.grid(row=2, column=3)

# create an entry
# find all possible options of tk.Entry() in the following documentations:
# https://tkdocs.com/shipman/entry.html
# https://www.tutorialspoint.com/python/tk_entry.htm
entry_1 = tk.Entry(main_window, width=24, justify="right")
entry_1.grid(row=1, column=2)
entry_1.insert(0, "This is an entry. Edit me!")


if __name__ == "__main__":  # Executed only when this file is run.
    main_window.mainloop()  # Wait for button clicks and act upon them
