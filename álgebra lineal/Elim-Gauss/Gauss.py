"""Programa 1 que convierte la matriz dada en un archivo txt a una matriz escalonada"""


"""función que recibe el archivo txt y lo procesa"""
def gauss(input1):

    # Se importan las funciones que nos ayudarán a escalonar la matriz
    from MulSumRenglon import MulSumRenglon
    from IntercambioRenglon import IntercambiarRenglon


    # abrimos el archivo y guardamos los valores de la matriz en un arreglo
    import numpy
    matriz = []
    matriz= numpy.loadtxt(input1, dtype=float, skiprows=1)

    # guardamos los valores de la primera linea en otro arrego
    indicadores=[]
    contenido = open(input1, "r")
    indicadores=contenido.readline().split()
    contenido.close()
    indicadores = list(map(int, indicadores))
    ecu = indicadores[0]
    tam = (indicadores[1])+1

    #inicializamos un contador que itererá en las filas de la matriz
    i=0

    while(i<ecu):
        #comprobamos que el pivote no sea cero, de serlo se le intercambiará con el renglón más próximo donde dicho pivote no sea cero
        if(matriz[i][i]==0):
            for g in range(i,ecu):
                if(matriz[g][i]!=0):
                    IntercambiarRenglon(tam, matriz, i, g)
                    break
        # una vez que el pivote es un entero se eliminan los valores debajo de su columna
        j=i+1
        while(j<ecu):
            MulSumRenglon(tam, matriz, i, j, 1)
            j=j+1
        i=i+1
    # guardamosla matriz en un archivo txt output1 con formato .2f
    numpy.savetxt("output1.txt", matriz, fmt='%.2f')

input1 = "input1(Gauss).txt"
gauss(input1)
