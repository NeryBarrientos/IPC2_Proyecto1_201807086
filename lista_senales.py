import nodo_senales
from lista_frecuencias import LSimple_frecuencias
cn = nodo_senales

class LSimple_senales(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        return self.primero is None  # Comprobar si la lista está vacía

    def Agregar(self, t, a, nombre, frecuencias):
        # Agregar una nueva señal a la lista de señales
        nuevo = cn.NodoSenales(t, a, nombre, frecuencias)
        if self.vacio():
            self.primero = self.ultimo = nuevo
            self.ultimo.siguiente = self.primero  # Hacer que el último nodo apunte al primero
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero  # Hacer que el último nodo apunte al primero

    def agregar_binaria(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                nueva_binaria = LSimple_frecuencias()  # Crear una nueva instancia para señales binarias
                actual = aux.frecuencias.primero
                while actual is not None:
                    # Convierte las frecuencias a binario (0 o 1)
                    valor_modificado = 1 if int(actual.valor) != 0 else 0
                    nueva_binaria.Agregar(actual.t, actual.a, valor_modificado)
                    actual = actual.siguiente

                aux.binaria = nueva_binaria  # Asignar la nueva instancia de señales binarias
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    def printLista(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                # Imprimir información de la señal y sus frecuencias
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                aux.frecuencias.printLista()
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    def imprimir_binaria(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                # Imprimir información de la señal y sus valores binarios
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                aux.binaria.printLista()
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    def mostrar_matriz_sin_duplicados(self, matriz):
        filas_vistas = set()
        matriz_sin_duplicados = []

        for fila in matriz:
            fila_tupla = tuple(fila)  # Convierte la fila en una tupla para eliminar duplicados

            if fila_tupla not in filas_vistas:
                filas_vistas.add(fila_tupla)
                matriz_sin_duplicados.append(list(fila_tupla))

        return matriz_sin_duplicados

    def procesar_binaria(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1

            while validar:
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                print('Matriz Original')
                matriz_original = aux.frecuencias.convertir_a_matriz()
                for i in matriz_original:
                    print(i)
                lista_filas_iguales = aux.binaria.comparar_binaria()

                # Crear una nueva instancia de LSimple_frecuencias para 'reducida'
                nueva_reducida = LSimple_frecuencias()

                for grupo_filas in lista_filas_iguales:
                    # Sumar las filas correspondientes en la matriz original y agregar el resultado a la matriz resultado
                    suma_fila = [sum(filas) for filas in zip(*(matriz_original[i] for i in grupo_filas))]

                    # Convertir los índices de filas iguales a texto, por ejemplo, [0, 1, 2] a "1,2,3"
                    valor_fila = ",".join(str(fila_idx + 1) for fila_idx in grupo_filas)

                    # Agregar los valores a la instancia de nueva_reducida
                    for col_idx, valor in enumerate(suma_fila):
                        nueva_reducida.Agregar(valor_fila, col_idx + 1, valor)

                # Copiar las filas no afectadas directamente desde la matriz original a 'nueva_reducida'
                filas_no_afectadas = set(range(len(matriz_original))) - set(sum(lista_filas_iguales, []))
                for fila_idx in filas_no_afectadas:
                    for col_idx, valor in enumerate(matriz_original[fila_idx]):
                        nueva_reducida.Agregar(str(fila_idx + 1), col_idx + 1, valor)

                # Asignar 'nueva_reducida' al atributo 'reducida' del nodo actual
                aux.reducida = nueva_reducida
                print('Este es el resultado:')
                nueva_reducida.printLista()

                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente
