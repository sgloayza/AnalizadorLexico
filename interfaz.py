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
label = tk.Label(win, text="Codigo:")
label.pack()
texto = tk.Text(win,width=50)
texto.pack()









def lexico():
    data = texto.get("1.0","end")
    print(">> "+ data)
    resultado = analisisLexico(data)
    createNewWindow(resultado,"léxico")



def sintaxis():
    s=texto.get("1.0","end-1c").split("\n")
    resultado = analisisSintactico(s)
    print(resultado)
    createNewWindow(resultado, "sintaxis")

btn = tk.Button(win, text="Analizador léxico", command= lexico)
btn.pack()
btn2 = tk.Button(win, text="Analizador sintáctico", command= sintaxis)
btn2.pack()










def createNewWindow(resultado,tipo):
    newWindow = tk.Toplevel(win)
    tk.Label(newWindow, text = "Resultado "+tipo+":").pack();
    if tipo=="léxico":
        for i in resultado:
            tk.Label(newWindow, text = i, anchor="w").pack(fill='both')
    else:
        for i in resultado:
            tk.Label(newWindow, text=i, anchor="w").pack(fill='both')
    btn3 = tk.Button(newWindow, text="Ok", command=newWindow.destroy)
    btn3.pack()








win.mainloop()