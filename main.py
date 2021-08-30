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
posix = 0
posiy = 0
posfx = 0
posfy = 0
tamfila = 0
tamcolumna = 0

def sumaGas(combustible):
    suma = 0
    for gas in combustible:
        suma += int(gas)
    return suma

def menu():
    global archivo, matrizcombustible, terrenoTrabajar, posix, posiy,posfx,posfy, tamfila,tamcolumna
    print("Menu principal: \n\t1.Cargar archivo \n\t2.Procesar Archivo\n\t3.Escribir archivo salida \n\t5.Generar Grafica\n\t6.Salir")
    print('--------------------------------------------------')
    lectura = input("Escoja una opcion: ")
    print('--------------------------------------------------')
    if int(lectura) == 1:
        abrir()
    elif int(lectura) == 2:
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
                posix = int(terreno.getElementsByTagName("x")[0].firstChild.data)
                posiy = int(terreno.getElementsByTagName("y")[0].firstChild.data)
                posfx = int(terreno.getElementsByTagName("x")[1].firstChild.data)
                posfy = int(terreno.getElementsByTagName("y")[1].firstChild.data)
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
                print(prueba)
        #temp = usar.recorrerDerecha(4,4)
        #temp1 = usar.recorrerabajo(4,4)
        #print(str(posix) + ',' + str(posiy) + ' ' + str(posfx) + ',' + str(posfy))
        #print(temp1)
        direccion = 'inicio'
        arreglopos = []
        arreglogas = []
        posicionfinal = str(posfx) + ',' + str(posfy)
        while posicionfinal not in arreglopos:
            #-------------------------------Esquinas---------------------------------Amarillo
            if ((int(posix)-1) == 0) and ((int(posiy)-1) ==0):
                if direccion in 'inicio':
                    v1 = sumaGas(usar.recorrerDerecha(posix,posiy))
                    v2 = sumaGas(usar.recorrerabajo(posix,posiy))
                    if v1 < v2:
                        direccion = 'derecha'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posiy += 1
                    else:
                        direccion = 'abajo'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posix += 1
                elif direccion in 'izquierda':
                    v1 = sumaGas(usar.recorrerabajo(posix,posiy))
                    direccion = 'abajo'
                    actual = str(posix) + ',' + str(posiy)
                    arreglopos.append(actual)
                    print(f'posiciones = {arreglopos}')
                    arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                    print(f'gasolinas {arreglogas}')
                    posix += 1
                elif direccion in 'arriba':
                    v1 = sumaGas(usar.recorrerDerecha(posix,posiy))
                    direccion = 'derecha'
                    actual = str(posix) + ',' + str(posiy)
                    arreglopos.append(actual)
                    print(f'posiciones = {arreglopos}') 
                    arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                    print(f'gasolinas {arreglogas}')
                    posiy += 1
            #elif ((int(posix)-1) ==0) and (((int(posiy)+1) > int(tamcolumna)):
            #elif ((int(posix)+1) > int(tamfila)) and ((int(posiy)-1) ==0):
            #elif ((int(posix)+1) > int(tamfila)) and ((int(posiy)+1) > int(tamcolumna):
                #-------------------------------orillaesquinax---------------------------------Anaranjado
            #elif ((int(posix)-1) == 0) and ((int(posiy)-2) == 0):
            #elif ((int(posix)-1) == 0) and ((int(posiy)+2) > int(tamcolumna)):
            #elif ((int(posix)+1) > int(tamfila)) and ((int(posiy)-1) == 0:
            #elif ((int(posix)+1) > int(tamfila)) and ((int(posiy)+2) > int(tamcolumna):
            #-------------------------------orillaesquinay---------------------------------Verde
            elif ((int(posix)-2) == 0) and ((int(posiy)-1) == 0):
                if direccion in 'abajo':
                    v1 = sumaGas(usar.recorrerDerecha(posix,posiy))
                    v2 = sumaGas(usar.recorrerabajo(posix,posiy))
                    if v1 > v2:
                        direccion = 'abajo'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posix += 1
                    else:
                        direccion = 'derecha'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posiy += 1
            #elif ((int(posix)-2) == 0) and ((int(posiy)+1) > int(tamcolumna)):
                #print(f'{posix} {posiy}')
                #if direccion in 'derecha':
                    #v1 = sumaGas(usar.recorrerabajo(posix,posiy))
                    #direccion = 'abajo'
                    #actual = str(posix) + ',' + str(posiy)
                    #arreglopos.append(actual)
                    #print(f'posiciones = {arreglopos}')
                    #arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                    #print(f'gasolinas {arreglogas}')
                    #posix += 1
            #elif ((int(posix)+2) > int(tamfila)) and ((int(posiy)-1) == 0:
            #elif ((int(posix)+2) > int(tamfila)) and ((int(posiy)+1) > int(tamcolumna):
            #-------------------------------enmedioarriba---------------------------------Verdelimon
            #elif ((int(posix)-1) == 0) and ((int(posiy)-2) >= 0) and ((int(posiy)+2) <= int(tamcolumna)):
            #-------------------------------enmedioabajo---------------------------------amrillo cafe
            #elif ((int(posix)+1) > int(tamfila)) and ((int(posiy)-2) >= 0) and ((int(posiy)+2) <= int(tamcolumna)):
            #-------------------------------enmedioizquierda---------------------------------morado
            #elif ((int(posiy)-1) == 0) and ((int(posix)-2) >= 0) and ((int(posix)+2) <= int(tamfila)):
            #-------------------------------enmedioderecha---------------------------------moradoderecha
            #elif ((int(posiy)+1) > int(tamcolumna)) and ((int(posix)-2) >= 0) and ((int(posix)+2) <= int(tamfila)):
                #if direccion in 'abajo':
                    #v1 = sumaGas(usar.recorrerIzquierda(posix,posiy))
                    #v2 = sumaGas(usar.recorrerabajo(posix,posiy))
                    #if v1 > v2:
                        #direccion = 'abajo'
                        #actual = str(posix) + ',' + str(posiy)
                        #arreglopos.append(actual)
                        #print(f'posiciones = {arreglopos}')
                        #arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        #print(f'gasolinas {arreglogas}')
                        #posix += 1
                    #else:
                        #direccion = 'izquierda'
                        #actual = str(posix) + ',' + str(posiy)
                        #arreglopos.append(actual)
                        #print(f'posiciones = {arreglopos}')
                        #arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        #print(f'gasolinas {arreglogas}')
                        #posiy -= 1
                #print('aca')
                #print(direccion)
                #-------------------------------interseccionarribIz---------------------------------gris
            elif ((int(posix)-2) == 0) and ((int(posiy)-2) == 0):
                if direccion in 'derecha':
                    v1 = sumaGas(usar.recorrerDerecha(posix,posiy))
                    v2 = sumaGas(usar.recorrerabajo(posix,posiy))
                    if v1 > v2:
                        direccion = 'abajo'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posix += 1
                    else:
                        direccion = 'derecha'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posiy += 1
            #-------------------------------interseccionarribDere---------------------------------gris
            elif ((int(posix)-2) == 0) and ((int(posiy)+2) > int(tamcolumna)):
                if direccion in 'derecha':
                    v1 = sumaGas(usar.recorrerDerechaAbajo(posix,posiy))
                    v2 = sumaGas(usar.recorrerabajo(posix,posiy))
                    v3 = sumaGas(usar.recorrerDerechaArriba(posix,posiy))
                    if (v1 > v2) and (v3 > v2):
                        direccion = 'abajo'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posix += 1
                    elif (v2 > v1) and (v3 > v1):
                        direccion = 'derecha'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posiy += 1
                        exit()
                    elif (v1 > v3) and (v2 > v3):
                        direccion = 'derecha'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posiy += 1
            #-------------------------------interseccionabajoIz---------------------------------gris
            #elif ((int(posix)+2) > int(tamfila)) and ((int(posiy)-2) == 0):
            #-------------------------------interseccionabajoDere---------------------------------gris
            #elif ((int(posix)+2) > int(tamfila)) and ((int(posiy)+2) > int(tamcolumna)):
            #-------------------------------enmedioarribax+1---------------------------------grisoscuro
            elif ((int(posix)-2) == 0) and ((int(posiy)-2) > 0 ) and ((int(posiy)+2) <= int(tamcolumna)):
                if direccion in 'derecha':
                    v1 = sumaGas(usar.recorrerDerecha(posix,posiy))
                    v2 = sumaGas(usar.recorrerabajo(posix,posiy))
                    if (v1 > v2):
                        direccion = 'abajo'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posix += 1
                    else:
                        direccion = 'derecha'
                        actual = str(posix) + ',' + str(posiy)
                        arreglopos.append(actual)
                        print(f'posiciones = {arreglopos}')
                        arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        print(f'gasolinas {arreglogas}')
                        posiy += 1
            #-------------------------------enmedioabajotamfila-1---------------------------------grisoscuro
            #elif ((int(posix)+2) > int(tamfila)) and ((int(posiy)-2) <=0 ) and ((int(posiy)-2) <= int(tamcolumna)):
            #-------------------------------enmizqierday+1---------------------------------grisoscuro
            #elif ((int(posiy)-2) == 0) and ((int(posix)-2) >=0 ) and ((int(posix)-2) <= int(tamfila)):
            #-------------------------------enmedioderechatamcolumna-1---------------------------------grisoscuro
            #elif ((int(posiy)+2) > int(tamcolumna)) and ((int(posix)-2) >=0 ) and ((int(posix)-2) <= int(tamfila)):
            #-------------------------------centro---------------------------------azulmarino
            #elif ((int(posiy)-2) >= 0) and ((int(posix)-2) >=0 ) and ((int(posiy)+2) <= int(tamcolumna)) and ((int(posix)+2) <= int(tamfila)):
                #if direccion in 'derecha':
                    #v1 = sumaGas(usar.recorrerDerecha(posix,posiy))
                    #v2 = sumaGas(usar.recorrerabajo(posix,posiy))
                    #if v1 > v2:
                        #direccion = 'abajo'
                        #actual = str(posix) + ',' + str(posiy)
                        #arreglopos.append(actual)
                        #print(f'posiciones = {arreglopos}')
                        #arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        #print(f'gasolinas {arreglogas}')
                        #posix += 1
                    #else:
                        #direccion = 'derecha'
                        #actual = str(posix) + ',' + str(posiy)
                        #arreglopos.append(actual)
                        #print(f'posiciones = {arreglopos}')
                        #arreglogas.append(usar.getCombustible(actual[0],actual[2]))
                        #print(f'gasolinas {arreglogas}')
                        #posiy += 1

            
    elif lectura == int(3):
        c=1
    elif lectura == int(4):
        print('Nery José Barrientos Posadas\n201807086\nIntroducción a la computacion 2 sección "A"\nIngenieria en ciencias y sistemas\n4to semestre')
        menu()
    elif lectura == int(5):
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
    elif lectura == int(6):
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

def recorrido(fila,columna):
    combustible = usar.recorrerDerecha(fila,columna)
    prueba = sumaGas(combustible)
    print(prueba)


menu()