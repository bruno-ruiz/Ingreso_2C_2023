import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Bruno Thiago
Ruiz Aranda
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


    def btn_comenzar_ingreso_on_click(self):
        i = 0
        respuesta = True
        suma_negativos = 0
        suma_positivos = 0
        cantidad_de_negativos = 0
        cantidad_de_positivos = 0
        cantidad_de_ceros = 0
        diferencia = 0
        
        while respuesta != None:
            numero = prompt(title="Info",prompt="ingrese un numero")
            numero = int(numero)
            i = 0
            if numero < 0:
                 suma_negativos += numero
                 cantidad_de_negativos += 1
            else:
                if numero == 0:
                    cantidad_de_ceros += 1
                else:
                    suma_positivos += numero
                    cantidad_de_positivos += 1
                    
            respuesta = prompt(title="Info",prompt="¿Desea a seguir agregando numeros?")
            
        diferencia = cantidad_de_positivos - cantidad_de_negativos
        
        mensaje = (f"La suma acumulada de los negativos:{suma_negativos}\n"
                   f"La suma acumulada de los positivos:{suma_positivos}\n"
                   f"Cantidad de números positivos ingresados_{cantidad_de_positivos}\n"
                   f"Cantidad de números negativos ingresados:{cantidad_de_negativos}\n"
                   f"Cantidad de ceros:{cantidad_de_ceros}\n"
                   f"Diferencia entre la cantidad de los números positivos ingresados y los negativos:{diferencia}")
        
        Alert(title="UTN", message=mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
