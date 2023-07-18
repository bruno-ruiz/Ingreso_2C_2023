import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Bruno Thiago
Ruiz Aranda

Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca_lamparas = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad = int(cantidad)
        precio_bruto = 800 * cantidad
        if cantidad > 5:
            importe_descuento = precio_bruto * 0.5
        else:
            if cantidad == 5:
                if marca_lamparas == "ArgentinaLuz":
                    importe_descuento = precio_bruto * 0.6
                else:
                    importe_descuento = precio_bruto * 0.7
            else:
                if cantidad == 4:
                    if marca_lamparas == "ArgentinaLuz"  or marca_lamparas == "FelipeLamparas":
                        importe_descuento = precio_bruto * 0.75
                    else:
                        importe_descuento = precio_bruto * 0.80
                else:
                    if cantidad == 3:
                        if marca_lamparas == "ArgentinaLuz":
                            importe_descuento  = precio_bruto * 0.85
                        else:
                            if marca_lamparas == "FelipeLamparas":
                                importe_descuento = precio_bruto * 0.90
                            else:
                                importe_descuento = precio_bruto * 0.95
                        if cantidad < 3:
                            importe_descuento = precio_bruto * 0
                   
        
        descuento_adicional = precio_bruto * importe_descuento
        importe_final = precio_bruto - descuento_adicional
        if importe_final > 4000:
            descuento_adicional = importe_descuento * 0.95
            alert(title="TP 4",message=f"El descuento nacional que obtuvo es de: {descuento_adicional}")
                        
        alert(title="TP 4",message= f"El importe final con descuento es: {importe_descuento}")
                    
if __name__ == "__main__":
    app = App()
    app.mainloop()