import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # Importamos el módulo tkcalendar para la selección de fechas

from modelo.horarios_ocuparo_error import HorarioOcupadoException
from modelo.campos_incompletos import CamposIncompletosException
from modelo.pagos_invalido import PagoInvalidoException

class CasaVestidosApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Casa de Vestidos App")
        self.horarios_ocupados = {}
        self.inventario = [] 
        self.rentas = [] 
        self.citas = [] 
        self.mantenimientos = [] 
        self.devoluciones = [] 
        self.pagos = [] 
        
        # Botones en la ventana principal
        registrar_asesor_button = tk.Button(ventana, text="Registrar Asesor", command=self.abrir_ventana_registro)
        registrar_asesor_button.pack()
        
        iniciar_sesion_button = tk.Button(ventana, text="Iniciar Sesión", command=self.abrir_ventana_iniciar_sesion)
        iniciar_sesion_button.pack()
        
        self.asesores = {}  # Almacena los asesores registrados
        self.usuario_actual = None  # Almacena el usuario que ha iniciado sesión

    def abrir_ventana_registro(self):
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registro de Asesor")

        # Campos de registro
        nombre_label = tk.Label(ventana_registro, text="Nombre:")
        nombre_label.pack()
        nombre_entry = tk.Entry(ventana_registro)
        nombre_entry.pack()

        cedula_label = tk.Label(ventana_registro, text="Cédula:")
        cedula_label.pack()
        cedula_entry = tk.Entry(ventana_registro)
        cedula_entry.pack()

        celular_label = tk.Label(ventana_registro, text="Celular:")
        celular_label.pack()
        celular_entry = tk.Entry(ventana_registro)
        celular_entry.pack()

        correo_label = tk.Label(ventana_registro, text="Correo Electrónico:")
        correo_label.pack()
        correo_entry = tk.Entry(ventana_registro)
        correo_entry.pack()

        usuario_label = tk.Label(ventana_registro, text="Usuario:")
        usuario_label.pack()
        usuario_entry = tk.Entry(ventana_registro)
        usuario_entry.pack()

        contraseña_label = tk.Label(ventana_registro, text="Contraseña:")
        contraseña_label.pack()
        contraseña_entry = tk.Entry(ventana_registro, show="*")  # Para ocultar la contraseña
        contraseña_entry.pack()

        registrar_button = tk.Button(ventana_registro, text="Registrar", command=lambda: self.registrar_asesor(nombre_entry.get(), cedula_entry.get(), celular_entry.get(), correo_entry.get(), usuario_entry.get(), contraseña_entry.get()))
        registrar_button.pack()

        visualizar_button = tk.Button(ventana_registro, text="Visualizar Asesores", command=self.visualizar_asesores)
        visualizar_button.pack()

    def registrar_asesor(self, nombre, cedula, celular, correo, usuario, contraseña):
        # Verifica si los campos obligatorios están completos
        campos_obligatorios = [nombre, cedula, celular, correo, usuario, contraseña]
        if not all(campos_obligatorios):
            try:
                raise CamposIncompletosException(next(campo for campo, valor in zip(["Nombre", "Cédula", "Celular", "Correo Electrónico", "Usuario", "Contraseña"], campos_obligatorios) if not valor))
            except CamposIncompletosException as e:
                messagebox.showerror("Error", str(e))
            return

        if usuario not in self.asesores:
            self.asesores[usuario] = {
                "Nombre": nombre,
                "Cédula": cedula,
                "Celular": celular,
                "Correo": correo,
                "Contraseña": contraseña
            }
            messagebox.showinfo("Registro Exitoso", "El asesor se ha registrado con éxito.")
        else:
            messagebox.showerror("Error", "El usuario ya existe. Por favor, elija otro nombre de usuario.")

    def visualizar_asesores(self):
        visualizar_ventana = tk.Toplevel(self.ventana)
        visualizar_ventana.title("Asesores Registrados")
        
        lista_asesores = tk.Text(visualizar_ventana)
        lista_asesores.pack()
        
        for usuario, datos in self.asesores.items():
            lista_asesores.insert(tk.END, f"Usuario: {usuario}\n")
            for campo, valor in datos.items():
                if campo != "Contraseña":  # Excluir la contraseña
                    lista_asesores.insert(tk.END, f"{campo}: {valor}\n")
            lista_asesores.insert(tk.END, "\n")

    def abrir_ventana_iniciar_sesion(self):
        ventana_iniciar_sesion = tk.Toplevel(self.ventana)
        ventana_iniciar_sesion.title("Iniciar Sesión")

        usuario_label = tk.Label(ventana_iniciar_sesion, text="Usuario:")
        usuario_label.pack()
        usuario_entry = tk.Entry(ventana_iniciar_sesion)
        usuario_entry.pack()

        contraseña_label = tk.Label(ventana_iniciar_sesion, text="Contraseña:")
        contraseña_label.pack()
        contraseña_entry = tk.Entry(ventana_iniciar_sesion, show="*")
        contraseña_entry.pack()

        ingresar_button = tk.Button(ventana_iniciar_sesion, text="Ingresar", command=lambda: self.iniciar_sesion(usuario_entry.get(), contraseña_entry.get()))
        ingresar_button.pack()

        cambiar_contraseña_button = tk.Button(ventana_iniciar_sesion, text="Cambiar Contraseña", command=self.abrir_ventana_cambio_contraseña)
        cambiar_contraseña_button.pack()

    def iniciar_sesion(self, usuario, contraseña):
        if usuario in self.asesores and self.asesores[usuario]["Contraseña"] == contraseña:
            self.usuario_actual = usuario
            messagebox.showinfo("Inicio de Sesión Exitoso", f"Bienvenido, {usuario}!")
            self.abrir_ventana_menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

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

    def abrir_ventana_inventario(self):
        ventana_inventario = tk.Toplevel(self.ventana)
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
        
        # Muestra los datos añadidos
        mostrar_inventario_button = tk.Button(ventana_inventario, text="Mostrar Inventario", command=self.mostrar_inventario)
        mostrar_inventario_button.pack()


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
    
    def mostrar_inventario(self):
        ventana_mostrar_inventario = tk.Toplevel(self.ventana)
        ventana_mostrar_inventario.title("Inventario Registrado")

        lista_inventario = tk.Text(ventana_mostrar_inventario)
        lista_inventario.pack()

        for item in self.inventario:
            lista_inventario.insert(tk.END, f"Estado: {item['Estado']}\n")
            lista_inventario.insert(tk.END, f"Color: {item['Color']}\n")
            lista_inventario.insert(tk.END, f"Tipo: {item['Tipo']}\n")
            lista_inventario.insert(tk.END, f"Cantidad: {item['Cantidad']}\n")
            lista_inventario.insert(tk.END, f"Valor: {item['Valor']}\n")
            lista_inventario.insert(tk.END, f"Código: {item['Código']}\n")
            lista_inventario.insert(tk.END, "\n")



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

        #boton para guardar datos
        guardar_renta_button = tk.Button(ventana_renta, text="Guardar Renta", command=lambda: self.guardar_renta(
        fecha_inicio_entry.get_date(), fecha_finalizacion_entry.get_date(), vestido_entry.get(), observacion_entry.get()))
        guardar_renta_button.pack()
        #boton para mostrar la lista de datos
        mostrar_rentas_button = tk.Button(ventana_renta, text="Mostrar Rentas", command=self.mostrar_rentas)
        mostrar_rentas_button.pack()

    def guardar_renta(self, fecha_inicio, fecha_finalizacion, vestido, observacion):
        renta = {
        "Fecha de Inicio": fecha_inicio,
        "Fecha de Finalización": fecha_finalizacion,
        "Vestido": vestido,
        "Observación": observacion
    }
        self.rentas.append(renta)
        messagebox.showinfo("Renta Registrada", "La renta se ha registrado con éxito.")

    def mostrar_rentas(self):
        ventana_mostrar_rentas = tk.Toplevel(self.ventana)
        ventana_mostrar_rentas.title("Rentas Registradas")

        lista_rentas = tk.Text(ventana_mostrar_rentas)
        lista_rentas.pack()

        for renta in self.rentas:
            lista_rentas.insert(tk.END, f"Fecha de Inicio: {renta['Fecha de Inicio']}\n")
            lista_rentas.insert(tk.END, f"Fecha de Finalización: {renta['Fecha de Finalización']}\n")
            lista_rentas.insert(tk.END, f"Vestido: {renta['Vestido']}\n")
            lista_rentas.insert(tk.END, f"Observación: {renta['Observación']}\n")
            lista_rentas.insert(tk.END, "\n")


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

        # Botón para programar la cita
        programar_cita_button = tk.Button(ventana_cita, text="Programar Cita", command=lambda: self.programar_cita(fecha_cita_entry.get_date(), hora_cita_entry.get()))
        programar_cita_button.pack()

        #boton para mostrar la lista de citas
        mostrar_citas_button = tk.Button(ventana_cita, text="Mostrar Citas", command=self.mostrar_citas)
        mostrar_citas_button.pack()

    def programar_cita(self, fecha, hora):
        horario = f"{fecha} {hora}"
        if horario in self.horarios_ocupados:
            raise HorarioOcupadoException(horario)
        else:
            # Registra el horario y la cita
            self.horarios_ocupados[horario] = "Cita programada"
            mensaje_exito = f"Cita programada para el {fecha} a las {hora}"
            messagebox.showinfo("Cita Programada", mensaje_exito)

    def mostrar_citas(self):
        ventana_mostrar_citas = tk.Toplevel(self.ventana)
        ventana_mostrar_citas.title("Citas Programadas")

        lista_citas = tk.Text(ventana_mostrar_citas)
        lista_citas.pack()

        for horario, estado in self.horarios_ocupados.items():
            lista_citas.insert(tk.END, f"Hora de Cita: {horario}\n")
            lista_citas.insert(tk.END, f"Estado: {estado}\n")
            lista_citas.insert(tk.END, "\n")


    def abrir_ventana_devolucion(self):
        ventana_devolucion = tk.Toplevel(self.ventana)
        ventana_devolucion.title("Registrar Devolución")

        fecha_devolucion_label = tk.Label(ventana_devolucion, text="Fecha de Devolución:")
        fecha_devolucion_label.pack()
        fecha_devolucion_entry = DateEntry(ventana_devolucion)  # Campo de selección de fecha
        fecha_devolucion_entry.pack()

        guardar_devolucion_button = tk.Button(ventana_devolucion, text="Guardar Devolución", command=lambda: self.guardar_devolucion(fecha_devolucion_entry.get_date()))
        guardar_devolucion_button.pack()

        mostrar_devoluciones_button = tk.Button(ventana_devolucion, text="Mostrar Devoluciones", command=self.mostrar_devoluciones)
        mostrar_devoluciones_button.pack()
        
    def guardar_devolucion(self, fecha_devolucion):
        # Agrega la fecha de devolución a la lista
        self.devoluciones.append(fecha_devolucion)

        # Muestra un mensaje de éxito
        mensaje_exito = f"Devolución registrada para el {fecha_devolucion}"
        messagebox.showinfo("Devolución Registrada", mensaje_exito)

    def mostrar_devoluciones(self):
        ventana_mostrar_devoluciones = tk.Toplevel(self.ventana)
        ventana_mostrar_devoluciones.title("Devoluciones Registradas")

        lista_devoluciones = tk.Text(ventana_mostrar_devoluciones)
        lista_devoluciones.pack()

        # Recorre la lista de devoluciones y muestra las fechas
        for fecha_devolucion in self.devoluciones:
            lista_devoluciones.insert(tk.END, f"Fecha de Devolución: {fecha_devolucion}\n")


    def abrir_ventana_pago(self):
        ventana_pago = tk.Toplevel(self.ventana)
        ventana_pago.title("Registrar Pago")

        dinero_total_label = tk.Label(ventana_pago, text="Dinero Total:")
        dinero_total_label.pack()
        dinero_total_entry = tk.Entry(ventana_pago)
        dinero_total_entry.pack()

        concepto_pago_label = tk.Label(ventana_pago, text="Concepto de Pago:")
        concepto_pago_label.pack()
        concepto_pago_entry = tk.Entry(ventana_pago)
        concepto_pago_entry.pack()

        # Botón para guardar el pago
        guardar_pago_button = tk.Button(ventana_pago, text="Guardar Pago", command=lambda: self.guardar_pago(
            float(dinero_total_entry.get()), concepto_pago_entry.get()))
        guardar_pago_button.pack()

        # Botón para mostrar la lista de pagos
        mostrar_pagos_button = tk.Button(ventana_pago, text="Mostrar Pagos", command=self.mostrar_pagos)
        mostrar_pagos_button.pack()

    def guardar_pago(self, monto, concepto):
        if monto < 0:
            raise PagoInvalidoException(monto)
        pago = {
            "Dinero Total": monto,
            "Concepto de Pago": concepto
        }
        self.pagos.append(pago)

        # Muestra un mensaje de éxito
        mensaje_exito = "Pago registrado con éxito."
        messagebox.showinfo("Pago Registrado", mensaje_exito)

    def mostrar_pagos(self):
        ventana_mostrar_pagos = tk.Toplevel(self.ventana)
        ventana_mostrar_pagos.title("Pagos Registrados")

        lista_pagos = tk.Text(ventana_mostrar_pagos)
        lista_pagos.pack()

        # Recorre la lista de pagos y muestra los datos
        for pago in self.pagos:
            lista_pagos.insert(tk.END, "Pago:\n")
            for campo, valor in pago.items():
                lista_pagos.insert(tk.END, f"{campo}: {valor}\n")
            lista_pagos.insert(tk.END, "\n")


    def abrir_ventana_mantenimiento(self):
        ventana_mantenimiento = tk.Toplevel(self.ventana)
        ventana_mantenimiento.title("Registrar Mantenimiento")

        fecha_inicio_label = tk.Label(ventana_mantenimiento, text="Fecha de Inicio:")
        fecha_inicio_label.pack()
        fecha_inicio_entry = DateEntry(ventana_mantenimiento)  # Campo de selección de fecha
        fecha_inicio_entry.pack()

        fecha_fin_label = tk.Label(ventana_mantenimiento, text="Fecha de Fin:")
        fecha_fin_label.pack()
        fecha_fin_entry = DateEntry(ventana_mantenimiento)  # Campo de selección de fecha
        fecha_fin_entry.pack()

        descripcion_label = tk.Label(ventana_mantenimiento, text="Descripción:")
        descripcion_label.pack()
        descripcion_entry = tk.Entry(ventana_mantenimiento)
        descripcion_entry.pack()

        costo_label = tk.Label(ventana_mantenimiento, text="Costo:")
        costo_label.pack()
        costo_entry = tk.Entry(ventana_mantenimiento)
        costo_entry.pack()

         # Botón para guardar el mantenimiento
        guardar_mantenimiento_button = tk.Button(ventana_mantenimiento, text="Guardar Mantenimiento", command=lambda: self.guardar_mantenimiento(
            fecha_inicio_entry.get_date(), fecha_fin_entry.get_date(), descripcion_entry.get(), costo_entry.get()))
        guardar_mantenimiento_button.pack()

        # Botón para mostrar la lista de mantenimientos
        mostrar_mantenimientos_button = tk.Button(ventana_mantenimiento, text="Mostrar Mantenimientos", command=self.mostrar_mantenimientos)
        mostrar_mantenimientos_button.pack()

    def guardar_mantenimiento(self, fecha_inicio, fecha_fin, descripcion, costo):
        # Crea un diccionario con los datos del mantenimiento
        mantenimiento = {
            "Fecha de Inicio": fecha_inicio,
            "Fecha de Fin": fecha_fin,
            "Descripción": descripcion,
            "Costo": costo
        }
        self.mantenimientos.append(mantenimiento)

        # Muestra un mensaje de éxito
        mensaje_exito = "Mantenimiento registrado con éxito."
        messagebox.showinfo("Mantenimiento Registrado", mensaje_exito)

    def mostrar_mantenimientos(self):
        ventana_mostrar_mantenimientos = tk.Toplevel(self.ventana)
        ventana_mostrar_mantenimientos.title("Mantenimientos Registrados")

        lista_mantenimientos = tk.Text(ventana_mostrar_mantenimientos)
        lista_mantenimientos.pack()

        # Recorre la lista de mantenimientos y muestra los datos
        for mantenimiento in self.mantenimientos:
            lista_mantenimientos.insert(tk.END, "Mantenimiento:\n")
            for campo, valor in mantenimiento.items():
                lista_mantenimientos.insert(tk.END, f"{campo}: {valor}\n")
            lista_mantenimientos.insert(tk.END, "\n")    


if __name__ == "__main__":
    ventana = tk.Tk()
    app = CasaVestidosApp(ventana)
    ventana.mainloop()