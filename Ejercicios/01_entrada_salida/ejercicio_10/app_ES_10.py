import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Bruno Thiago
apellido:Ruiz Aranda 
---
Ejercicio: entrada_salida_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de descuento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_descuento = customtkinter.CTkEntry(master=self)
        self.txt_descuento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
       importe = self.txt_importe.get()
       porcentaje_Descuento = self.txt_descuento.get()
       importe = float(importe)
       descuento = float(porcentaje_Descuento)
       descuento = importe * descuento /100
       descuento_final = importe - descuento
       mensaje =f"El descuento cera de {descuento_final} "
       alert(title="Ejercicio 10",message=mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()