from Memoria import*
from Ajustes import*
import os


def separar(a_separar, separador):
    arreglo = list()
    registro = ""
    for letra in a_separar:
        if letra == separador or letra == '\n':
            arreglo.append(registro)
            registro = ""
            continue
        registro += letra
    if letra != "\n":
        arreglo.append(registro)
    return arreglo
def quitarLetras(texto):
    sinLetras = ""
    for letra in texto:
        if letra.isdigit():
            sinLetras+=letra
    return sinLetras
def mostrarArchivos(a):
    print("------------------------------")
    print("Archivos")
    for nom, peso in a:
        print(nom+"   "+str(peso)+" kb")

CLEAR = "cls"
archivo = open("archivos.txt", "r")
lineas = archivo.readlines()
archivos = list()
for linea in lineas:
    arr = separar(linea, ",")
    arr[1] = quitarLetras(arr[1])
    arr[1] = int(arr[1])
    archivos.append(arr)
    
    
while True:
    memoria = Memoria(1000, 400, 1800, 700, 900, 1200, 1500)
    memoria.mostrarMemoria()
    print("1) Primer Ajuste")
    print("2) Mejor Ajuste")
    print("3) Peor Ajuste")
    print("4) Siguiente Ajuste")
    try:
        opc = int(input("Opcion: "))
    except:
        print("Opcion nó válida")
        os.system(CLEAR)
        continue
    if opc == 1:
        primerAjuste(memoria, archivos)
    elif opc==2:
        mejorAjuste(memoria, archivos)
    elif opc==3:
        peorAjuste(memoria, archivos)
    elif opc==4:
        siguienteAjuste(memoria, archivos)
    mostrarArchivos(archivos)
    memoria.mostrarMemoria()
    rep = input("Ingresa 'fin' para terminar: ")
    if rep == "fin":
        break
    os.system(CLEAR)
    
    
    
    
    
    
    
    
    