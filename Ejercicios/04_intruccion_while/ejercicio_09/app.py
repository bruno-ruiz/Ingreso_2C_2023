import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Bruno Thiago
Ruiz Aranda
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        flag_primera_vez = True
        respuesta = True
        numero_maximo = None
        numero_minimo = None
            
        while respuesta != None:
            numero = prompt(title="info",prompt="Ingrese un número")
            numero = int(numero)
            
            if flag_primera_vez == True:
                numero_maximo = numero
                numero_minimo = numero
                flag_primera_vez = False
            else:
                if numero > numero_maximo:
                    numero_maximo = numero
                else:
                    if numero < numero_minimo:
                        numero_minimo = numero
            
            respuesta = prompt(title="Info",prompt="¿Desea a seguir agregando numeros?")

        self.txt_maximo.delete(0,tkinter.END)
        self.txt_maximo.insert(0,numero_maximo)
        self.txt_minimo.delete(0,tkinter.END)
        self.txt_minimo.insert(0,numero_minimo)



if __name__ == "__main__":
    app = App()
    app.mainloop()
