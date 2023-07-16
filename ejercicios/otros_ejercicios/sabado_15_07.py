import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

# ENUNCIADO:
# Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


# 1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

# 2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
# medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

# 3- validar todos los datos

# 4- en las vacaciones se pueden seleccionar distintas excursiones para realizar , 
# se pueden hacer desde 0 excursión a 11 excursiones

# 5- una vez ingresada la cantidad se debe pedir por cada excursión 
# el importe y el tipo de excursión(caminata  o vehículo). 
# informar cual es el precio más caro el más barato y el promedio

# 6- informar cual es el tipo de excursión(caminata  o vehículo). 
# más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_mostrar_on_click(self):
# validamos no sea un none, rango de valores, cantidad de caracteres
        nombre = prompt(title='utn', prompt='Ingrese su nombre')
        while nombre == None or nombre.isdigit() or len(nombre) < 3: # isdigit() devuelve true cuando son sólo numeros - si es alfanmerico devuelve False
            nombre = prompt(title='utn', prompt='Ingrese su nombre')


        edad = prompt(title='utn', prompt='Ingrese su edad')
        while edad == None or not edad.isdigit() or int(edad) < 1 or int(edad) > 100 :
            edad = prompt(title='utn', prompt='Ingrese su edad')
        edad = int(edad)

        genero = prompt(title='utn', prompt='Ingrese su genero ("femenino", "masculino", "otro")')
        while genero == None or genero.isdigit() or genero != "femenino" and genero != "masculino" and genero != "otro":
            genero = prompt(title='utn', prompt='Ingrese su genero ("femenino", "masculino", "otro")')


        mensaje= f'usted es {nombre} tiene {edad} de edad y su género es {genero}'

        alert('utn', message=mensaje)

#2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
# medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

        altura = prompt(title='utn', prompt='Ingrese su altura en cm')
        while altura == None or not altura.isdigit():
            altura = prompt(title='utn', prompt='Ingrese su altura en cm')

        altura = int(altura)

        if altura < 140:  # Estructura de control
            tipo_altura = 'bajo'
        else: 
            if  altura <= 170: # no enamorarse de and --> if ((altura  >= 140 and )) altura <= 170
                tipo_altura= 'medio'
            else: 
                if  altura <= 190:
                    tipo_altura = 'alto'
                else: 
                    tipo_altura = 'muy alto'
        
        mensaje = f'Usted es {tipo_altura}'
        alert(title='utn', message=mensaje)

        #CON ELIF
                # if altura < 140:  # Estructura de control
                #     tipo_altura = 'bajo'
                # elif altura <= 170:
                #     tipo_altura= 'medio'
                # elif altura <= 170:
                #     tipo_altura = 'alto'
                # else: 
                #     tipo_altura = 'muy alto'



        
    



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()