from tkinter import messagebox

class HorarioOcupadoException(Exception):
    def __init__(self, cita):
        self.cita = cita
        mensaje_error = f"El horario {cita} ya está ocupado."
        messagebox.showerror("Error", mensaje_error)
        

