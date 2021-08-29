import nodo
cn = nodo

class LSimple(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def Agregar(self,x,y,combustible):
        nuevo = cn.Nodo(x,y,combustible)
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
                print(f'fila: {aux.x}  columna: {aux.y}  combustible: {aux.combustible}')
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente
    
    def getCombustible(self,x,y):
        prueba = self.primero
        bandera = True
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                bandera = False
                return prueba.combustible
            else:
                prueba = prueba.siguiente

    def recorrerDerecha(self,x,y):
        prueba = self.primero
        bandera = True
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                bandera = False
                nodo2 = prueba.siguiente
                gas = nodo2.combustible
                arreglo = []
                arreglo.append(prueba.combustible)
                arreglo.append(gas)
                nodo3 = prueba.siguiente.siguiente
                arreglo.append(nodo3.combustible)
                return arreglo
            else:
                prueba = prueba.siguiente
    
    def recorrerabajo(self,x,y):
        prueba = self.primero
        bandera = True
        gas = []
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                variable1 = prueba.combustible
                gas.append(variable1)
                bandera2 = True
                bandera = False
                while bandera2 == True:
                    if (int(prueba.x) == (int(x)+1)) and (int(prueba.y) == int(y)):
                        variable2 = prueba.combustible
                        gas.append(variable2)
                        bandera3 = True
                        bandera2 = False
                        while bandera3 == True:
                            if (int(prueba.x) == (int(x)+2)) and (int(prueba.y) == int(y)):
                                variable3 = prueba.combustible
                                gas.append(variable3)
                                bandera3 = False
                            else:
                                prueba = prueba.siguiente
                    else:
                        prueba = prueba.siguiente   
            else:
                prueba = prueba.siguiente
        return gas

    def recorrerArriba(self,x,y):
        prueba = self.primero
        bandera = True
        gas = []
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                variable1 = prueba.combustible
                gas.append(variable1)
                bandera2 = True
                bandera = False
                while bandera2 == True:
                    if (int(prueba.x) == (int(x)-1)) and (int(prueba.y) == (int(y)-2)):
                        variable2 = prueba.combustible
                        gas.append(variable2)
                        bandera3 = True
                        bandera2 = False
                        while bandera3 == True:
                            if (int(prueba.x) == (int(x)-2)) and (int(prueba.y) == int(y)):
                                variable3 = prueba.combustible
                                gas.append(variable3)
                                bandera3 = False
                            else:
                                prueba = prueba.siguiente
                    else:
                        prueba = prueba.siguiente   
            else:
                prueba = prueba.siguiente
        return gas

    def recorrerIzquierda(self,x,y):
        prueba = self.primero
        bandera = True
        gas = []
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                variable1 = prueba.combustible
                gas.append(variable1)
                bandera2 = True
                bandera = False
                while bandera2 == True:
                    if (int(prueba.x) == (int(x))) and (int(prueba.y) == (int(y)-1)):
                        variable2 = prueba.combustible
                        gas.append(variable2)
                        bandera3 = True
                        bandera2 = False
                        while bandera3 == True:
                            if (int(prueba.x) == (int(x))) and (int(prueba.y) == (int(y)-2)):
                                variable3 = prueba.combustible
                                gas.append(variable3)
                                bandera3 = False
                            else:
                                prueba = prueba.siguiente
                    else:
                        prueba = prueba.siguiente   
            else:
                prueba = prueba.siguiente
        return gas

    def recorrerIzquierdaArriba(self,x,y):
        prueba = self.primero
        bandera = True
        gas = []
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                variable1 = prueba.combustible
                gas.append(variable1)
                bandera2 = True
                bandera = False
                while bandera2 == True:
                    if (int(prueba.x) == (int(x))) and (int(prueba.y) == (int(y)-1)):
                        variable2 = prueba.combustible
                        gas.append(variable2)
                        bandera3 = True
                        bandera2 = False
                        while bandera3 == True:
                            if (int(prueba.x) == (int(x)-1)) and (int(prueba.y) == (int(y)-1)):
                                variable3 = prueba.combustible
                                gas.append(variable3)
                                bandera3 = False
                            else:
                                prueba = prueba.siguiente
                    else:
                        prueba = prueba.siguiente   
            else:
                prueba = prueba.siguiente
        return gas

    def recorrerIzquierdaAbajo(self,x,y):
        prueba = self.primero
        bandera = True
        gas = []
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                variable1 = prueba.combustible
                gas.append(variable1)
                bandera2 = True
                bandera = False
                while bandera2 == True:
                    if (int(prueba.x) == (int(x))) and (int(prueba.y) == (int(y)-1)):
                        variable2 = prueba.combustible
                        gas.append(variable2)
                        bandera3 = True
                        bandera2 = False
                        while bandera3 == True:
                            if (int(prueba.x) == (int(x)+1)) and (int(prueba.y) == (int(y)-1)):
                                variable3 = prueba.combustible
                                gas.append(variable3)
                                bandera3 = False
                            else:
                                prueba = prueba.siguiente
                    else:
                        prueba = prueba.siguiente   
            else:
                prueba = prueba.siguiente
        return gas

    def recorrerDerechaAbajo(self,x,y):
        prueba = self.primero
        bandera = True
        gas = []
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                variable1 = prueba.combustible
                gas.append(variable1)
                bandera2 = True
                bandera = False
                while bandera2 == True:
                    if (int(prueba.x) == (int(x))) and (int(prueba.y) == (int(y)+1)):
                        variable2 = prueba.combustible
                        gas.append(variable2)
                        bandera3 = True
                        bandera2 = False
                        while bandera3 == True:
                            if (int(prueba.x) == (int(x)+1)) and (int(prueba.y) == (int(y)+1)):
                                variable3 = prueba.combustible
                                gas.append(variable3)
                                bandera3 = False
                            else:
                                prueba = prueba.siguiente
                    else:
                        prueba = prueba.siguiente   
            else:
                prueba = prueba.siguiente
        return gas

    def recorrerDerechaArriba(self,x,y):
        prueba = self.primero
        bandera = True
        gas = []
        while (bandera == True):
            if (int(prueba.x) == int(x)) and (int(prueba.y) == int(y)):
                variable1 = prueba.combustible
                gas.append(variable1)
                bandera2 = True
                bandera = False
                while bandera2 == True:
                    if (int(prueba.x) == (int(x))) and (int(prueba.y) == (int(y)+1)):
                        variable2 = prueba.combustible
                        gas.append(variable2)
                        bandera3 = True
                        bandera2 = False
                        while bandera3 == True:
                            if (int(prueba.x) == (int(x)-1)) and (int(prueba.y) == (int(y)+1)):
                                variable3 = prueba.combustible
                                gas.append(variable3)
                                bandera3 = False
                            else:
                                prueba = prueba.siguiente
                    else:
                        prueba = prueba.siguiente   
            else:
                prueba = prueba.siguiente
        return gas

    def borrar(self):
        self.primero = None
        self.ultimo = None