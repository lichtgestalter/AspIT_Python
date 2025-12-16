"""Der er blevet tilføjet en frame.

Kør programmet.
Find ud af, hvad hver række af kode gør. F.eks. ved at ændre koden en smule og køre den igen.
Især skift de overordnede vinduer for GUI-objekterne mellem frame_1
og main_window og leg med værdierne for padx og pady.
Læs alle kommentarerne.
Tag et kort kig på de linkede dokumentationer for Frame. Du vil få brug for dem i fremtidige øvelser."""

import tkinter as tk

padx = 8
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create a frame
# A frame is an (invisible) subwindow with its own grid.
# Frames are used to organize the positioning of GUI objects that belong to this frame.
# You can find all possible options of tk.Frame() in the following documentations:
# https://tkdocs.com/shipman/frame.html
# https://www.tutorialspoint.com/python/tk_frame.htm
frame_1 = tk.Frame(main_window)
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

# Create a button
button_1 = tk.Button(main_window, text="Click me, I am a button")
button_1.grid(row=0, column=1, padx=padx, pady=pady)

# Create a label
# when defining a GUI object the first argument is always the name of the parent window.
# we changed the parent window of label_1 and entry_1 from main_window to frame_1.
label_1 = tk.Label(frame_1, text="this is a label")
label_1.grid(row=2, column=3, padx=padx, pady=pady)  # this position now refers to frame_1 instead of main_window.

# Create an entry
entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")


if __name__ == "__main__":
    main_window.mainloop()
