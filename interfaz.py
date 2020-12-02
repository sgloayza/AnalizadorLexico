import sintaxis
import lexico
import tkinter as tk
from lexico import *
from sintaxis import *


win = tk.Tk()

scroll_bar = tk.Scrollbar(win)
scroll_bar.pack(side="right", fill="y")

#Añadiendo un titulo a nuestra ventana principal
win.title("Analizador lexico")
#Dimensiones en pixeles de nuestra ventana principal
win.geometry('500x500')
label = tk.Label(win, text="Codigo:")
label.pack()
texto = tk.Text(win,width=50,yscrollcommand = scroll_bar.set)
texto.pack()







def lexico():
    data = texto.get("1.0","end")
    print(">> "+ data)
    resultado = analisisLexico(data)
    createNewWindow(resultado,"léxico")

def sintaxis():
    s=texto.get("1.0","end-1c")
    resultado = analisisSintactico(s)
    createNewWindow(resultado, "sintaxis")

btn = tk.Button(win, text="Analizador léxico", command= lexico)
btn.pack()
btn2 = tk.Button(win, text="Analizador sintáctico", command= sintaxis)
btn2.pack()


scroll_bar.config( command = texto.yview )







def createNewWindow(resultado,tipo):
    newWindow = tk.Toplevel(win)



    labelTitulo = tk.Label(newWindow, text = "Resultado "+tipo+":")
    labelTitulo.pack()

    if tipo=="léxico":
        for i in resultado:
            LabelRespuesta = tk.Label(newWindow, text = i, anchor="w").pack(fill='both')
    else:
        if len(resultado)==0:
            LabelRespuesta = tk.Label(newWindow, text="No hay errores sintácticos", anchor="w").pack(fill='both')
        else:
            for i in resultado:
                LabelRespuesta = tk.Label(newWindow, text=i, anchor="w").pack(fill='both')

    btn3 = tk.Button(newWindow, text="Ok", command=newWindow.destroy)
    btn3.pack()








win.mainloop()