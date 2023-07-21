import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        '''
        Enunciado:
        Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
        quiera hasta que presione el botón Cancelar (en el prompt). 
        Luego calcular:
            La suma acumulada de los negativos
            La suma acumulada de los positivos
            Cantidad de números positivos ingresados
            Cantidad de números negativos ingresados
            Cantidad de ceros
            Diferencia entre la cantidad de los números positivos ingresados y los negativos

        Informar los resultados mediante alert()
        '''

    def btn_comenzar_ingreso_on_click(self):
        acumulado_negativos = 0
        acumulado_positivos = 0
        contador_positivos = 0 
        contador_negativos = 0
        contador_ceros = 0


        flag = True

        while flag == True:
            numero = prompt(title='utn', prompt='ingrese un numero')
                    
            if numero == None:
                break

            else:
                numero = int(numero)

                if numero < 0:
                    acumulado_negativos += numero
                    contador_negativos += 1
                else:
                    if numero > 0:
                        acumulado_positivos += numero
                        contador_positivos += 1
                    else:
                        contador_ceros += 1
        
        diferencia_contador_entre_p_y_n = contador_positivos - contador_negativos

        alert('utn', f''' La suma acumulada de los negativos es de: {acumulado_negativos}
        La suma acumulada de los positivos es de: {acumulado_positivos}
        Cantidad de números positivos ingresados es de: {contador_positivos}
        Cantidad de números negativos ingresados es de: {contador_negativos}
        Cantidad de ceros es de: {contador_ceros}
        Diferencia entre la cantidad de los números positivos ingresados y los negativos es de: {diferencia_contador_entre_p_y_n}''' )
                    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
