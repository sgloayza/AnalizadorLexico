import sintaxis
import lexico
import tkinter
from tkinter import *
from lexico import *
from sintaxis import *


win = Tk()

scroll_bar = Scrollbar(win)
scroll_bar.pack(side="right", fill="y")

win.title("Analizador léxico y sintáctico")
win.geometry('500x500')

label = Label(win, text="Código")
label.pack()
texto = Text(win,width=50,yscrollcommand = scroll_bar.set)
texto.pack()







def lexico():
    data = texto.get("1.0","end")
    resultado = analisisLexico(data)
    createNewWindow(resultado,"léxico")     #resultado es lista de tokens

def sintaxis():
    data=texto.get("1.0","end-1c")
    resultado = analisisSintactico(data)
    createNewWindow(resultado,"sintáctico")    #resultado es lista de errores

btn = Button(win, text="Analizador léxico", command= lexico)
btn.pack()
btn2 = Button(win, text="Analizador sintáctico", command= sintaxis)
btn2.pack()


scroll_bar.config( command = texto.yview )





def createNewWindow(resultado,tipo):
    root = Toplevel(win)
    root.title("Resultado "+tipo)

    mylabel = Label(root)
    mylabel.grid()

    text = Text(mylabel, height=30, width=60)
    text.grid(row=0, column=0)

    scrollbar = Scrollbar(mylabel,command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="NSEW")

    if(tipo=="léxico"):
        print("_______________________ANALISIS LÉXICO___________________________\n")
        if len(resultado) == 0: resultado.append("No hay tokens")
        for i in resultado:
            text.insert(END, i)
            text.insert(END, "\n")
            print(i)
        print("\n_________________________________________________________________\n")
    else:
        print("_______________________ANALISIS SINTÁCTICO_______________________\n")
        if len(resultado)==0: resultado.append("No hay errores sintácticos")
        for i in resultado:
            text.insert(END, i)
            text.insert(END, "\n")
            print(i)
        print("\n__________________________________________________________________\n")


    root.mainloop()






win.mainloop()