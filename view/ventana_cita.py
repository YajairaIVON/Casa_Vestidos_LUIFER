import tkinter as tk
from tkcalendar import DateEntry  
import json
from modelo.horarios_ocuparo_error import HorarioOcupadoException


class VentanaCita:
    def __init__(self, ventana):
        self.ventana = ventana
        self.citas = []  # Lista para almacenar las citas

    def guardar_cita(self, fecha, hora):
        
        if cita.fecha == fecha and cita.hora == hora:
            raise HorarioOcupadoException("El horario ya está ocupado")
        
        cita = {"Fecha": fecha, "Hora": hora}
        self.citas.append(cita)
        with open("citas.json", "w") as file:
            json.dump(self.citas, file)

    def ver_citas(self):
        ventana_ver_citas = tk.Toplevel(self.ventana)
        ventana_ver_citas.title("Citas Guardadas")

        for cita in self.citas:
            fecha = cita["Fecha"]
            hora = cita["Hora"]
            label = tk.Label(ventana_ver_citas, text=f"Fecha: {fecha}, Hora: {hora}")
            label.pack()

    def abrir_ventana_cita(self):
        ventana_cita = tk.Toplevel(self.ventana)
        ventana_cita.title("Programar Cita")

        fecha_cita_label = tk.Label(ventana_cita, text="Fecha de Cita:")
        fecha_cita_label.pack()
        fecha_cita_entry = DateEntry(ventana_cita)  # Campo de selección de fecha
        fecha_cita_entry.pack()

        hora_cita_label = tk.Label(ventana_cita, text="Hora de Cita:")
        hora_cita_label.pack()
        hora_cita_entry = tk.Entry(ventana_cita)
        hora_cita_entry.pack()

        guardar_button = tk.Button(ventana_cita, text="Guardar Cita", command=lambda: self.guardar_cita(fecha_cita_entry.get(), hora_cita_entry.get()))
        guardar_button.pack()

        ver_citas_button = tk.Button(ventana_cita, text="Ver Citas", command=self.ver_citas)
        ver_citas_button.pack()
