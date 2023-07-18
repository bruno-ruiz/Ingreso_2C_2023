import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

''' Bruno Thiago
    Ruiz Aranda
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure windows
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
        importe_uno = self.txt_importe_1.get()
        importe_dos = self.txt_importe_2.get()
        importe_tres = self.txt_importe_3.get()
        importe_uno = float(importe_uno)
        importe_dos = float(importe_dos)
        importe_tres = float(importe_tres)
        suma = importe_uno + importe_dos + importe_tres
        mensaje =f"la suma de los importes es de {suma}"
        alert(title="TP 1",message=mensaje)
        
    def btn_promedio_on_click(self):
        importe_uno = self.txt_importe_1.get()
        importe_dos = self.txt_importe_2.get()
        importe_tres = self.txt_importe_3.get()
        importe_uno = float(importe_uno)
        importe_dos = float(importe_dos)
        importe_tres = float(importe_tres)
        promedio = (importe_uno + importe_dos + importe_tres) / 3
        alert(title="tp1",message="El promedio es de "+ str(promedio))
        

    def btn_total_iva_on_click(self):
        importe_uno= self.txt_importe_1.get()
        importe_dos = self.txt_importe_2.get()
        importe_tres = self.txt_importe_3.get()
        importe_uno= float(importe_uno)
        importe_dos = float(importe_uno)
        importe_tres = float(importe_tres)
        suma = importe_tres + importe_dos + importe_uno
        Iva = suma * 0.21
        Total = suma + Iva
        mensaje = f"el precio final mas iva es {Total}"
        alert(title="TP1",message=mensaje)
          
    
if __name__ == "__main__":
    app = App()
    app.mainloop()