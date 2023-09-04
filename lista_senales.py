import nodo_senales
from lista_frecuencias import LSimple_frecuencias
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import easygui as eg
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

    def imprimir_reducida(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                # Imprimir información de la señal y sus valores binarios
                print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                aux.reducida.printLista()
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
                # print(f'Tiempo: {aux.t}  Amplitud: {aux.a}  Valor: {aux.nombre}')
                # print('Matriz Original')
                matriz_original = aux.frecuencias.convertir_a_matriz()
                # for i in matriz_original:
                    # print(i)
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
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    def convertir_reducida_a_diccionario(self):
        if self.vacio():
            return {}  # Devolver un diccionario vacío si la lista está vacía

        diccionario_resultante = []

        validar = True
        aux = self.primero

        while validar:
            datos_senal = {
                "Tiempo": aux.t,
                "Amplitud": aux.a,
                "Nombre": aux.nombre,
                "datos": aux.reducida.convertir_a_lista()
            }

            diccionario_resultante.append(datos_senal)

            if aux == self.ultimo:
                validar = False
            else:
                aux = aux.siguiente

        return diccionario_resultante

    def generar_xml(self, diccionario):
        # Crear el elemento raíz
        senalesReducidas = ET.Element("senalesReducidas")

        for senal in diccionario:
            senal_element = ET.SubElement(senalesReducidas, "senal", nombre=senal["Nombre"], A=senal["Amplitud"])

            grupos = self.agrupar_por_tiempo(senal["datos"])

            for i, grupo in enumerate(grupos, start=1):
                grupo_element = ET.SubElement(senal_element, "grupo", g=str(i))
                tiempos_element = ET.SubElement(grupo_element, "tiempos")
                tiempos_element.text = grupo["tiempo"]

                datosGrupo_element = ET.SubElement(grupo_element, "datosGrupo")

                for dato in grupo["datos"]:
                    dato_element = ET.SubElement(datosGrupo_element, "dato", A=str(dato["amplitud"]))
                    dato_element.text = str(dato["valor"])

        # Crear un objeto ElementTree
        tree = ET.ElementTree(senalesReducidas)

        # Obtener una cadena XML con formato legible
        xml_string = minidom.parseString(ET.tostring(senalesReducidas)).toprettyxml(indent="  ")

        # Abre el cuadro de diálogo para guardar el archivo XML
        archivo_guardar = eg.filesavebox(msg="Guardar archivo XML",
                                         title="Guardar XML",
                                         default='D:/rec nery/rec nery/Desktop/Nery José Barrientos/Segundo Semestre 2023/ipc2/IPC2_Proyecto1_201807086/*xml',
                                         filetypes=["*.xml"])  # Definir la extensión .xml aquí

        if archivo_guardar:
            # Agregar la extensión .xml si no está presente en el nombre del archivo
            if not archivo_guardar.endswith(".xml"):
                archivo_guardar += ".xml"

            # Guardar la cadena XML formateada en el archivo seleccionado
            with open(archivo_guardar, "w") as xml_file:
                xml_file.write(xml_string)

            eg.msgbox(msg="Archivo XML guardado exitosamente.", title="Éxito", ok_button="Aceptar")
        else:
            eg.msgbox(msg="No se seleccionó una ubicación para guardar el archivo XML.", title="Error", ok_button="Aceptar")

    def agrupar_por_tiempo(self, datos):
        grupos = []

        for dato in datos:
            encontrado = False
            for grupo in grupos:
                if grupo["tiempo"] == dato["tiempo"]:
                    grupo["datos"].append(dato)
                    encontrado = True
                    break

            if not encontrado:
                grupos.append({"tiempo": dato["tiempo"], "datos": [dato]})

        return grupos

    def borrar(self):
        # Borra todos los elementos de la lista de frecuencias
        self.primero = None
        self.ultimo = None