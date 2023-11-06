import tkinter as tk
from tkinter import messagebox


class VentanaCambioContraseña:
    def __init__(self, ventana, asesores):
        self.ventana = ventana
        self.asesores = asesores

        self.ventana_cambio_contraseña = tk.Toplevel(self.ventana)
        self.ventana_cambio_contraseña.title("Cambiar Contraseña")

        self.usuario_label = tk.Label(self.ventana_cambio_contraseña, text="Usuario:")
        self.usuario_label.pack()

        self.usuario_entry = tk.Entry(self.ventana_cambio_contraseña)
        self.usuario_entry.pack()

        self.nueva_contraseña_label = tk.Label(self.ventana_cambio_contraseña, text="Nueva Contraseña:")
        self.nueva_contraseña_label.pack()

        self.nueva_contraseña_entry = tk.Entry(self.ventana_cambio_contraseña, show="*")
        self.nueva_contraseña_entry.pack()

        self.guardar_contraseña_button = tk.Button(self.ventana_cambio_contraseña, text="Guardar Contraseña", command=self.cambiar_contraseña)
        self.guardar_contraseña_button.pack()

    def cambiar_contraseña(self):
        usuario = self.usuario_entry.get()
        nueva_contraseña = self.nueva_contraseña_entry.get()
        
        if usuario in self.asesores:
            self.asesores[usuario]["Contraseña"] = nueva_contraseña
            messagebox.showinfo("Cambio de Contraseña", "La contraseña se ha cambiado con éxito")



    
