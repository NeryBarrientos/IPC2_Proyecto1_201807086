import nodo_senales
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
    def Agregar(self,t,a,nombre,frecuencias):
        nuevo = cn.NodoSenales(t,a,nombre,frecuencias)
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
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                aux.frecuencias.printLista()
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente