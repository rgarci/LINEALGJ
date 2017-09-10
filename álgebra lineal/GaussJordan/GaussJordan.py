"""Programa 2 que convierte la matriz dada en un archivo txt a una matriz escalonada reducida"""


# función que recibe el archivo txt y lo procesa
def gaussjordan(input1):
    # Se importan las funciones que nos ayudarán a escalonar la matriz
    from MulSumRenglon import MulSumRenglon
    from IntercambioRenglon import IntercambiarRenglon
    from UnificarRenglon import UnificarRenglon
    import numpy


    # guardamos todos los valores del archivo en un arreglo
    archivo = open (input1,'r')
    datos = []

    for linea in archivo.readlines():
        partes_linea = linea.split()
        datos.append([int(i)for i in partes_linea])

    cont=1 #usamos un contador que nos ayudará a movernos a través de la matriz datos
    N=datos[0][0]

    ecu=datos[cont][0] #guardamos el numero de ecuaciones de la matriz
    tam=datos[cont][1]+1 #guardamos el numero de variables de la matriz y agregamos 1 para tomar en cuenta el vector resultado
    cont=cont+1 #aumentamos el contador
    matriz=[]

    for h in range(cont, cont+ecu):
        matriz.append(datos[h])
        print(h)

    print(matriz)


input1="input1.txt"
gaussjordan(input1)
