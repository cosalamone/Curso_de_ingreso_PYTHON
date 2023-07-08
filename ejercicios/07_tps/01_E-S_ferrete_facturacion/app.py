import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Constanza
Apellido: Salamone

Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)

        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        importe_uno_str = self.txt_importe_1.get()
        importe_dos_str = self.txt_importe_2.get()
        importe_tres_str = self.txt_importe_3.get()

        importe_uno = float(importe_uno_str)
        importe_dos = float(importe_dos_str)
        importe_tres = float(importe_tres_str)

        resultado = importe_uno + importe_dos + importe_tres

        alert(title='Suma de los productos', message=f'El precio total por los tres productos es: {resultado}')

    def btn_promedio_on_click(self):
        importe_uno_str = self.txt_importe_1.get()
        importe_dos_str = self.txt_importe_2.get()
        importe_tres_str = self.txt_importe_3.get()

        importe_uno = float(importe_uno_str)
        importe_dos = float(importe_dos_str)
        importe_tres = float(importe_tres_str)

        promedio = (importe_uno + importe_dos + importe_tres) / 3

        alert(title='Promedio de los productos', message=f'El promedio de los 3 productos es: {promedio:.2f}')

    def btn_total_iva_on_click(self):
        importe_uno_str = self.txt_importe_1.get()
        importe_dos_str = self.txt_importe_2.get()
        importe_tres_str = self.txt_importe_3.get()

        importe_uno = float(importe_uno_str)
        importe_dos = float(importe_dos_str)
        importe_tres = float(importe_tres_str)    

        suma = importe_uno + importe_dos + importe_tres
        iva = suma * 0.21

        precio_con_iva = suma + iva

        alert(title='Precio con iva', message=f'El precio final, con IVA (21%) incluido es: {precio_con_iva:.2f}')
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()