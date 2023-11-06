from modelo.pago import Pago

class Renta:
     def __init__(self, fecha_inicio,fecha_finalizacion, vestido:str, observacion):
        self.fecha_iniciob = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.vestido :str = vestido
        self.observacion = observacion 
        self.pago: list[Pago] = []


     def guardar_renta(self, fecha_inicio,fecha_finalizacion, vestido:str, observacion):
        renta = Renta(fecha_inicio,fecha_finalizacion, vestido, observacion)
        self.renta.append(Renta)

