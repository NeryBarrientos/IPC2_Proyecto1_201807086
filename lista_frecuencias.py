import nodo_frecuencias
cn = nodo_frecuencias

class LSimple_frecuencias(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        # Verifica si la lista está vacía
        if self.primero == None:
            return True
        else:
            return False

    def Agregar(self, t, a, valor):
        # Agrega un nuevo nodo a la lista de frecuencias de manera ordenada
        nuevo = cn.NodoFrecuencias(t, a, valor)
        
        # Caso especial: la lista está vacía o el nuevo valor debe ir al principio
        if self.vacio() or (t, a) < (self.primero.t, self.primero.a):
            nuevo.siguiente = self.primero
            self.primero = nuevo
            if self.vacio():
                self.ultimo = nuevo
            return

        actual = self.primero

        while actual.siguiente is not None and (t, a) > (actual.siguiente.t, actual.siguiente.a):
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

        # Si el nuevo valor se inserta al final, actualizamos 'ultimo'
        if nuevo.siguiente is None:
            self.ultimo = nuevo

    def printLista(self):
        # Imprime los valores de la lista de frecuencias
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

    def convertir_a_matriz(self):
        if self.vacio():
            print('Lista Vacia')
            return []

        # Encuentra el tamaño máximo necesario para crear la matriz
        max_t = 0
        max_a = 0
        aux = self.primero
        while aux is not None:
            max_t = max(max_t, int(aux.t))
            max_a = max(max_a, int(aux.a))
            aux = aux.siguiente

        # Crea una matriz llena de ceros con las dimensiones necesarias
        matriz = [[0 for _ in range(max_a)] for _ in range(max_t)]

        # Rellena la matriz con los valores de los nodos, restando 1 a t y a
        aux = self.primero
        while aux is not None:
            matriz[int(aux.t) - 1][int(aux.a) - 1] = int(aux.valor)  # Resta 1 a t y a
            aux = aux.siguiente

        return matriz



    def encontrar_filas_iguales(self, matriz):
        # Encuentra filas iguales en la matriz y las agrega a una lista de grupos de filas iguales
        filas_iguales = []

        for i in range(len(matriz)):
            if i not in [fila for grupo in filas_iguales for fila in grupo]:
                # Si esta fila no se ha incluido en grupos anteriores
                grupo = [i]
                fila_actual = matriz[i]

                for j in range(i + 1, len(matriz)):
                    if fila_actual == matriz[j]:
                        grupo.append(j)

                if len(grupo) > 1:
                    # Si encontramos al menos una fila igual, agregamos el grupo a la lista
                    filas_iguales.append(grupo)

        return filas_iguales

    def comparar_binaria(self):
        # Convierte la lista de frecuencias en una matriz
        matriz = self.convertir_a_matriz()
        # print('Matriz Binaria')
        # print(matriz)
        # Encuentra las filas iguales en la matriz
        iguales = self.encontrar_filas_iguales(matriz)
        # print('Filas iguales')
        # print(iguales)
        return iguales

    def convertir_a_lista(self):
        lista_datos = []

        actual = self.primero
        while actual is not None:
            dato = {
                "tiempo": actual.t,
                "amplitud": actual.a,
                "valor": actual.valor
            }
            lista_datos.append(dato)
            actual = actual.siguiente

        return lista_datos

    def borrar(self):
        # Borra todos los elementos de la lista de frecuencias
        self.primero = None
        self.ultimo = None
