from os import system
import webbrowser
import os
import easygui as eg
from xml.dom import minidom
from listasimple import LSimple
system("cls")
archivo = ''
matrizcombustible = []
usar = LSimple()
terrenoTrabajar = []
def menu():
    global archivo, matrizcombustible, terrenoTrabajar
    print("Menu principal: \n\t1.Cargar archivo \n\t2.Procesar Archivo\n\t3.Escribir archivo salida \n\t5.Generar Grafica\n\t6.Salir")
    print('--------------------------------------------------')
    lectura = input("Escoja una opcion: ")
    print('--------------------------------------------------')
    if lectura == str(1):
        abrir()
    elif lectura == str(6):
        exit()
    else:
        print("No es una opcion valida")
        menu()

def abrir():
    global archivo
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/USUARIO/Desktop/*xml',
                         filetypes=extension)                      
    eg.msgbox(archivo, "fileopenbox", ok_button="Continuar")
    print('La ruta del archivo selecionada es: ' +archivo)
    #f = open(archivo,'r',encoding="utf8")
    #leer = f.read()
    #f.close()
    menu()

menu()