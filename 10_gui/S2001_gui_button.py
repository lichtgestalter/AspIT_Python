"""Vores første GUI: kun én knap i ét vindue.

Kør programmet.
Find ud af, hvad hver række kode gør. For eksempel ved at ændre koden en smule og køre den igen.
Læs alle kommentarerne.
Tag et kort kig på de linkede dokumentationer. Du vil få brug for dem i fremtidige øvelser.
Se youtube-videoen (link i kommentarerne)."""

import tkinter as tk  # import the GUI library

# Define the main window, its title text and its size
# These first 3 lines are typically roughly the same in every tkinter GUI
main_window = tk.Tk()  # create the main window
main_window.title('my first GUI')  # text shown in the top window bar
main_window.geometry("500x500")  # window size

# Create a button
# You can find all possible options of tk.Button() in the following documentations:
# https://tkdocs.com/shipman/button.html
# https://www.tutorialspoint.com/python/tk_button.htm#
button_1 = tk.Button(main_window, text="Click me, I am a button")

# Define where the button is positioned
# Watch this video from 1:48 till 7:03 to understand positioning in tkinter:
# https://www.youtube.com/watch?v=BSfbjrqIw20&t=108s
# You can find all possible options of grid() in the following documentations:
# https://tkdocs.com/shipman/grid.html
# https://www.tutorialspoint.com/python/tk_grid.htm
button_1.grid(row=0, column=1)

# main program
if __name__ == "__main__":  # Executed only when this file is run.
    main_window.mainloop()  # Wait for button clicks and act upon them
