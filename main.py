import xml.etree.ElementTree as ET
from tkinter import messagebox
import easygui as eg
from os import system
from lista_frecuencias import LSimple_frecuencias
from lista_senales import LSimple_senales
import time
import sys

archivo_procesado = False

# Limpiar la pantalla
system("cls")

# Inicializar las listas
Lista_frecuencias = LSimple_frecuencias()
Lista_senales = LSimple_senales()

# Función para mostrar el menú y obtener la elección del usuario
def main_menu():
    # Mensaje de bienvenida
    imprimir = '*********************************************'
    imprimir1 = 'Bienvenido'
    mensaje = imprimir.center(75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    print(mensaje)
    
    # Menú principal
    print("Menu Principal:")
    print("\t1. Cargar archivo")
    print("\t2. Procesar archivo")
    print("\t3. Escribir archivo salida")
    print("\t4. Mostrar datos del estudiante")
    print("\t5. Generar gráfica")
    print("\t6. Inicializar Sitema")
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

# Función para leer y procesar el archivo XML
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
                
                # Agregar el valor a la lista de frecuencias de la señal actual de manera ordenada
                Lista_frecuencias.Agregar(t_dato, A_dato, valor)
            
            # Agregar la señal con su lista de frecuencias a la lista de señales
            Lista_senales.Agregar(t, A, nombre, Lista_frecuencias)
    
    except Exception as e:
        print(f"Error al procesar el archivo XML: {str(e)}")

# Función para cargar un archivo XML
def load_file():
    # Mensaje de éxito al cargar el archivo
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    
    # Extensiones permitidas
    extension = ["*.xml"]
    
    # Diálogo para seleccionar un archivo
    archivo = eg.fileopenbox(msg="Abrir archivo",
                             title="Control: fileopenbox",
                             default='D:/rec nery/rec nery/Desktop/Nery José Barrientos/Segundo Semestre 2023/ipc2/IPC2_Proyecto1_201807086/*xml',
                             filetypes=extension)
    
    if archivo:
        mensaje = 'Ruta del Archivo: ' + str(archivo) + '\n\n\n\n\n' + imprimir.center(
            75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
        eg.msgbox(msg=mensaje, title="Mensaje")
        try:
            # Leer el contenido del archivo XML y procesarlo
            f = open(archivo, 'r', encoding="utf8")
            contenido = f.read()
            f.close()
            leer_archivo_xml(contenido)
        except Exception as e:
            # Mostrar mensaje de error si ocurre un problema al leer el archivo
            eg.msgbox(msg=f"Error al leer el archivo XML: {str(e)}", title="Error", ok_button="Aceptar")
    else:
        eg.msgbox(msg="No se seleccionó un archivo.", title="Error", ok_button="Aceptar")


def update_progress_bar(iteration, total, bar_length=50):
    progress = iteration / total
    arrow = '=' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f'\r[{arrow + spaces}] {int(progress * 100)}%')
    sys.stdout.flush()

def process_data_with_progress():
    total_steps = 100
    for i in range(total_steps + 1):
        update_progress_bar(i, total_steps)
        time.sleep(0.02)  # Simular 2 segundos en total
    eg.msgbox(msg="Archivo Procesado Correctamente.", title="Procesado", ok_button="Aceptar")

# Función para procesar los datos
def process_data():
    # Llamar a la función para procesar datos con barra de progreso
    process_data_with_progress()
    print()
    Lista_senales.agregar_binaria()
    Lista_senales.procesar_binaria()
    return True

def out_xml():
    diccionario = Lista_senales.convertir_reducida_a_diccionario()
    Lista_senales.generar_xml(diccionario)

def mostrar_datos_personales():
    print("Datos Personales:")
    print("\tNombre: Nery José Barrientos Posadas")
    print("\tCarne: 201807086")
    print("\tCurso: Lab. IPC 2")
    print("\tSección: A")

def new_system():
    Lista_senales.borrar()
    eg.msgbox(msg="Se inicializó el Sistema", title="Inicializar", ok_button="Aceptar")

def generar_grafica():
    while True:
        try:
            Lista_senales.mostrar_nombres()
            opcion = input("Por favor, elija el nombre de la señal: ")
            if not Lista_senales.buscar_nombre(opcion):
                print("Entrada no válida. Ingrese un nombre válido.")
            else:
                Lista_senales.graph_generate(opcion)
                Lista_senales.graph_generate_reducida(opcion)
                eg.msgbox(msg="Graficas Generadas Correctamente.", title="Graficas", ok_button="Aceptar")
                break
        except ValueError:
            print("Entrada no válida. Ingrese un nombre válido.")

# Bucle principal
while True:
    opcion = main_menu()
    
    if opcion == 1:
        print("Ha elegido la opción 1: Cargar archivo\n")
        load_file()
    elif opcion == 2:
        print("Ha elegido la opción 2: Procesar archivo")
        if Lista_senales.vacio():
            print("No se ha cargado ningun archivo")
        else:
            archivo_procesado = process_data()
    elif opcion == 3:
        print("Ha elegido la opción 3: Escribir archivo salida")
        if Lista_senales.vacio():
            print("No se ha cargado ningun archivo")
        else:
            out_xml()
    elif opcion == 4:
        print("Ha elegido la opción 4: Mostrar datos del estudiante")
        mostrar_datos_personales()
    elif opcion == 5:
        print("Ha elegido la opción 5: Generar gráfica")
        if Lista_senales.vacio() or not archivo_procesado:
            print("No se ha cargado ningun archivo")
        else:
            generar_grafica()
    elif opcion == 6:
        print("Ha elegido la opción 6: Inicializar el Sistema")
        new_system()
    elif opcion == 7:
        print("Ha elegido la opción 6: Salida")
        break  # Salir del bucle al elegir la opción 6
