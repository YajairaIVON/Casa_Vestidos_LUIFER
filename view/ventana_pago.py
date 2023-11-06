import tkinter as tk
from modelo.pagos_invalido import PagoInvalidoException

class VentanaPago:
    def __init__(self, ventana):
        self.ventana = ventana

    def abrir_ventana_pago(self):
        ventana_pago = tk.Toplevel(self.ventana)
        ventana_pago.title("Registrar Pago")

        def guardar_datos(self, dinero_total, concepto_pago):
            self.dinero_total = dinero_total_entry.get()
            self.concepto_pago = concepto_pago_entry.get()
            # Aquí puedes implementar la lógica para guardar los datos en tu aplicación
        
            if dinero_total <= 0:
             raise PagoInvalidoException()
       
        def visualizar_datos():
            ventana_visualizacion = tk.Toplevel(self.ventana)
            ventana_visualizacion.title("Visualizar Datos")
            # Aquí puedes mostrar los datos guardados en una nueva ventana

        dinero_total_label = tk.Label(ventana_pago, text="Dinero Total:")
        dinero_total_label.pack()
        dinero_total_entry = tk.Entry(ventana_pago)
        dinero_total_entry.pack()

        concepto_pago_label = tk.Label(ventana_pago, text="Concepto de Pago:")
        concepto_pago_label.pack()
        concepto_pago_entry = tk.Entry(ventana_pago)
        concepto_pago_entry.pack()

        # Botón para guardar los datos
        guardar_button = tk.Button(ventana_pago, text="Guardar", command=guardar_datos)
        guardar_button.pack()

        # Botón para visualizar los datos
        visualizar_button = tk.Button(ventana_pago, text="Visualizar", command=visualizar_datos)
        visualizar_button.pack()



