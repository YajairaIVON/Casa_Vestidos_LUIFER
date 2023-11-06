from modelo.renta import Renta
from modelo.mantenimiento import Mantenimiento
from modelo.devolucion import Devolucion

class Vestido:
     
     def __init__(self, color:str, tipo:str, cantidad:int, valor:float, estado:str, codigo:int):
        self.color: str = color
        self.tipo:str = tipo
        self.cantidad :int = cantidad 
        self.valor:float = valor 
        self.estado:str = estado
        self.codigo:int = codigo
        self.rentas : list[Renta] = []
        self.mantenimiento : list[Mantenimiento] = []
        self.devolucion : list[Devolucion] = []

     def registrar_mantenimiento(self, fecha_inicio,fecha_fin, descripcion, costo):
        mantenimiento = Mantenimiento(fecha_inicio,fecha_fin, descripcion, costo)
        self.mantenimiento.append(Mantenimiento)

     def registrar_renta(self, fecha_inicio,fecha_finalizacion, vestido:str, observacion):
        renta = Renta(fecha_inicio,fecha_finalizacion, vestido, observacion)
        self.renta.append(Renta)

     def registrar_devolucion(self, fecha_devolucion):
         devolucion = Devolucion(fecha_devolucion)
         self.devolucion.append(Devolucion)
         


