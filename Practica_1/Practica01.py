# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:13:53 2021

@author: waldo
"""
from tkinter import *
import numpy as np


#Funcion para calcular
def calcular_ecus():
    
    #Alojar vairbales obtenidas de la ecuacion 1
    x1 = coex1.get()
    y1 = coey1.get()
    dep1 = coedep1.get()
    #Alojar vairbales obtenidas de la ecuacion 2
    x2 = coex2.get()
    y2 = coey2.get()
    dep2 = coedep2.get()
    #Usar los datos para generar matrices con los datos de x, y, terminos indep
    A = np.matrix([[x1, y1],[x2, y2]])
    b = np.matrix([[dep1],[dep2]])
    if np.linalg.det(A) == 0:
        x = None
        print("No se puede resolver")
        ed_label=Label(text="No se puede resolver" , bg= "#BC9EC1", font = ("Cambria",16))
        ed_label.place(x= 22, y =440)
    else:
        #obtencion de la matris resultante == valortes de x , y
        x = (A**-1)*b
        print("x=",x[0],"\t","y=", x[1])
        #Labels de los resultados
        t1 ="Resultado de X = %d"%x[0]
        ed_label=Label(text=t1 , bg= "#BC9EC1", font = ("Cambria",16))
        ed_label.place(x= 22, y =440)
        t2 = "Resultado de Y = %d"%x[1]
        ed_label=Label(text=t2, bg= "#BC9EC1", font = ("Cambria",16))
        ed_label.place(x= 222, y =440)
    
        

ventana =Tk()
ventana.geometry("650x550")
ventana.title("Programa de ecuaciones Python")
ventana.resizable(False,False)
ventana.config(background = "#272D2D")

main_title = Label(text="SISTEMA DE ECUACIONES",font = ("Cambria",18), bg = "#BC9EC1", fg= "white", width="500", height="2" )
main_title.pack()


nombre_label=Label(text="Primera Ecuacion", bg= "#BC9EC1", font = ("Cambria",16))
nombre_label.place(x= 22, y =100)
nombre_X_label_1=Label(text="Coeficiente de X", bg= "#BC9EC1", font = ("Cambria",12))
nombre_X_label_1.place(x= 22, y =160)
nombre_Y_label_1=Label(text="Coeficiente de Y", bg= "#BC9EC1", font = ("Cambria",12))
nombre_Y_label_1.place(x= 225, y =160)
nombre_I_label_1=Label(text="Termino Idependiente", bg= "#BC9EC1", font = ("Cambria",12))
nombre_I_label_1.place(x= 425, y =160)

ed_label=Label(text="Segunda Ecuacion", bg= "#BC9EC1", font = ("Cambria",16))
ed_label.place(x= 22, y =210)
nombre_X_label_1=Label(text="Coeficiente de X", bg= "#BC9EC1", font = ("Cambria",12))
nombre_X_label_1.place(x= 22, y =280)
nombre_Y_label_1=Label(text="Coeficiente de Y", bg= "#BC9EC1", font = ("Cambria",12))
nombre_Y_label_1.place(x= 225, y =280)
nombre_I_label_1=Label(text="Termino Idependiente", bg= "#BC9EC1", font = ("Cambria",12))
nombre_I_label_1.place(x= 425, y =280)

#Variables de la primera ecuacion
coex1 = IntVar()
coey1 = IntVar()
coedep1 = IntVar()


#variables de la segunda ecacuion
coex2 = IntVar()
coey2 = IntVar()
coedep2 = IntVar()

#Entrada de ecuacion 1
coex1_entry = Entry(textvariable=coex1,width="3",font = ("Cambria",12))
coey1_entry = Entry(textvariable=coey1,width="3",font = ("Cambria",12))
coedep1_entry = Entry(textvariable=coedep1,width="3",font = ("Cambria",12))

#mostrar entradas de ecuacion 1
coex1_entry.place(x=150, y =160)
coey1_entry.place(x=353, y =160)
coedep1_entry.place(x=593, y =160)

#Entrada de ecuacion 2
coex2_entry = Entry(textvariable=coex2,width="3",font = ("Cambria",12))
coey2_entry = Entry(textvariable=coey2,width="3",font = ("Cambria",12))
coedep2_entry = Entry(textvariable=coedep2,width="3",font = ("Cambria",12))

#mostrar entradas de ecuacion 2
coex2_entry.place(x=150, y =280)
coey2_entry.place(x=353, y =280)
coedep2_entry.place(x=593, y =280)

#boton para calcular
calc_btn = Button(ventana, text = "Calcular", width="30", height= "2", command=calcular_ecus, bg="#D68FD6")
#mostrar boton
calc_btn.place(x=160,y=355)

ventana.mainloop()