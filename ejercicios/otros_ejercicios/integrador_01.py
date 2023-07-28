import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de comprar cada entrada:

Nombre del comprador
Edad (no menor a 16)
Género (Masculino, Femenino, Otro)
Tipo de entrada (General, Campo delantero, Platea)
Medio de pago (Crédito, Efectivo, Débito) 
Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, el medio de pago y su precio correspondiente.

Lista de precios: 
General: $16000
Campo: $25000
Platea: $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 


Al finalizar la venta de entradas, los organizadores quieren obtener la siguiente información:

A. Cantidad total de dinero recaudado por las ventas de entradas.
B. Cantidad de entradas vendidas para cada tipo.
C. Promedio de edad de las personas que compraron ubicación en Platea.
D. Nombre de la persona de mayor edad que compró una entrada de platea.
E. Porcentaje de entradas vendidas de tipo "general"
F. Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
G. Tipo de entradas más vendidas


PARTE 2
A. Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo delantero".
B. Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
C. Calcula el número total de entradas compradas por personas mayores de 30 años y su precio promedio.
D. Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
E. Cual es el total de descuentos que aplicó la empresa
F. Cuál es el total de descuentos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito.
G. Encuentra el nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito.
H. Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
I. Calcula el monto total recaudado por la venta de entradas de tipo "General" y pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.



'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

