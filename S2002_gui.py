"""
now there are more buttons, a label and an entry.

xFind out what every row of code does. For example by changing the code a bit and running it again.
xRead all the comments.
xHave a short look at the linked documentations.
xWatch the youtube video.

play around with the row and column options of grid() in order to understand grid() better
"""
import tkinter as tk  # import the GUI library

# Define the main window, its title text and its size
# These first 3 lines are typically roughly the same in every tkinter GUI
main_window = tk.Tk()  # create the main window
main_window.title('my first GUI')  # text shown in the top window bar
main_window.geometry("500x500")  # window size

# create a button
# find all possible options of tk.Button() in the following documentations:
# https://tkdocs.com/shipman/button.html
# https://www.tutorialspoint.com/python/tk_button.htm#
button_1 = tk.Button(main_window, text="Click me, I am a button")

# define where the button is positioned
# watch this video from 1:48 till 7:03 to understand positioning in tkinter:
# https://www.youtube.com/watch?v=BSfbjrqIw20&t=108s
# find all possible options of grid() in the following documentations:
# https://tkdocs.com/shipman/grid.html
# https://www.tutorialspoint.com/python/tk_grid.htm
button_1.grid(row=0, column=1)


if __name__ == "__main__":  # Executed only when this file is run.
    main_window.mainloop()  # Wait for button clicks and act upon them
