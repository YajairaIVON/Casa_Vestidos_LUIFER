import tkinter as tk
from tkcalendar import DateEntry
import json

class VentanaRenta:
    def __init__(self, ventana):
        self.ventana = ventana

    def abrir_ventana_renta(self):
        ventana_renta = tk.Toplevel(self.ventana)
        ventana_renta.title("Registrar Renta")

        fecha_inicio_label = tk.Label(ventana_renta, text="Fecha de Inicio:")
        fecha_inicio_label.pack()
        fecha_inicio_entry = DateEntry(ventana_renta)  # Campo de selección de fecha
        fecha_inicio_entry.pack()

        fecha_finalizacion_label = tk.Label(ventana_renta, text="Fecha de Finalización:")
        fecha_finalizacion_label.pack()
        fecha_finalizacion_entry = DateEntry(ventana_renta)  # Campo de selección de fecha
        fecha_finalizacion_entry.pack()

        vestido_label = tk.Label(ventana_renta, text="Vestido:")
        vestido_label.pack()
        vestido_entry = tk.Entry(ventana_renta)
        vestido_entry.pack()

        observacion_label = tk.Label(ventana_renta, text="Observación:")
        observacion_label.pack()
        observacion_entry = tk.Entry(ventana_renta)
        observacion_entry.pack()

        # Botón para guardar la renta
        guardar_button = tk.Button(ventana_renta, text="Guardar", command=lambda: self.guardar_renta(
            fecha_inicio_entry.get(),
            fecha_finalizacion_entry.get(),
            vestido_entry.get(),
            observacion_entry.get()
        ))
        guardar_button.pack()

        # Botón para visualizar renta
        visualizar_button = tk.Button(ventana_renta, text="Visualizar Renta", command=self.visualizar_renta)
        visualizar_button.pack()

    def registrar_renta(self, fecha_inicio, fecha_finalizacion, vestido, observacion):
        renta_data = {
            "Fecha de Inicio": fecha_inicio,
            "Fecha de Finalización": fecha_finalizacion,
            "Vestido": vestido,
            "Observación": observacion
        }

        try:
            with open("renta_data.json", "a") as file:
                json.dump(renta_data, file)
                file.write('\n')
            print("Datos de renta guardados con éxito.")
        except Exception as e:
            print("Error al guardar datos de renta:", str(e))

    def visualizar_renta(self):
        visualizar_ventana = tk.Toplevel(self.ventana)
        visualizar_ventana.title("Datos de Renta")

        try:
            with open("renta_data.json", "r") as file:
                for line in file:
                    renta_data = json.loads(line)
                    for key, value in renta_data.items():
                        label = tk.Label(visualizar_ventana, text=f"{key}: {value}")
                        label.pack()
        except FileNotFoundError:
            print("El archivo de datos de renta no existe.")
        except Exception as e:
            print("Error al cargar datos de renta:", str(e))
