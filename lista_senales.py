import nodo_senales
from lista_frecuencias import LSimple_frecuencias
cn = nodo_senales

class LSimple_senales(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False

    # Agrega una señal a la lista de señales
    def Agregar(self,t,a,nombre,frecuencias):
        nuevo = cn.NodoSenales(t,a,nombre,frecuencias)
        if self.vacio():
            self.primero = self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero

    # Convierte las frecuencias de cada señal a binario (0 o 1) y actualiza la lista de señales con los valores binarios
    def agregar_binaria(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                nueva_binaria = LSimple_frecuencias()  # Crea una nueva instancia de LSimple_frecuencias para binaria
                actual = aux.frecuencias.primero
                while actual is not None:
                    # Aplica la condición: si el valor es diferente de 0, valor = 1, de lo contrario, es 0
                    valor_modificado = 1 if int(actual.valor) != 0 else 0
                    nueva_binaria.Agregar(actual.t, actual.a, valor_modificado)
                    actual = actual.siguiente

                aux.binaria = nueva_binaria  # Asigna la nueva instancia de LSimple_frecuencias a binaria
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    # Imprime la lista de señales junto con sus valores de frecuencias
    def printLista(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                aux.frecuencias.printLista()
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    # Imprime la lista de señales junto con sus valores binarios
    def imprimir_binaria(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                aux.binaria.printLista()
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    # Procesa las señales binarias e imprime las filas que son iguales entre señales
    def procesar_binaria(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                aux.binaria.comparar_binaria()
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

                    
