# from tkinter import ttk
# import tkinter as tk
# # Crea la ventana principal
# root = tk.Tk()
# root.title("Interfaz culia penca")
# # Crea los widgets de la interfaz de usuario

# # Checkbuttons
# checkbuttons = tk.Checkbutton(root, text="Type here")
# checkbuttons.pack()

# # Radiobuttons
# radiobuttons = tk.Radiobutton(root, text="Kali")
# radiobuttons.pack()

# # Dropdown
# autofocus = tk.OptionMenu(root, "Lens Position", "Auto", "Continuous", "Macro", "Manual")
# autofocus.pack()
# autofocus.place(x=50,y=250)

# # Tabs
# tab_control = ttk.Notebook(root)
# tab_1 = tk.Frame(tab_control)
# tab_2 = tk.Frame(tab_control)
# tab_3 = tk.Frame(tab_control)
# tab_control.add(tab_1, text="Tab 1")
# tab_control.add(tab_2, text="Tab 2")
# tab_control.add(tab_3, text="Tab 3")

# # Botones
# button_1 = tk.Button(root, text="Foto click", height = 5, width=25, background='green')
# button_1.pack()
# button_1.place(x=400,y=500)
# # Otros widgets
# label = tk.Label(root, text="I love it!")
# label.pack()

# # Ajusta el tamaño de la ventana principal
# root.geometry("600x600")

# # Inicia el bucle de eventos
# root.mainloop()

from tkinter import ttk
import tkinter as tk

root = tk.Tk()

for i in range(10):
    root.grid_rowconfigure(i, weight=1)
    for j in range(10):
        root.grid_columnconfigure(j, weight=1)


autofocus = tk.OptionMenu(root, "Lens Position", "Auto", "Continuous", "Macro", "Manual")
autofocus.config(width=10)
autofocus.grid(column=0, row=1)


#   Button

button_1 = tk.Button(root, text="Foto click",  background='green')
button_1.config(width=20, height=5)
button_1.grid(column=8, row=8)

root.geometry("600x600")
root.mainloop()