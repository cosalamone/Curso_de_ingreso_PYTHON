import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
ESTRUCTURA GRAL 

# INICIALICACIONES
    acumulador_edad = 0


    while ture:
        #INGRESO DE DATOS Y VALIDACIONES
        edad = prompt()
        # Validacion de edad

        # Procesos
        acumulador_edad += edad


# SALIDA DE DATOS



--------------------- FOR = FOREACH ---------------------
Realiza iteraciones sobre una variable iterable (ej: un string, listas, tuplas, etc)
No tiene la posibilidad de hacer bucles infinitos

    numeros = [1,2,3,4,9]
    for numero in numeros:
        pring(numero / numeros[numero])



--------------------- LISTAS ---------------------
range() funcion que devuelve algo similar a una lista, es un itebrale 
    ej: range(8) --> devuelve un iterable de 8 elementos--> del 0 al 7 // range(0 , 9 , 2)
0= desde donde inicia (por default inicia en 0)
9= la cantidad de iterables
2= step: cada cuanto itera(cada cuanto salta) (por default salta de a 1)

Para que vaya en forma decreciente seria: 
    range(100, 1, -1) --> el -1 le indica que va restando de a 1



alumnos = ['Juan', 'Pedro', 'Marta'] // Permite guardar muchos datos en una sola variable

'''
alumnos = ['Juan', 'Pedro', 'Marta'] # [0, 1, 2] - permite mezclar tipos de datos

