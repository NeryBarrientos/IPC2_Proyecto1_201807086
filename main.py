import xml.etree.ElementTree as ET
from tkinter import messagebox
import easygui as eg
from os import system
from lista_frecuencias import LSimple_frecuencias
from lista_senales import LSimple_senales
system("cls")
Lista_frecuencias = LSimple_frecuencias()
Lista_senales = LSimple_senales()

# Función para mostrar el menú y obtener la elección del usuario
def main_menu():
    imprimir = '*********************************************'
    imprimir1 = 'Bienvenido'
    mensaje = imprimir.center(75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    print(mensaje)
    print("Menu Principal:")
    print("\t1. Cargar archivo")
    print("\t2. Procesar archivo")
    print("\t3. Escribir archivo salida")
    print("\t4. Mostrar datos del estudiante")
    print("\t5. Generar gráfica")
    print("\t6. Inicializar sistema")
    print("\t7. Salida")
    
    while True:
        try:
            opcion = int(input("Por favor, elija una opción (1-7): "))
            if opcion < 1 or opcion > 7:
                print("Opción no válida. Por favor, ingrese un número del 1 al 7.")
            else:
                return opcion
        except ValueError:
            print("Entrada no válida. Ingrese un número del 1 al 7.")

def leer_archivo_xml(archivo):
    try:
        tree = ET.ElementTree(ET.fromstring(archivo))

        root = tree.getroot()

        # Iterar a través de las etiquetas "senal"
        for senal in root.findall('senal'):
            nombre = senal.get('nombre')
            t = senal.get('t')
            A = senal.get('A')

            # Crear una nueva instancia de la lista de frecuencias para cada señal
            Lista_frecuencias = LSimple_frecuencias()

            # Iterar a través de las etiquetas "dato" dentro de cada "senal"
            for dato in senal.findall('dato'):
                t_dato = dato.get('t')
                A_dato = dato.get('A')
                valor = dato.text
                
                # Agregar el valor a la lista de frecuencias de la señal actual
                Lista_frecuencias.Agregar(t_dato, A_dato, valor)

            # Agregar la señal con su lista de frecuencias a la lista de señales
            Lista_senales.Agregar(t, A, nombre, Lista_frecuencias)

        # Mostrar las señales y sus listas de frecuencias
        Lista_senales.printLista()

    except Exception as e:
        print(f"Error al procesar el archivo XML: {str(e)}")


def load_file():
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    extension = ["*.xml"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                             title="Control: fileopenbox",
                             default='D:/rec nery/rec nery/Desktop/Nery José Barrientos/Segundo Semestre 2023/ipc2/IPC2_Proyecto1_201807086/*xml',
                             filetypes=extension)

    if archivo:
        mensaje = 'Ruta del Archivo: ' + str(archivo) + '\n\n\n\n\n' + imprimir.center(
            75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
        eg.msgbox(msg=mensaje, title="Mensaje")
        try:
            f = open(archivo, 'r', encoding="utf8")
            contenido = f.read()
            f.close()
            leer_archivo_xml(contenido)
        except Exception as e:
            eg.msgbox(msg=f"Error al leer el archivo XML: {str(e)}", title="Error", ok_button="Aceptar")
    else:
        eg.msgbox(msg="No se seleccionó un archivo.", title="Error", ok_button="Aceptar")


while True:
    opcion = main_menu()
    
    if opcion == 1:
        print("Ha elegido la opción 1: Cargar archivo\n")
        load_file()
    elif opcion == 2:
        print("Ha elegido la opción 2: Procesar archivo")
        # Aquí puedes agregar la lógica para procesar el archivo
    elif opcion == 3:
        print("Ha elegido la opción 3: Escribir archivo salida")
        # Aquí puedes agregar la lógica para escribir el archivo de salida
    elif opcion == 4:
        print("Ha elegido la opción 4: Mostrar datos del estudiante")
        # Aquí puedes agregar la lógica para mostrar los datos del estudiante
    elif opcion == 5:
        print("Ha elegido la opción 5: Generar gráfica")
        # Aquí puedes agregar la lógica para generar una gráfica
    elif opcion == 6:
        print("Ha elegido la opción 6: Inicializar sistema")
        # Aquí puedes agregar la lógica para inicializar el sistema
    elif opcion == 7:
        print("Ha elegido la opción 7: Salida")
        break
