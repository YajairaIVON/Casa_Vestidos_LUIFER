import tkinter as tk
from tkinter import messagebox
from ventana_menu import VentanaMenu

class VentanaIniciarSesion:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal #Conexion entre ventanaIniciarSesion y VentanaPrincipal
        ventana_iniciar_sesion = tk.Toplevel(self.ventana_principal.ventana)
        ventana_iniciar_sesion.title("Iniciar Sesión")

        usuario_label = tk.Label(ventana_iniciar_sesion, text="Usuario:")
        usuario_label.pack()
        self.usuario_entry = tk.Entry(ventana_iniciar_sesion)
        self.usuario_entry.pack()

        contraseña_label = tk.Label(ventana_iniciar_sesion, text="Contraseña:")
        contraseña_label.pack()
        self.contraseña_entry = tk.Entry(ventana_iniciar_sesion, show="*")
        self.contraseña_entry.pack()

        ingresar_button = tk.Button(ventana_iniciar_sesion, text="Ingresar", command=lambda: self.iniciar_sesion(
            self.usuario_entry.get(), self.contraseña_entry.get()))
        
        ingresar_button = tk.Button(ventana_iniciar_sesion, text="Ingresar", command=self.iniciar_sesion)
        ingresar_button.pack()

        cambiar_contraseña_button = tk.Button(
            ventana_iniciar_sesion, text="Cambiar Contraseña", command=self.abrir_ventana_cambio_contraseña)
        cambiar_contraseña_button.pack()

    def iniciar_sesion(self):
        nombre_de_usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()

        for asesor in self.ventana_principal.luifer.asesores:
            if asesor.usuario == nombre_de_usuario:
                if asesor.iniciar_sesion(nombre_de_usuario, contraseña):
                    self.ventana_principal.luifer.asesor_en_sesion = asesor
                    VentanaMenu(self)                                   
                else:
                    #Mostrar mensaje No inicia sesion
                    pass

    def abrir_ventana_cambio_contraseña(self):
        ventana_cambio_contraseña = tk.Toplevel(self.ventana)
        ventana_cambio_contraseña.title("Cambiar Contraseña")

        usuario_label = tk.Label(ventana_cambio_contraseña, text="Usuario:")
        usuario_label.pack()
        usuario_entry = tk.Entry(ventana_cambio_contraseña)
        usuario_entry.pack()

        nueva_contraseña_label = tk.Label(ventana_cambio_contraseña, text="Nueva Contraseña:")
        nueva_contraseña_label.pack()
        nueva_contraseña_entry = tk.Entry(ventana_cambio_contraseña, show="*")
        nueva_contraseña_entry.pack()

        guardar_contraseña_button = tk.Button(ventana_cambio_contraseña, text="Guardar Contraseña", command=lambda: self.cambiar_contraseña(usuario_entry.get(), nueva_contraseña_entry.get()))
        guardar_contraseña_button.pack()

    def cambiar_contraseña(self, usuario, nueva_contraseña):
        if usuario in self.asesores:
            self.asesores[usuario]["Contraseña"] = nueva_contraseña
            messagebox.showinfo("Cambio de Contraseña", "La contraseña se ha cambiado con éxito.")
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")

    def abrir_ventana_menu(self):
        if self.usuario_actual:
            ventana_menu = tk.Toplevel(self.ventana)
            ventana_menu.title("Menú")
            
            mensaje_bienvenida = tk.Label(ventana_menu, text=f"Bienvenido, {self.usuario_actual}!")
            mensaje_bienvenida.pack()
            
            registrar_inventario_button = tk.Button(ventana_menu, text="Registrar Inventario", command=self.abrir_ventana_inventario)
            registrar_inventario_button.pack()

            registrar_renta_button = tk.Button(ventana_menu, text="Registrar Renta", command=self.abrir_ventana_renta)
            registrar_renta_button.pack()

            programar_cita_button = tk.Button(ventana_menu, text="Programar Cita", command=self.abrir_ventana_cita)
            programar_cita_button.pack()

            registrar_devolucion_button = tk.Button(ventana_menu, text="Registrar Devolución", command=self.abrir_ventana_devolucion)
            registrar_devolucion_button.pack()

            registrar_pago_button = tk.Button(ventana_menu, text="Registrar Pago", command=self.abrir_ventana_pago)
            registrar_pago_button.pack()

            registrar_mantenimiento_button = tk.Button(ventana_menu, text="Registrar Mantenimiento", command=self.abrir_ventana_mantenimiento)
            registrar_mantenimiento_button.pack()
        else:
            messagebox.showerror("Error", "Debe iniciar sesión para acceder al menú.")