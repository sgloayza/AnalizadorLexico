import sintaxis
import lexico
import tkinter as tk
from lexico import *
from sintaxis import *



win = tk.Tk()
#Añadiendo un titulo a nuestra ventana principal
win.title("Analizador lexico")
#Dimensiones en pixeles de nuestra ventana principal
win.geometry('500x500')
lbl = tk.Label(win, text="Codigo:")
lbl.pack()
txt = tk.Text(win,width=50)
txt.pack()

def prueba():
    s=txt.get("1.0","end-1c")
    result = parser.parse(s)
    print(result)

def prueba2():
    x = txt.get("1.0","end-1c")
    for linea in x:
        print(">>" + linea)
        analizar(linea)
        if len(linea) == 0:
            break

btn = tk.Button(win, text="Analizador lexico", command= prueba2)
btn.pack()
btn2 = tk.Button(win, text="Analizador sintactico", command= prueba)
btn2.pack()


win.mainloop()