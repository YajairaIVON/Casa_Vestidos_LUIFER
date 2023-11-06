import tkinter as tk
from tkinter import messagebox
from modelo.campos_incompletos import CamposIncompletosException

class VentanaRegistroAsesor:

    def __init__(self, ventana_principal):
        self.ventana_principal  = ventana_principal
        self.ventana_registro = tk.Toplevel(self.ventana_principal.ventana)
        self.ventana_registro.title("Registro de Asesor")

        # Campos de registro
        self.nombre_label = tk.Label(self.ventana_registro, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.ventana_registro)
        self.nombre_entry.pack()

        self.cedula_label = tk.Label(self.ventana_registro, text="Cédula:")
        self.cedula_label.pack()
        self.cedula_entry = tk.Entry(self.ventana_registro)
        self.cedula_entry.pack()

        self.celular_label = tk.Label(self.ventana_registro, text="Celular:")
        self.celular_label.pack()
        self.celular_entry = tk.Entry(self.ventana_registro)
        self.celular_entry.pack()

        self.correo_label = tk.Label(
            self.ventana_registro, text="Correo Electrónico:")
        self.correo_label.pack()
        self.correo_entry = tk.Entry(self.ventana_registro)
        self.correo_entry.pack()

        self.usuario_label = tk.Label(self.ventana_registro, text="Usuario:")
        self.usuario_label.pack()
        self.usuario_entry = tk.Entry(self.ventana_registro)
        self.usuario_entry.pack()

        self.contraseña_label = tk.Label(self.ventana_registro, text="Contraseña:")
        self.contraseña_label.pack()
        # Para ocultar la contraseña
        self.contraseña_entry = tk.Entry(self.ventana_registro, show="*")
        self.contraseña_entry.pack()

        
        self.registrar_button = tk.Button(
            self.ventana_registro, text="Registrar", command=self.registrar_asesor)
        self.registrar_button.pack()

      

    def registrar_asesor(self):
        nombre = self.nombre_entry.get()
        if not nombre:
            raise CamposIncompletosException("nombre")
        cedula = self.cedula_entry.get()
        if not cedula:
            raise CamposIncompletosException("cedula")
        celular = self.celular_entry.get()
        if not celular:
            raise CamposIncompletosException("celular")
        correo = self.correo_entry.get()
        if not correo:
            raise CamposIncompletosException("correo")
        usuario = self.usuario_entry.get()
        if not usuario:
            raise CamposIncompletosException("usuario")
        contrasenha = self.contraseña_entry.get()
        if not contrasenha:
            raise CamposIncompletosException("contrasenha")
        
        self.ventana_principal.luifer.registrar_asesor(
            nombre, cedula, celular, correo, usuario, contrasenha)
        messagebox.showinfo("Registro Exitoso", "El asesor se ha registrado con éxito.")
        self.ventana_registro.destroy() #Cierra la ventana de registro para permitir solo la vizualizacion de la nueva ventana

        
