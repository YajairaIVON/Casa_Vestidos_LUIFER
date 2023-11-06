import tkinter as tk
from tkcalendar import DateEntry 
import json

#from view.ventana_menu import menu

class VentanaDevolucion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.devoluciones = []  # Lista para almacenar las devoluciones

    def registrar_devolucion(self, fecha_devolucion):
        devolucion = {"Fecha de Devolución": fecha_devolucion}
        self.devoluciones.append(devolucion)
        with open("devoluciones.json", "w") as file:
            json.dump(self.devoluciones, file)

    def ver_devoluciones(self):
        ventana_ver_devoluciones = tk.Toplevel(self.ventana)
        ventana_ver_devoluciones.title("Devoluciones Registradas")

        for devolucion in self.devoluciones:
            fecha_devolucion = devolucion["Fecha de Devolución"]
            label = tk.Label(ventana_ver_devoluciones, text=f"Fecha de Devolución: {fecha_devolucion}")
            label.pack()

    def abrir_ventana_devolucion(self):
        ventana_devolucion = tk.Toplevel(self.ventana)
        ventana_devolucion.title("Registrar Devolución")

        fecha_devolucion_label = tk.Label(ventana_devolucion, text="Fecha de Devolución:")
        fecha_devolucion_label.pack()
        fecha_devolucion_entry = DateEntry(ventana_devolucion)  # Campo de selección de fecha
        fecha_devolucion_entry.pack()

        guardar_devolucion_button = tk.Button(ventana_devolucion, text="Guardar Devolución", command=lambda: self.guardar_devolucion(fecha_devolucion_entry.get()))
        guardar_devolucion_button.pack()

        ver_devoluciones_button = tk.Button(ventana_devolucion, text="Ver Devoluciones", command=self.ver_devoluciones)
        ver_devoluciones_button.pack()


