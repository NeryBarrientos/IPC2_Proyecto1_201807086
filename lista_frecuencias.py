import nodo_frecuencias
cn = nodo_frecuencias

class LSimple_frecuencias(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False
    def Agregar(self,t,a,valor):
        nuevo = cn.NodoFrecuencias(t,a,valor)
        if self.vacio():
            self.primero = self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero

    def printLista(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.valor}')
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente
    def borrar(self):
        self.primero = None
        self.ultimo = None