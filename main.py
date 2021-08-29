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
    elif lectura == str(2):
    
    elif lectura == str(3):
        c=1
    elif lectura == str(4):
        print('Nery José Barrientos Posadas\n201807086\nIntroducción a la computacion 2 sección "A"\nIngenieria en ciencias y sistemas\n4to semestre')
        menu()
    elif lectura == str(5):
        temporal = 'graph grid {\n'
        docxml = minidom.parse(archivo)
        terrenos = docxml.getElementsByTagName("terreno")
        print('Lista terrenos:')
        for terreno in terrenos:
            print(terreno.getAttribute("nombre"))
        lectura = input('Escoja el terreno a trabajar: ')
        for terreno in terrenos:
            if lectura in (terreno.getAttribute("nombre")):
                tamfila = terreno.getElementsByTagName("n")[0].firstChild.data
                tamcolumna = terreno.getElementsByTagName("m")[0].firstChild.data
                for element in (terreno.getElementsByTagName("posicion")):
                    fila = element.getAttribute("x")
                    columna = element.getAttribute("y")
                    combustible = element.firstChild.data
                    usar.Agregar(fila,columna,combustible)
                #usar.printLista()
                prueba = []
                for i in range(int(tamfila)):
                    prueba1 = []
                    for j in range(int(tamcolumna)):
                        gas = usar.getCombustible(i+1,j+1)
                        prueba1.append(gas)
                    prueba.append(prueba1)
                #print(prueba)
        temporal += 'label = "' + lectura + '"\n'
        if int(tamfila) == int(tamcolumna):
            contador = 0
            for i in range(int(tamfila)):
                for j in range(int(tamcolumna)):
                    temporal += f'a{contador} [label = "{prueba[i][j]}"];\n'
                    contador += 1 
            contador = 0
            for i in range(int(tamfila)):
                temporal += f'a{contador}-- '
                cont2 = 0 + contador
                contador += 1
                for j in range(int(tamcolumna)-1):
                    if (j+1) == (int(tamcolumna)-1):
                        cont2 += int(tamfila)
                        temporal += f'a{cont2} \n'
                    else:
                        cont2 += int(tamfila)
                        temporal += f'a{cont2} -- '
            contador = 0
            for i in range(int(tamfila)):
                temporal += 'rank=same{a'+ str(contador) + '--'
                contador += 1
                for j in range(int(tamcolumna)-1):
                    if (j+1) == (int(tamcolumna)-1):
                        temporal += f'a{contador} '
                        temporal += '}\n'
                        contador +=1
                    else:
                        temporal += f'a{contador} -- '
                        contador += 1
        elif int(tamfila) > int(tamcolumna):
            contador = 0
            for i in range(int(tamfila)):
                for j in range(int(tamcolumna)):
                    temporal += f'a{contador} [label = "{prueba[i][j]}"];\n'
                    contador += 1 
            contador = 0
            for i in range(int(tamcolumna)):
                temporal += f'a{contador} -- '
                cont2 = 0 + contador
                contador += 1
                for j in range(int(tamfila)-1):
                    if (j+1) == (int(tamfila)-1):
                        cont2 += (int(tamcolumna))
                        temporal += f'a{cont2} \n'
                    else:
                        cont2 += int(tamcolumna)
                        temporal += f'a{cont2} -- '
            contador = 0
            for i in range(int(tamfila)):
                temporal += 'rank=same{a'+ str(contador) + '--'
                contador += 1
                for j in range(int(tamcolumna)-1):
                    if (j+1) == (int(tamcolumna)-1):
                        temporal += f'a{contador} '
                        temporal += '}\n'
                        contador +=1
                    else:
                        temporal += f'a{contador} -- '
                        contador += 1
        elif int(tamfila) < int(tamcolumna):
            print('prueba')
            contador = 0
            for i in range(int(tamfila)):
                for j in range(int(tamcolumna)):
                    temporal += f'a{contador} [label = "{prueba[i][j]}"];\n'
                    contador += 1 
            contador = 0
            contador = 0
            for i in range(int(tamcolumna)):
                temporal += f'a{contador}-- '
                cont2 = 0 + contador
                contador += 1
                for j in range(int(tamfila)-1):
                    if (j+1) == (int(tamfila)-1):
                        cont2 += int(tamcolumna)
                        temporal += f'a{cont2} \n'
                    else:
                        cont2 += int(tamcolumna)
                        temporal += f'a{cont2} -- '
            contador = 0
            for i in range(int(tamfila)):
                temporal += 'rank=same{a'+ str(contador) + '--'
                contador += 1
                for j in range(int(tamfila)):
                    if (j+1) == (int(tamfila)):
                        temporal += f'a{contador} '
                        temporal += '}\n'
                        contador +=1
                    else:
                        temporal += f'a{contador} -- '
                        contador += 1
        else:
            print('Es otro caso')            
        temporal += '\n}'
        grapho = open("grapho.txt","w")
        grapho.write(temporal)
        grapho.close()
        comando = 'dot -Tpdf grapho.txt -o grapho.pdf'
        os.system(comando)
        webbrowser.open_new_tab('grapho.pdf')
        temporal = ''
        usar.borrar()
        menu()
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