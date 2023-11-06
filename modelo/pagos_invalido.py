from tkinter import messagebox
class PagoInvalidoException(Exception):
    def __init__(self, monto):
        self.monto = monto
        mensaje_error = f"El monto de pago {monto} es inválido. El pago no puede ser menor a cero."
        messagebox.showerror("Error", mensaje_error)

