"""Programa 1 que convierte la matriz dada en un archivo txt a una matriz escalonada"""


"""función que recibe el archivo txt y lo procesa"""
def gauss(input1):
    """Se importan las funciones que nos ayudarán a escalonar la matriz"""
    from MulSumRenglon import MulSumRenglon
    from UnificarRenglon import UnificarRenglon


    """abrimos el archivo y guardamos los valores en un arreglo"""
    import numpy
    matriz = []
    matriz= numpy.loadtxt(input1, dtype=int, skiprows=1)
    print(matriz[0][1])

"""
    for i in range(1+matriz[0][1]):
        if(matri[i][i]==0):
            for e in range(matriz[0][0]):
                if (matriz[e][i] !=0):
                    IntercambiarRenglon(matriz, i, e)
        else:
            for j in range(i+1, matriz[0][0]):
                MulSumRenglon(1+matriz[0][1], matriz, i, j, 1)
                """


input1 = "input1.txt"
gauss(input1)
