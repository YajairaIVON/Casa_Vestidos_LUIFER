import tkinter as tk
from tkinter import messagebox

class VentanaVestido:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_inventario = tk.Toplevel(self.ventana_principal.ventana)
        ventana_inventario.title("Registrar Inventario")

        estado_label = tk.Label(ventana_inventario, text="Estado:")
        estado_label.pack()
        estado_entry = tk.Entry(ventana_inventario)
        estado_entry.pack()

        color_label = tk.Label(ventana_inventario, text="Color:")
        color_label.pack()
        color_entry = tk.Entry(ventana_inventario)
        color_entry.pack()

        tipo_label = tk.Label(ventana_inventario, text="Tipo:")
        tipo_label.pack()
        tipo_entry = tk.Entry(ventana_inventario)
        tipo_entry.pack()

        cantidad_label = tk.Label(ventana_inventario, text="Cantidad:")
        cantidad_label.pack()
        cantidad_entry = tk.Entry(ventana_inventario)
        cantidad_entry.pack()

        valor_label = tk.Label(ventana_inventario, text="Valor:")
        valor_label.pack()
        valor_entry = tk.Entry(ventana_inventario)
        valor_entry.pack()

        codigo_label = tk.Label(ventana_inventario, text="Código:")
        codigo_label.pack()
        codigo_entry = tk.Entry(ventana_inventario)
        codigo_entry.pack()

        # Botón para guardar datos del inventario
        guardar_inventario_button = tk.Button(ventana_inventario, text="Guardar Inventario", command=lambda: self.guardar_inventario(
            estado_entry.get(), color_entry.get(), tipo_entry.get(), cantidad_entry.get(), valor_entry.get(), codigo_entry.get()))
        guardar_inventario_button.pack()

        # Botón para visualizar el inventario
        visualizar_inventario_button = tk.Button(ventana_inventario, text="Visualizar Inventario", command=self.visualizar_inventario)
        visualizar_inventario_button.pack()



    def guardar_inventario(self, estado, color, tipo, cantidad, valor, codigo):
        item_inventario = {
            "Estado": estado,
            "Color": color,
            "Tipo": tipo,
            "Cantidad": cantidad,
            "Valor": valor,
            "Código": codigo
        }
        self.inventario.append(item_inventario)
        messagebox.showinfo("Registro Exitoso", "Los datos del inventario se han guardado con éxito.")

    def visualizar_inventario(self):
        visualizar_ventana = tk.Toplevel(self.ventana)
        visualizar_ventana.title("Inventario Registrado")

        lista_inventario = tk.Text(visualizar_ventana)
        lista_inventario.pack()

        for item in self.inventario:
            for campo, valor in item.items():
                lista_inventario.insert(tk.END, f"{campo}: {valor}\n")
            lista_inventario.insert(tk.END, "\n")




