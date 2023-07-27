import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
ATAJOS Y OTROS

** SHIFT + TAB para 'destabear'

** print(f'El promedio de edad de platea es {promedio:.1f}') 

############################################################################################################

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

############################################################################################################

ANOTACIONES TEMAS

----------------------- FOR = FOREACH -----------------------
Realiza iteraciones sobre una variable iterable (ej: un string, listas, tuplas, range etc)
No tiene la posibilidad de hacer bucles infinitos

    numeros = [1,2,3,4,9]
    for numero in numeros:
        pring(numero / numeros[numero])



-------------------------- LISTAS -------------------------
*** RANGE() ***
range() funcion que devuelve algo similar a una lista, es un itebrale 
Crea una secuencia de numeros que por dafult inicia en 0 y se incrementa de a 1. Finaliza antes del número indicado en el stop
    ej: range(8) --> devuelve un iterable de 8 elementos--> del 0 al 7 // range(0 , 9 , 2)
0= desde donde inicia (por default inicia en 0)
9= la cantidad de iterables
2= step: cada cuanto itera(cada cuanto salta) (por default salta de a 1)

Para que vaya en forma decreciente seria: 
    range(100, 1, -1) --> el -1 le indica que va restando de a 1



alumnos = ['Juan', 'Pedro', 'Marta'] // Permite guardar muchos datos en una sola variable

for i in range(len(alumnos)): # sirve para usar varias listas a la par
    print(i) --> las posiciones --> 0 1 2
    print(alumnos[i]) --> obtengo la info de cada posicion -->  'Juan' 'Pedro' 'Marta'

    
*** APPEND() ***
    self.lista_datos.append(numero) --> Funciona como el .push() de JS
Agrega un elemento al final de la lista


*** CLEAR() ***
    self.lista_datos.clear() --> Para que no se agregue al final de la lista lo nuevo que quiero 
                                agregar, lo borro y luego hago el append()


*** INSERT() *** --> no lo usamos // dato para la vida //
    self.lista_datos.insert( P(posicion) , E(numero)) --> inserta un elemento en la posicion que quiera
    self.lista_datos.insert(2, 45) --> lista_datos = [6 , 4 , (45), 9 , 4] (el 45 es el nuevo, el 9 es el 
                                    que antes estaba en la posicion 2 y lo desplazó a la 3 --> no lo sobreescribe)
                                    Si la posicion en la que le indico que lo agregue no existe, lo agrega al final de la lista
'''
alumnos = ['Juan', 'Pedro', 'Marta'] # [0, 1, 2] - permite mezclar tipos de datos

