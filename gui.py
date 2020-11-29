import sintaxis
import lexico
import tkinter as tk
from lexico import *
from sintaxis import *


win = tk.Tk()
win2 = tk.Tk()
#Añadiendo un titulo a nuestra ventana principal
win.title("Analizador lexico")
#Dimensiones en pixeles de nuestra ventana principal
win.geometry('500x500')
lbl = tk.Label(win, text="Codigo:")
lbl.pack()
txt = tk.Text(win,width=50)
txt.pack()

def lexico():
    x = txt.get("1.0","end")
    print(">>" + x)
    resultado = analizar(x)
    createNewWindow(resultado)

def sintaxis():
    s=txt.get("1.0","end")
    resultado = parser.parse(s)

    print(resultado)

btn = tk.Button(win, text="Analizador lexico", command= lexico)
btn.pack()
btn2 = tk.Button(win, text="Analizador sintactico", command= sintaxis)
btn2.pack()

def createNewWindow(resultado):
    newWindow = tk.Toplevel(win)
    tk.Label(newWindow, text = "Resultado:").pack()
    label = tk.Label(newWindow)
    for i in resultado:
        tk.Label(newWindow, text = i).pack()
    btn3 = tk.Button(newWindow, text="Ok", command=newWindow.destroy)
    btn3.pack()
    label.pack()

win.mainloop()