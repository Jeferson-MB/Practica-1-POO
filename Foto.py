from User import User
class Foto:
    def __init__(self, UbicacionArchivo: str, TipoArchivo: str, Tamano:str):
        self.UbicacionArchico = UbicacionArchivo
        self.TipoArchivo = TipoArchivo
        self.Tamano = Tamano

    def __str__(self):
        return f""" 
        {self.UbicacionArchico} ({self.TipoArchivo}, {self.Tamano}KB)
        """
    

        