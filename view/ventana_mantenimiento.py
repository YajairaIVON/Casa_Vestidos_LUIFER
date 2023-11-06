import tkinter as tk
from tkcalendar import DateEntry

#from view.ventana_menu import Menu

class Mantenimiento:
    def __init__(self, ventana):
        self.ventana = ventana

    def abrir_ventana_mantenimiento(self):
        ventana_mantenimiento = tk.Toplevel(self.ventana)
        ventana_mantenimiento.title("Registrar Mantenimiento")

        def guardar_datos():
            fecha_inicio = fecha_inicio_entry.get()
            fecha_fin = fecha_fin_entry.get()
            descripcion = descripcion_entry.get()
            costo = costo_entry.get()
            # Aquí puedes implementar la lógica para guardar los datos en tu aplicación

        def visualizar_datos():
            ventana_visualizacion = tk.Toplevel(self.ventana)
            ventana_visualizacion.title("Visualizar Datos")
            # Aquí puedes mostrar los datos guardados en una nueva ventana

        fecha_inicio_label = tk.Label(ventana_mantenimiento, text="Fecha de Inicio:")
        fecha_inicio_label.pack()
        fecha_inicio_entry = DateEntry(ventana_mantenimiento)
        fecha_inicio_entry.pack()

        fecha_fin_label = tk.Label(ventana_mantenimiento, text="Fecha de Fin:")
        fecha_fin_label.pack()
        fecha_fin_entry = DateEntry(ventana_mantenimiento)
        fecha_fin_entry.pack()

        descripcion_label = tk.Label(ventana_mantenimiento, text="Descripción:")
        descripcion_label.pack()
        descripcion_entry = tk.Entry(ventana_mantenimiento)
        descripcion_entry.pack()

        costo_label = tk.Label(ventana_mantenimiento, text="Costo:")
        costo_label.pack()
        costo_entry = tk.Entry(ventana_mantenimiento)
        costo_entry.pack()

        # Botón para guardar los datos
        guardar_button = tk.Button(ventana_mantenimiento, text="Guardar", command=guardar_datos)
        guardar_button.pack()

        # Botón para visualizar los datos
        visualizar_button = tk.Button(ventana_mantenimiento, text="Visualizar", command=visualizar_datos)
        visualizar_button.pack()

