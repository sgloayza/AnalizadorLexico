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
    s=txt.get("1.0","end")
    parser.parse(s)
    createNewWindow()

def prueba2():
    x = txt.get("1.0","end")
    print(">>" + x)
    analizar(x)
    createNewWindow()


btn = tk.Button(win, text="Analizador lexico", command= prueba2)
btn.pack()
btn2 = tk.Button(win, text="Analizador sintactico", command= prueba)
btn2.pack()

def createNewWindow():
    newWindow = tk.Toplevel(win)
    labelTitulo = tk.Label(newWindow, text = "Resultado:")
    label = tk.Label(newWindow, text ="")
    labelTitulo.pack()
    label.pack()

win.mainloop()