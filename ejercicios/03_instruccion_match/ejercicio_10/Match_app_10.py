import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Constanza
Apellido: Salamone

Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar un alert con el mensaje “Se viaja”, 
caso contrario mostrar “No se viaja”. 
    Si es invierno: solo se viaja a Bariloche
    Si es verano: se viaja a Mar del plata y Cataratas
    Si es otoño: se viaja a todos los lugares
    Si es primavera: se viaja a todos los lugares menos Bariloche
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    '''
    Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
    En caso de hacerlo mostrar un alert con el mensaje “Se viaja”, 
    caso contrario mostrar “No se viaja”. 
        Si es invierno: solo se viaja a Bariloche
        Si es verano: se viaja a Mar del plata y Cataratas
        Si es otoño: se viaja a todos los lugares
        Si es primavera: se viaja a todos los lugares menos Bariloche
    '''
    def btn_informar_on_click(self):
        estacion = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()

        match(estacion):
            case 'Invierno':
                if destino == 'Bariloche':
                    alert(title='utn', message='Se viaja')
                else: 
                    alert(title='utn', message='Sólo se viaja a Bariloche')
            case 'Verano':
                if destino == 'Mar del planta' or destino == 'Cataratas':
                    alert(title='utn', message='Sólo se viaja a Bariloche')
                else:
                    alert(title='utn', message='Se viaja a Mar del plata y Cataratas')
            case 'Otoño':
                alert(title='utn', message='Se viaja a todos los lugares')
            case 'Primavera':
                if destino != 'Bariloche':
                    alert(title='utn', message='Se viaja')
                else:
                    alert(title='utn', message='Se viaja a todos los lugares menos Bariloche')
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()