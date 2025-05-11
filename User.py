class User:
    def __init__(self, nombre: str, apellidos: str, foto: str,rol):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__foto = foto
        self.__rol = rol
        self.__lugaresFrecuentes = []

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellidos
    
    def setApellido(self, apellido):
        self.__apellidos = apellido

    def getFoto(self):
        return self.__foto 
    
    def setFoto(self, foto):
        self.__foto = foto

    def getRol(self):
        return self.__rol
    
    def setRol(self, rol):
        self.__rol = rol

    def getLugaresFrecuentes(self):
        return self.__lugaresFrecuentes
    
    def setLugaresFreceuntes(self, lugar):
        self.__lugaresFrecuentes.append(lugar)

    def __str__(self):
        lugares = ' '.join(str(lugar) for lugar in self.__lugaresFrecuentes)
        fotos_str = ' '.join(str(foto) for foto in self.__foto)
        roles = '/'.join(rol.value for rol in self.__rol)
        return f"""
        Nombre: {self.__nombre} 
        Apellidos: {self.__apellidos} 
        Usted ocupa el rol de: {roles} \n
        Sus fotos se ubican en: {fotos_str} 
        Usted usualmente frcuenta: {lugares}"""
    
    
        
        
        
