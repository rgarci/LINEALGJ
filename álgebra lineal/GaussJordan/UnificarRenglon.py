"""Esta función vuelve 1 el pibote de un renglón"""


def UnificarRenglon(tam, matriz, r):
    aux=1
    for j in range(tam):
        if (matriz[r][j]!=0):
            aux = matriz[r][j]
            break
    for i in range(tam):
        matriz[r][i] = (matriz[r][i]/aux)
