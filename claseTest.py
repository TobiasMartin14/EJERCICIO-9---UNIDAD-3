import unittest
from claseManejador import ManejadorV
from claseNuevo import Nuevo
from claseUsado import Usado

class TestVehiculos(unittest.TestCase):

    def setUp(self):
        self.__vehiculos = ManejadorV()
        unAuto = Nuevo('Toyota', 'Corolla', 5, 'Gris', 1000000, 'full')
        self.__vehiculos.agregar_vehiculo(unAuto)
        unAuto = Usado('Ford', 'Focus', 5, 'Azul', 500000, 'MLO-409', 2012, 50000)
        self.__vehiculos.agregar_vehiculo(unAuto)
        unAuto = Nuevo('Toyota', 'Etios', 5, 'Blanco Perlado', 760000, 'base')
        self.__vehiculos.agregar_vehiculo(unAuto)
        
    def test_insertarElemento1(self):
        #insertar al final
        vehiculo = Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
        posicion = 3
        self.__vehiculos.insertar_vehiculo(vehiculo, posicion)
        lista_vehiculos = self.__vehiculos.generar_lista_python()
        
        lista_test = [Nuevo('Toyota', 'Corolla', 5, 'Gris', 1000000, 'full'),
                      Usado('Ford', 'Focus', 5, 'Azul', 500000, 'MLO-409', 2012, 50000),
                      Nuevo('Toyota', 'Etios', 5, 'Blanco Perlado', 760000, 'base'),
                      Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
                      ]
        
        # print(lista_vehiculos)
        # for vehiculo in lista_vehiculos:
        #     print(vehiculo)
        # print('')
        # print('----------------------------------------------------------------------------')
        # print('')
        # print(lista_test)
        # for vehiculo in lista_test:
        #     print(vehiculo)
            
        self.assertListEqual(lista_vehiculos, lista_test)
    
    
    def test_insertarElemento2(self):
         #insertar al principio
         vehiculo = Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
         posicion = 0
         self.__vehiculos.insertar_vehiculo(vehiculo, posicion)
         lista_vehiculos = self.__vehiculos.generar_lista_python()
         lista_test = []
         unAuto = Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
         lista_test.append(unAuto)
         unAuto = Nuevo('Toyota', 'Corolla', 5, 'Gris', 1000000, 'full')
         lista_test.append(unAuto)
         unAuto = Usado('Ford', 'Focus', 5, 'Azul', 500000, 'MLO-409', 2012, 50000)
         lista_test.append(unAuto)
         unAuto = Nuevo('Toyota', 'Etios', 5, 'Blanco Perlado', 760000, 'base')
         lista_test.append(unAuto)
         self.assertListEqual(lista_vehiculos, lista_test)
        
    def test_insertarElemento3(self):
         #insertar en el medio
         vehiculo = Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
         posicion = 1
         self.__vehiculos.insertar_vehiculo(vehiculo, posicion)
         lista_vehiculos = self.__vehiculos.generar_lista_python()
         lista_test = []
         unAuto = Nuevo('Toyota', 'Corolla', 5, 'Gris', 1000000, 'full')
         lista_test.append(unAuto)
         unAuto = Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
         lista_test.append(unAuto)
         unAuto = Usado('Ford', 'Focus', 5, 'Azul', 500000, 'MLO-409', 2012, 50000)
         lista_test.append(unAuto)
         unAuto = Nuevo('Toyota', 'Etios', 5, 'Blanco Perlado', 760000, 'base')
         lista_test.append(unAuto)
         self.assertListEqual(lista_vehiculos, lista_test)
    
    def test_agregar_elemento(self):
         #Agregar Vehiculo a la Lista
         vehiculo = Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
         self.__vehiculos.agregar_vehiculo(vehiculo)
         lista_vehiculos = self.__vehiculos.generar_lista_python()
       
         lista_test = []
         unAuto = Nuevo('Toyota', 'Corolla', 5, 'Gris', 1000000, 'full')
         lista_test.append(unAuto)
         unAuto = Usado('Ford', 'Focus', 5, 'Azul', 500000, 'MLO-409', 2012, 50000)
         lista_test.append(unAuto)
         unAuto = Nuevo('Toyota', 'Etios', 5, 'Blanco Perlado', 760000, 'base')
         lista_test.append(unAuto)
         unAuto = Usado('Ford', 'Mustang', 3, 'Negro Mate', 2000000, 'PDF-507', 2016, 40000)
         lista_test.append(unAuto) 
         
         self.assertListEqual(lista_vehiculos, lista_test)
         
    def test_obtener_elemento(self):
        vehiculo = self.__vehiculos.mostrarVehiculo(0)
        unAuto = Nuevo('Toyota', 'Corolla', 5, 'Gris', 1000000, 'full')
        self.assertEqual(vehiculo, unAuto)
        
    def test_modificar_precio(self):
        self.assertEqual(self.__vehiculos.modificar_precio('MLO-409', 30000), 26700)
        
        
       

