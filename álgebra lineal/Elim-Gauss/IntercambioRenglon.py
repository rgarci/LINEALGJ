"""Esta funcion recibe una matriz y los renglones a intercambiar"""


def IntercambiarRenglon(tam, matriz, r1, r2):
    aux=[0]*tam
    for i in range(tam):
        aux[i]=matriz[r1][i]
    for j in range(tam):
        matriz[r1][j]=matriz[r2][j]
        matriz[r2][j]=aux[j]
