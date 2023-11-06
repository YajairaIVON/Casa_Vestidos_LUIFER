import tkinter as tk
from tkinter import messagebox


class VentanaMenu:
    def __init__(self, ventana):
        self.ventana_vestido = tk.Toplevel(self.ventana)
        self.ventana_renta = tk.Toplevel(self.ventana)
        self.ventana_cita = tk.Toplevel(self.ventana)
        self.ventana_devolucion = tk.Toplevel(self.ventana)
        self.ventana_renta = tk.Toplevel(self.ventana)
        self.ventana_pago = tk.Toplevel(self.ventana)
        self.ventana_mantenimiento = tk.Toplevel(self.ventana)
        self.ventana = ventana

    def ventana_menu(self):
        if self.asesor_en_sesion:
            self.ventana_menu = tk.Toplevel(self.ventana)
            self.ventana_menu.title("Menú")

            mensaje_bienvenida = tk.Label(self.ventana_menu, text=f"Bienvenido, {self.usuario_actual}!")
            mensaje_bienvenida.pack()

            registrar_inventario_button = tk.Button(self.ventana_menu, text="Registrar Vestido", command=self.ventana_vestido)
            registrar_inventario_button.pack()

            registrar_renta_button = tk.Button(self.ventana_menu, text="Registrar Renta", command=self.ventana_renta)
            registrar_renta_button.pack()

            programar_cita_button = tk.Button(self.ventana_menu, text="Programar Cita", command=self.ventana_cita)
            programar_cita_button.pack()

            registrar_devolucion_button = tk.Button(self.ventana_menu, text="Registrar Devolución", command=self.ventana_devolucion)
            registrar_devolucion_button.pack()

            registrar_pago_button = tk.Button(self.ventana_menu, text="Registrar Pago", command=self.ventana_pago)
            registrar_pago_button.pack()

            registrar_mantenimiento_button = tk.Button(self.ventana_menu, text="Registrar Mantenimiento", command=self.ventana_mantenimiento)
            registrar_mantenimiento_button.pack()
        else:
           messagebox.showerror("Error", "Debe iniciar sesión para acceder al menú.")

       


