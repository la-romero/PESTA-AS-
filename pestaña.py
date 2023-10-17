import tkinter as tk
from tkinter import ttk
import webbrowser

def open_link(url):
    webbrowser.open(url)

root = tk.Tk()
root.title("Panel de pestañas")


# Crear el Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10)
class AboutFrame(ttk.Frame):

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Visitanos en 4_A IMEC de guapos")
        self.label.pack()


# Crear las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Saludar")
notebook.add(tab2, text="Acerca de ")


# Crear los botones en la pestaña 1

button1 = ttk.Button(tab1, text="grupo web", command=lambda: open_link("https://github.com/UPP4MA"))
button1.pack(pady=10)
button2 = ttk.Button(tab1, text="classrrom", command=lambda: open_link("https://classroom.google.com/c/NjIzMTgzMDIzNzYw/a/NjMwNjQ5MTExMjU3/details"))
button2.pack(pady=10)

# Crear los botones en la pestaña 2
button3 = ttk.Button(tab2, text="video", command=lambda: open_link("https://www.youtube.com/watch?v=Xgmw_DIvUBQ"))
button3.pack(pady=10)
button4 = ttk.Button(tab2, text="pagina web", command=lambda: open_link("recursospython.com/guias-y-manuales/panel-de-pestanas-notebook-tkinter/"))
button4.pack(pady=10)

root.mainloop()