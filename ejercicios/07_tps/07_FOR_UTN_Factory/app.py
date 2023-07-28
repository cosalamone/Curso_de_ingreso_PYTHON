'''
Nombre: Constanza 
Apellido: Salamone

UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        total_postulantes = 10

        contador = 0
        menor_edad = None

        acumulador_edades_f = 0
        acumulador_edades_m = 0
        acumulador_edades_nb = 0

        contador_f = 0
        contador_m = 0
        contador_nb = 0

        contador_aspnet = 0
        contador_js = 0
        contador_python = 0 

        mensaje = ''

    # A Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.

        for i in range(total_postulantes):
            nombre = prompt('UTN', 'Ingrese el nombre')
            edad = int(prompt('UTN', 'Ingrese la edad')) #
            genero = prompt('UTN', 'Ingrese el genero (F-M-NB)') #
            tecnologia = prompt('UTN', 'Ingrese la tecnologia (PYTHON - JS - ASP.NET)') # 
            puesto = prompt('UTN', 'Ingrese el puesto (Jr - Ssr - Sr)') #

            if genero == 'NB' and (tecnologia == 'JS' or tecnologia == 'ASP.NET') and (edad >= 25 and edad <= 40) and puesto == 'Ssr':
                contador += 1 
                mensaje += f'A: La cantidad de postulantes, no binario que trabajan con ASP.NET o JS, y su edad es entre 25 y 40 años, y su puesto es Ssr es: {contador}. \n'    
    # B. Nombre del postulante Jr con menor edad.
            if puesto == 'Jr' and (menor_edad == None or edad < menor_edad):
                menor_edad = edad
                jr_menor_edad = nombre

                mensaje += f'B: El postulante Jr de menor edad es: {jr_menor_edad} \n'

    # C Promedio de edades por género.
            if genero == 'F':
                acumulador_edades_f += edad
                contador_f += 1
            else:
                if genero == 'M':
                    acumulador_edades_m += edad
                    contador_m += 1
                else:
                    acumulador_edades_nb += edad
                    contador_nb += 1


        if contador_f != 0:
            promedio_femenino = acumulador_edades_f/contador_f

        if contador_m != 0:
            promedio_masculino = acumulador_edades_m / contador_m

        if contador_nb != 0:
            promedio_nb = acumulador_edades_nb / contador_nb
        
        mensaje +=f'C: edades femeninas: {promedio_femenino}, edades masculinas: {promedio_masculino}, edades nob: {promedio_nb} \n'

        


    #D. Tecnologia con mas postulantes (solo hay una).
        if tecnologia == 'JS':
            contador_js += 1
        else: 
            if tecnologia == 'ASP.NET':
                contador_aspnet += 1 
            else:
                if tecnologia == 'PYTHON':
                    contador_python += 1
            
        if contador_js > contador_aspnet and contador_js > contador_python:
            mensaje +=  'D: JS es la tecnología con más postulantes \n'
        else:
            if contador_aspnet> contador_python:
                mensaje +=  'D: ASP.NET es la tecnología con más postulantes\n'
            else:
                mensaje +=  'D: PYTHON es la tecnología con más postulantes\n'
        

    # E Porcentaje de postulantes de cada genero.
        poncentaje_femenimo = (contador_f *  100) /total_postulantes
        porcentaje_masculino = (contador_m * 100 ) /total_postulantes
        porcentaje_nb = (contador_nb * 100 ) /  total_postulantes


        mensaje +=f'E: El porcentaje de mujeres es:{poncentaje_femenimo} , el de hombres es: {porcentaje_masculino}, el de no binario es: {porcentaje_nb}\n'

        print(mensaje)



            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
