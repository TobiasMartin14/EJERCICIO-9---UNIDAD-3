class Vehiculo:
    __modelo: str
    __puertas: int
    __color: str
    __precio: float
    
    def __init__(self, modelo, puertas, color, precio):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio = precio
        
    def toJSON(self):
        d = dict(self.__modelo, self.__puertas, self.__color, self.__precio)
        return d
        
    def get_precio(self):
        return self.__precio
    
    def get_modelo(self):
        return self.__modelo
    
    def get_puertas(self):
        return self.__puertas
    
    def get_color(self):
        return self.__color
    
    def modificar_precio_base(self, nuevo_precio):
        self.__precio = nuevo_precio
    
    def __str__(self):
        cadena = 'Modelo:' + self.__modelo + ', Puertas: {}'.format(self.__puertas)+ ', Color:' + self.__color + ', Precio: {}'.format(self.__precio)
        return cadena
    
    def __eq__(self, otro):
        cadena1 = self.get_modelo() + self.get_color() + str(self.get_precio()) + str(self.get_puertas())
        cadena2 = otro.get_modelo() + otro.get_color() + str(otro.get_precio()) + str(otro.get_puertas())
        return cadena1 == cadena2