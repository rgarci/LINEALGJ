"""Programa 1 que convierte la matriz dada en un archivo txt a una matriz escalonada"""


"""función que recibe el archivo txt y lo procesa"""
def gauss(input1):
    """Se importan las funciones que nos ayudarán a escalonar la matriz"""
    from MulSumRenglon import MulSumRenglon
    from UnificarRenglon import UnificarRenglon
    from IntercambioRenglon import IntercambiarRenglon


    """abrimos el archivo y guardamos los valores en un arreglo"""
    import numpy
    matriz = []
    matriz= numpy.loadtxt(input1, dtype=float, skiprows=1)

    indicadores=[]
    contenido = open(input1, "r")
    indicadores=contenido.readline().split()
    indicadores = list(map(int, indicadores))
    ecu = indicadores[0]
    tam = indicadores[1]+1

    i=0

    while(i<ecu):
        j=i+1
        while(j<ecu):
            MulSumRenglon(tam, matriz, i, j, 1)
            j=j+1
        i=i+1


    print(matriz)

input1 = "input1.txt"
gauss(input1)
