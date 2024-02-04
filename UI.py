from tkinter import ttk
import tkinter as tk

root = tk.Tk()


for i in range(10):
    root.grid_rowconfigure(i, weight=1)
    for j in range(10):
        root.grid_columnconfigure(j, weight=1)


label_iso =  tk.Label(root,text = "ISO")
label_iso.grid(column=1, row = 0)

entry_iso = ttk.Entry(root)
entry_iso.config(width=10)
entry_iso.grid(column=2, row = 0)

label_shspeed =  tk.Label(root,text = "Shutter speed")
label_shspeed.grid(column=1, row = 1)

entry_shspeed = ttk.Entry(root)
entry_shspeed.config(width=10)
entry_shspeed.grid(column=2, row = 1)


label_gain =  tk.Label(root,text = "Gain")
label_gain.grid(column=1, row = 2)

entry_gain = ttk.Entry(root)
entry_gain.config(width=10)
entry_gain.grid(column=2, row = 2)

label_lposition =  tk.Label(root,text = "Lens position")
label_lposition.grid(column=1, row = 3)

lposition_selector = tk.OptionMenu(root, "Auto", "Continuous", "Macro", "Manual")
lposition_selector.config(width=10)
lposition_selector.grid(column=2, row=3)


#   Button

button_1 = tk.Button(root, text="Foto click",  background='green' , fg="white")
button_1.config(width=20, height=5)
button_1.grid(column=8, row=8)

root.geometry("600x600")
root.mainloop()
