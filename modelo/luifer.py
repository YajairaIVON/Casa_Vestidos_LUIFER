from modelo.asesor import Asesor
from modelo.vestido import Vestido

class Luifer:

    def __init__(self):
        self.asesores: list[Asesor] = []
        self.vestido: list[Vestido] = []
        self.asesor_en_sesion: Asesor = None # Este es el asesor que tiene la sesion iniciada 


    def registrar_asesor(self, nombre:str, cedula:str,celular:str, correo:str,usuario:str, contrasenha:str):
        asesor = Asesor(nombre,cedula, celular, correo, usuario, contrasenha)
        self.asesores.append(asesor)
    
    def registrar_vestido(self, color:str, tipo:str,cantidad:int, valor:float, estado:str, codigo:str):
        vestido = Vestido(color, tipo, cantidad,valor, estado, codigo)
        self.vestido.append(vestido)
    