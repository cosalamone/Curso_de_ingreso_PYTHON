import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Constanza
Apellido: Salamone

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre_cantidato_con_menos_votos= ''
        edad_con_menos_votos = 0
        votos_maximos = 0 
        votos_minimos = None
        acumulador_edades = 0 
        contador = 0 
        acumulador_votos = 0 

        flag = True 

        while flag == True:
            
            nombre = prompt(title='utn', prompt='Ingrese el nombre del candidato')

            edad = prompt(title='utn', prompt='Ingrese la edad del candidato, debe ser mayor a 25')
            edad= int(edad)
            while edad <= 25:
                edad = prompt(title='utn', prompt='Ingrese la edad del candidato, debe ser mayor a 25')
                edad= int(edad)
                

            cantidad_votos = prompt(title='utn', prompt='Ingrese la cantidad de votos')
            cantidad_votos= int(cantidad_votos)
            
            while cantidad_votos < 0: 
                cantidad_votos = prompt(title='utn', prompt='La cantidad de votos debe ser igual o menos a cero)')
                cantidad_votos= int(cantidad_votos)

            if cantidad_votos > votos_maximos: 
                nombre_cantidato_con_mayores_votos = nombre
                votos_maximos = cantidad_votos
                #edad_con_mas_votos = edad

            if votos_minimos == None : # para que no rompa la primera vez 
                votos_minimos = cantidad_votos
            else:
                if votos_minimos > cantidad_votos:
                    votos_minimos = cantidad_votos
                    nombre_cantidato_con_menos_votos = nombre
                    edad_con_menos_votos = edad

            acumulador_edades += edad
            contador += 1

            acumulador_votos += cantidad_votos

            
            rta = question(title='utn', message='¿Desea ingresar un nuevo candidato?')
            if rta == False:
                flag = False

        if contador != 0:
            promedio_edades = acumulador_edades / contador

        print(f'''(A)El candidato con mas cantidad de votos es {nombre_cantidato_con_mayores_votos}. (B)El cantidato con menos votos es: {nombre_cantidato_con_menos_votos} y su edad es {edad_con_menos_votos}. (C) El promedio de edades es: {promedio_edades}. (D) La cantidad de votos emitidos es {acumulador_votos}''')
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
