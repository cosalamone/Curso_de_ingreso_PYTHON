import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Constanza 
Apellido: Salamone

Al presionar el botón 'MÍNIMO' se analizará el vector lista_datos a efectos de determinar cuál es el número 
más chico allí contenido el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÍNIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,-10,15,-5,1,79]


    def btn_calcular_on_click(self):
        numero_minimo = True

        for i in range(len(self.lista_datos)):
            numero= self.lista_datos[i]
            if numero_minimo == True or numero_minimo > numero:
                numero_minimo = numero

        alert('utn', f'El numero más chico es: {numero_minimo}')
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()