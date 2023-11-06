from tkinter import messagebox
class CamposIncompletosException(Exception):
    def __init__(self, campos_obligatorios):
        self.campos_obligatorios = campos_obligatorios
        mensaje_error = f"Los campos apartir de {campos_obligatorios} se encuentran basios y son obligatorios."
        messagebox.showerror("Error", mensaje_error)
