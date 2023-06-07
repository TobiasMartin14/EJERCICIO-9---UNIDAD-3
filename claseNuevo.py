from claseVehiculo import Vehiculo

class Nuevo(Vehiculo):
    __marca: str
    __version: str
    
    def __init__(self, marca, modelo, puertas, color, preciobase, version):
        super().__init__(modelo, puertas, color, preciobase)
        self.__marca = marca
        self.__version = version
        
    def __str__(self):
        cadena = super().__str__()
        cadena += ', Marca: ' + self.__marca + ', Version: ' + self.__version
        return cadena
    
    def __eq__(self, otro):
        bandera = False
        if super().__eq__(otro):
            cadena1 = self.get_marca() + self.get_version()
            cadena2 = otro.get_marca() + otro.get_version()
            bandera = cadena1 == cadena2
        return bandera
    
    def get_marca(self):
        return self.__marca
    
    def get_version(self):
        return self.__version
    
    def toJSON(self):
        d = super().toJSON()
        c = dict(**d, marca = self.__marca, version = self.__version)
        return c
    
    @classmethod
    def set_cls_marca(self, marca):
        self.__marca = marca
    
    def get_precio(self)->float:
        precio_base = super().get_precio()
        precio_total = precio_base * 0.1
        if self.__version == 'full':
            precio_total += precio_base * 0.02
        return precio_total