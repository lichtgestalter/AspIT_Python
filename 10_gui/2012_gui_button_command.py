"""Der er defineret en funktion empty_entry(), som kaldes ved at trykke på en knap.

Kør programmet.
Læs alle kommentarerne.
Find ud af, hvad hver række kode gør. F.eks. ved at ændre koden en smule og køre den igen.

Vær særlig opmærksom på, hvordan funktionen empty_entry() kaldes, og hvordan teksten i indtastningsfeltet entry_1 tømmes."""

import tkinter as tk


def empty_entry():
    print("button_1 was pressed")
    entry_1.delete(0, tk.END)  # Delete text in the entry box, beginning with the first character (0) and ending with the last character (tk.END)


padx = 8
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create a label frame
frame_1 = tk.LabelFrame(main_window, text="this is the label of the label frame")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

# Create a button
# The parameter command of tk.Button specifies the name of the function to be called by clicking this button.
# The button has now a name that relates to its functionality. This makes it easier to understand the code.
empty_entry_button = tk.Button(main_window, text="Click me, I am a button", command=empty_entry)
empty_entry_button.grid(row=0, column=1, padx=padx, pady=pady)

# Create a label
label_1 = tk.Label(frame_1, text="this is a label")
label_1.grid(row=2, column=3, padx=padx, pady=pady)

# Create an entry
entry_1 = tk.Entry(frame_1, width=24, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")


if __name__ == "__main__":
    main_window.mainloop()