# Lista de nombres
        self.nombres = [
        "Juan", "María", "Luis", "Ana", "Carlos", "Jose", "Pedro", "Sofía", "Miguel", "Valentina",
        "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina", "Jorge", "Camila", "Ricardo", "Isabella",
        "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela", "Gustavo", "Carolina", "Emilio", "Antonella",
        "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina", "Raul", "Rocio", "Javier", "Marina",
        "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena", "Oscar", "Pilar", "Hugo", "Juana",
        "Guillermo", "Natalia", "Francisco", "Constanza", "Hector", "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
        "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia", "Camilo", "Teresa", "Samuel", "Rosa",
        "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano", "Silvia", "Nicolas", "Alicia",
        "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo", "Beatriz", "Elias", "Rita",
        "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes", "Gerardo", "Manuela", "Feliciano", "Marta"
    ]




    # Lista de edades (mayores o iguales a 16)
        self.edades = [
        25, 33, 20, 29, 50, 40, 22, 28, 35, 18,
        26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
        29, 17, 28, 34, 20, 25, 22, 33, 40, 16,
        19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
        35, 20, 23, 39, 30, 27, 22, 36, 28, 32,
        31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
        29, 22, 36, 30, 19, 25, 21, 38, 34, 17,
        32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
        31, 35, 24, 19, 28, 30, 26, 37, 33, 21,
        25, 29, 16, 38, 40, 50, 27, 30, 32, 24
    ]




    # Lista de géneros (Masculino, Femenino u Otro)
        self.generos = [
        "Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Masculino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
    ]




    # Lista de tipo de entrada (General, Campo delantero, Platea)
        self.tipo_entrada = [
        "General", "Campo delantero", "Platea", "General", "Platea", "General", "General", "Platea", "Campo delantero", "General",
        "Campo delantero", "Platea", "General", "General", "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "General", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero"
    ]




    # Lista de medio de pago (Credito, Debito, Efectivo)
        self.medio_pago = [
        "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito"
    ]




        # Lista de precios correspondientes a cada tipo de entrada
        self.precios = [16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000
    ]



    def btn_mostrar_on_click(self):
        mensaje = ''
    
    #A. Cantidad total de dinero recaudado por las ventas de entradas.  
        acumulador_precios_con_descuento = 0
        for i in range(len(self.precios)):
            precio = self.precios[i]
            medio_pago = self.medio_pago[i]
            if medio_pago == 'Credito':
                precio = precio * 0.8
                acumulador_precios_con_descuento += precio
            else:
                if medio_pago == 'Debito':
                    precio = precio * 0.85
                    acumulador_precios_con_descuento += precio
                else:
                    precio = precio 
                    acumulador_precios_con_descuento += precio
                    
        mensaje += f'A: La cantidad de dinero recaudado por las ventas es de {acumulador_precios_con_descuento} \n'


    #B. Cantidad de entradas vendidas para cada tipo.
        contador_general = 0
        contador_campo = 0
        contador_platea = 0 

        for i in range(len(self.tipo_entrada)):
            if self.tipo_entrada[i] == "General":
                contador_general += 1
            else:
                if self.tipo_entrada[i] == "Campo delantero":
                    contador_campo +=1
                else:
                    contador_platea += 1

        mensaje += f"B: La cantidad de entradas generales que se vendieron es {contador_general}, de campo delantero se vendieron: {contador_campo} y de platea: {contador_platea} \n"


    #C. Promedio de edad de las personas que compraron ubicación en Platea.
        acumulador_edades_platea = 0
        contador_edades_platea = 0
        

        for i in range(len(self.tipo_entrada)): #i se comparte en el resto de las listas - x persona 
            if self.tipo_entrada[i] == "Platea":
                acumulador_edades_platea += self.edades[i]
                contador_edades_platea +=1 


        if contador_edades_platea != 0:
            promedio = acumulador_edades_platea / contador_edades_platea  ################ ver hacer flag para contador ################ PORQUE ROMPE EL PROGRAMA SI /0 
            mensaje += f'C: El promedio de edad de platea es {promedio:.1f} \n'
        else:
            mensaje += 'C: Nadie compró platea. No hay un promedio por calcular \n'

        
    #D. Nombre de la persona de mayor edad que compró una entrada de Platea.
        edad_maxima = 0
        flag = True
        
        # Primero obtengo la mayor edad
        for i in range(len(self.tipo_entrada)): #i se comparte en el resto de las listas - x persona 
            edad = self.edades[i]
            tipo = self.tipo_entrada[i]
            if tipo == "Platea":
                if edad > edad_maxima or flag == True:
                    edad_maxima = edad
                    flag = False
                
        # Luego busco que nombres tienen esa edad  
        for i in range(len(self.tipo_entrada)):
            edad = self.edades[i]
            tipo = self.tipo_entrada[i]
            nombre = self.nombres[i]
            if edad == edad_maxima and tipo == 'Platea':
                mensaje += f'\t{nombre} \n'


    #E. Porcentaje de entradas vendidas de tipo "general"  #ent_generales * 100/ total
        contador_entradas_total = 0
        contador_entradas_general = 0

        for i in range(len(self.tipo_entrada)):
            contador_entradas_total += 1
            if self.tipo_entrada[i] == "General":
                contador_entradas_general += 1

        porcentaje_entradas_general = contador_entradas_general * 100 / contador_entradas_total

        mensaje +=f'El porcentaje de entradas vendidas de tipo "General" es {porcentaje_entradas_general} \n'

    #F. Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
        maxima_Edad = 0
        flag = True

        #Obtener la edad maxima
        for i in range(len(self.edades)):
            edad = self.edades[i]
            nombre = self.nombres[i]
            tipo = self.tipo_entrada[i]
            if tipo == 'General': 
                if edad > maxima_Edad or flag == True:
                    maxima_Edad = edad
                    flag = False
        for i in range(len(self.edades)):
            edad = self.edades[i]
            nombre = self.nombres[i]
            tipo = self.tipo_entrada[i]
            genero = self.generos[i]
            if edad == maxima_Edad and tipo == 'General' and genero == 'Masculino':
                mensaje +=f'La edad maxima (F) es: {maxima_Edad} \t{nombre}  \n'


    #G. Tipo de entradas más vendidas
        contador_campo_g = 0
        contador_general_g = 0
        contador_platea_g = 0 

        entradas_mas_vendidas = 0

        #Obtengo el tipo de entrada
        for i in range(len(self.tipo_entrada)):
            tipo = self.tipo_entrada[i]
            if tipo == 'General':
                contador_general_g += 1
            else:
                if tipo == 'Platea':
                    contador_platea_g += 1
                else:
                    contador_campo_g += 1

        #Comparo que contador obtumo más ventas
        if contador_campo_g > entradas_mas_vendidas and (contador_campo_g > contador_platea and contador_campo_g > contador_general):
            entradas_mas_vendidas = contador_campo_g
            nombre_mas_vendido = "Campo delantero"
        else:
            if contador_general  > entradas_mas_vendidas and contador_general > contador_platea and contador_general> contador_campo_g:
                entradas_mas_vendidas = contador_general
                nombre_mas_vendido = "General"
            else:
                nombre_mas_vendido = "Platea"

        if contador_campo_g > entradas_mas_vendidas or contador_general_g > entradas_mas_vendidas or contador_platea_g > entradas_mas_vendidas:
            entradas_mas_vendidas = contador_campo_g or contador_general_g or contador_platea_g

        mensaje +=f'Entradas mas vendidas son de: {nombre_mas_vendido} (y se vendieron {entradas_mas_vendidas})  \n'

    # 2A. Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo delantero".
        contador_genero_f = 0
        contador_genero_m = 0
        

        for i in range(len(self.tipo_entrada)):
            tipo = self.tipo_entrada[i]
            genero = self.generos[i]

            if tipo == "Campo delantero":
                if genero == 'Femenino':
                    contador_genero_f += 1
                else: 
                    if genero == 'Masculino':
                        contador_genero_m += 1
        
        if contador_genero_f> contador_genero_m:
            genero_mayor_campo_delantero = 'Femenino'
            mensaje +=f'1: El genero que más entradas compró Campo delantero es: {genero_mayor_campo_delantero} \n'
        else:
            genero_mayor_campo_delantero = 'Masculino'
            mensaje +=f'1: El genero que más entradas compró Campo delantero es: {genero_mayor_campo_delantero} \n'


    # 2B. Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
        contador_entradas_general = 0
        acumulador_edad_general = 0

        for i in range(len(self.medio_pago)):
            tipo = self.tipo_entrada[i]
            edad = self.edades[i]
            medio_pago = self.medio_pago[i]

            if tipo == 'General' and medio_pago == 'Credito': 
                acumulador_edad_general += edad
                contador_entradas_general += 1

        promedio = acumulador_edad_general / contador_entradas_general

        mensaje += f'2: La cantidad de personas es: {contador_entradas_general}. El promedio de edades de quienes pagaron con tarjeta de credito entradas de tipo "General" es: {promedio:.2f} \n'

    # 2C. Calcula el número total de entradas compradas por personas mayores de 30 años y su precio promedio.
        acumulador_precio_entrada = 0
        contador_precio_entrada = 0

        for i in range(len(self.edades)):
            edad= self.edades[i]
            precio = self.precios[i]

            if edad > 30:
                acumulador_precio_entrada += precio
                contador_precio_entrada += 1

        if contador_precio_entrada != 0:
            promedio = acumulador_precio_entrada / contador_precio_entrada
            mensaje +=f'3: La cantidad de entradas compradas por personamas > 30 es: {contador_precio_entrada}, y el precio promedio es {promedio:.2f} \n '
        else:
            mensaje +='3: No hay venta de entradas a personas con más de 30 años \n '

    # 2D. Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
        contador_total_entradas = 0
        contador_entradas_platea = 0

        for i in range(len(self.tipo_entrada)):
            tipo = self.tipo_entrada[i]
            medio_pago = self.medio_pago[i]
            contador_total_entradas += 1

            if medio_pago == 'Debito' and tipo == 'Platea':
                contador_entradas_platea += 1

        procentaje = (contador_entradas_platea * 100) / contador_total_entradas 

        mensaje +=f'4: El porcentaje de personas que compró platea y pagó con debito es: {procentaje} \n '

    # 2E. Cual es el total de descuentos en pesos que aplicó la empresa
        acumulador_desc = 0
        contador_credito= 0
        contador_debito = 0 
        for i in range(len(self.precios)):
            precio = self.precios[i]
            medio_pago = self.medio_pago[i]


            if medio_pago == 'Credito':
                descuento_aplicado = precio * 0.2
                acumulador_desc += descuento_aplicado
                contador_credito += precio
            else:
                if medio_pago == 'Debito':
                    descuento_aplicado = precio * 0.15
                    acumulador_desc += descuento_aplicado
                    contador_debito += precio
        
        mensaje +=f'5: El total de descuentos aplicados (debito y credito) fue de ${acumulador_desc}. Credito {contador_credito}. Debito {contador_debito} \n'
            

    # 2F. Cuál es el total de descuentos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito.

        acumulador_desc = 0
        for i in range(len(self.precios)):
            precio = self.precios[i]
            medio_pago = self.medio_pago[i]


            if medio_pago == 'Credito':
                descuento_aplicado = precio * 0.2
                acumulador_desc += descuento_aplicado

        
        mensaje += f'6: El total de descuentos aplicados  por compra con crédito fue de ${acumulador_desc} \n'

    # 2G. Encuentra el nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito.
        precio_general_mas_alto = 0 

        for i in range(len(self.tipo_entrada)):
            tipo = self.tipo_entrada[i]
            medio_pago = self.medio_pago[i]
            precio = self.precios[i]
        
            if tipo == 'General' and medio_pago == 'Debito':
                if precio > precio_general_mas_alto: ## buscar precio 
                    precio_general_mas_alto = precio
    
        nombres_general_precio_mas_alto = ''
        edades_general_precio_mas_alto = ''
        
        for i in range(len(self.tipo_entrada)):
            tipo = self.tipo_entrada[i]
            precio = self.precios[i]
            nombre = self.nombres[i]
            edad = self.edades[i]
            medio_pago = self.medio_pago[i]

            if tipo == 'General' and medio_pago == 'Debito':
                if precio_general_mas_alto == precio:
                    nombres_general_precio_mas_alto += f' {nombre}'
                    edades_general_precio_mas_alto += f' {edad}'

        # cuando tengo el precio, hago otro for para iterar lo mismo y en un if, cada vez que el precio conicnda acumulo los nombres de las personas
        
        mensaje +=f'7: El nombre de la persona que pago el precio mas alto (${precio_general_mas_alto})en General, pagando con debito es {nombres_general_precio_mas_alto } y su edad es{edades_general_precio_mas_alto} \n'

    # 2H. Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
        contador_platea_con_edad_prima = 0

        for i in range(len(self.tipo_entrada)):
            tipo = self.tipo_entrada[i]
            edad = self.edades[i]
            cantidad_divisores = 0 

            if tipo == 'Platea':
                for i in range(1, self.edades[i] +1):
                    if edad % i == 0:
                        cantidad_divisores += 1
                if cantidad_divisores == 2:
                    contador_platea_con_edad_prima += 1
        
        mensaje +=f'8: La cantidad de personas que compraron platea y su edad es un número primo es: {contador_platea_con_edad_prima}  \n'
            

    # 2I. Calcula el monto total recaudado por la venta de entradas de tipo "General" y pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.

        acumulador_precio_general_credeito_mc = 0

        for i in range(len(self.tipo_entrada)):
            tipo = self.tipo_entrada[i]
            medio_pago = self.medio_pago[i]
            edad = self.edades[i]
            precio = self.precios[i]
            if tipo == 'General' and medio_pago == 'Credito':
                if edad % 5 == 0:
                    acumulador_precio_general_credeito_mc += precio * 0.8

        mensaje +=f'9: El monto total recaudado de entradas General, pagadas con credito, cuyas personas tengan edad multipo de 5 es: {acumulador_precio_general_credeito_mc} \n'


        alert('utn', mensaje)
        
    def btn_cargar_on_click(self):
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

