"""esta función multiplica un renglon R1 por una constante y lo suma a otro renglon R2"""



def MulSumRenglon(tam, matriz, r1, r2):

    pivote2 = 0
    aux=[0]*tam


    for i in range(tam):
        if(matriz[r1][i]!=0):
            pivote2 = -matriz[r2][i]/matriz[r1][i]
            break

    for e in range(tam):
        aux[e]=(pivote2*(matriz[r1][e]))

    for j in range(tam):
        matriz[r2][j] = (matriz[r2][j] + aux[j])
