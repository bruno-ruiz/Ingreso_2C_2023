import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Bruno Thiago
Ruiz Aranda
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. txt.delte y insert

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)
                
        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        apellido = prompt(title="Info",prompt="Ingrese su apellido").upper()
        while apellido == None or not apellido.isdigit():
            apellido = prompt(title="Info error",prompt="Ingrese su apellido").upper()
            
        edad = prompt(title="Info",prompt="ingrese su edad")
        while edad == None or (edad > 17 and edad < 91):
            edad = prompt(title="Info error",prompt="ingrese su edad")
            edad = int(edad)
             
        estado_civil = prompt(title="Info",prompt="ingrese su estado_civil, soltero, casado, viudo").upper()
        while estado_civil == None or (estado_civil != "soltero" and estado_civil != "femenino" and estado_civil != "viudo"): 
          estado_civil = prompt(title="Info error",prompt="ingrese su estado_civil,soltero, casado, viudo").upper()
        
        numero_de_legajo = prompt(title="Info",prompt="Ingrese su legajo: sin ceros a la izquierda")
        while numero_de_legajo == None or(numero_de_legajo == 4) or legajo.startswith('0'):
            numero_de_legajo = prompt(title="Info error",prompt="Ingrese su legajo: sin ceros a la izquierda")
            numero_de_legajo = int(numero_de_legajo)
        
        self.txt_apellido.delete(0,tkinter.END)
        self.txt_apellido.insert(0,apellido)
        self.txt_edad.delete(0,tkinter.END)
        self.txt_edad.insert(0,edad)
        self.txt_legajo.delete(0,tkinter.END)
        self.txt_legajo.insert(0,numero_de_legajo)
        self.combobox_tipo.delete(0,tkinter.END)
        self.combobox_tipo.insert(0,estado_civil)
 
    
if __name__ == "__main__":
    app = App()
    app.mainloop()