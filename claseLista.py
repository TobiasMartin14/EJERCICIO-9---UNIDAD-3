from zope.interface import implementer
from coleccionInterfaz import IColeccion
from claseNodo import Nodo
from claseVehiculo import Vehiculo
from claseNuevo import Nuevo
from claseUsado import Usado

@implementer(IColeccion)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
        
    def __iter__(self):
        self.__actual = self.__comienzo
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return dato
        
    def insertarVehiculo(self, unVehiculo: Vehiculo, posicion):
        if posicion < 0 or posicion > self.__tope:
            raise Exception('Posicion No valida')
        else:  
            unNodo = Nodo(unVehiculo)
            if posicion == 0:
                unNodo.set_siguiente(self.__comienzo)
                self.__comienzo = unNodo
            else:
                i = 0
                anterior = self.__comienzo
                posterior = self.__comienzo
                while i < posicion and posterior != None:
                    anterior = posterior
                    posterior = posterior.get_siguiente()
                    i += 1
                anterior.set_siguiente(unNodo)
                unNodo.set_siguiente(posterior)
            self.__tope += 1
        
    def agregarVehiculo(self, unVehiculo: Vehiculo):
        unNodo = Nodo(unVehiculo)
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            while aux.get_siguiente() != None:
                aux = aux.get_siguiente()
            aux.set_siguiente(unNodo)
            self.__actual = unNodo
            self.__tope += 1

    def mostrarVehiculo(self, posicion):
        if posicion < 0 or posicion > self.__tope:
            raise Exception('Posicion fuera de rango')
        else:  
            if posicion == 0:
                return self.__comienzo.get_dato()
            else:
                i = 0
                aux = self.__comienzo
                while i < posicion and aux.get_siguiente() != None:
                    aux = aux.get_siguiente()
                    i += 1
                return aux.get_dato()
                
    
    def modificar_precio(self, patente, precio):
        unVehiculo = self.__comienzo.get_dato()
        if isinstance(unVehiculo, Usado):
            if unVehiculo.get_patente() == patente:
                unVehiculo.modificar_precio_base(precio)
        else:
            bandera = False
            aux = self.__comienzo.get_siguiente()
            unVehiculo = aux.get_dato()
            while aux.get_siguiente() != None and not bandera:
                if unVehiculo.get_patente() == patente:
                    bandera = True
                    unVehiculo.modificar_precio_base(precio)
                else:
                    aux = aux.get_siguiente()
                    if aux != None:
                        unVehiculo = aux.get_dato()
            if bandera == False:
                print('La patente ingresada no se encontro')
            else:
                print (unVehiculo.get_precio())
                return unVehiculo.get_precio()
                
    def toJSON(self):
        aux = self.__comienzo
        ld = []
        while aux != None:
            vdic = aux.toJSON()
            ld.append(vdic)
            aux = aux.getSiguiente()
            
    def generar_lista_python(self):
        aux = self.__comienzo
        lista = []
        while aux != None:
            unAuto = aux.get_dato()
            if isinstance(aux, Usado):
                aux: Usado
            elif isinstance(aux, Nuevo):
                aux: Nuevo
            lista.append(unAuto)
            aux = aux.get_siguiente()
        return lista
    

            
                