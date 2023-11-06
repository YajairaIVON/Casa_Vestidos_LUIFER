import tkinter as tk

from view.ventana_registro_asesor import VentanaRegistroAsesor
from view.ventana_iniciar_sesion import VentanaIniciarSesion
from modelo.luifer import Luifer


class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Casa de Vestidos App")

        # Botones en la ventana principal
        registrar_asesor_button = tk.Button(
            self.ventana, text="Registrar Asesor", command=self.abrir_ventana_registro)
        registrar_asesor_button.pack()

        iniciar_sesion_button = tk.Button(
            self.ventana, text="Iniciar Sesión", command=self.abrir_ventana_iniciar_sesion)
        iniciar_sesion_button.pack()
        self.luifer = Luifer()  # Conexion entre view y model.


    def abrir_ventana_registro(self):
        VentanaRegistroAsesor(self)

    def abrir_ventana_iniciar_sesion(self):
        VentanaIniciarSesion(self)

    def Mostrar(self):
        self.ventana.mainloop()
