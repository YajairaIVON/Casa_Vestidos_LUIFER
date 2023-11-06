from modelo.cita import Cita

class Asesor: 
    def __init__(self, nombre:str, cedula:str, celular:int, correo:str,usuario:str, contrasenha:str):
        self.nombre: str = nombre
        self.cedula:str = cedula
        self.celular : int = celular 
        self.correo:str = correo 
        self.usuario:str = usuario 
        self.contrasenha:str = contrasenha 
        self.citas: list[Cita] = []
        
    def programar_cita(self, fecha_cita, hora_cita):
        cita = Cita(fecha_cita, hora_cita)
        self.citas.append(cita)
    
    def iniciar_sesion(self, nombre_usuario:str, contraseña:str)->bool:
        if nombre_usuario == self.usuario:
            if contraseña == self.contrasenha:
                return True
        return False
    def cambio_contraseña(self, nueva_contraseña:str):
        self.contrasenha = nueva_contraseña
        
     

