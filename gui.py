from lexico import *
import tkinter as tk


win = tk.Tk()
#Añadiendo un titulo a nuestra ventana principal
win.title("Analizador lexico")
#Dimensiones en pixeles de nuestra ventana principal
win.geometry('400x400')
lbl = tk.Label(win, text="Codigo:")
lbl.pack()
txt = tk.Entry(win,width=10)
txt.pack()
def prueba():
    print("Hola",txt.get())
btn = tk.Button(win, text="Analizador lexico", command=prueba)
btn.pack()
btn1 = tk.Button(win, text="Analizador sintactico", command=prueba)
btn1.pack()


win.mainloop()