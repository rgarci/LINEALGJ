"""esta función multiplica un renglon R1 por una constante y lo suma a otro renglon R2"""

matriz= [[1, 1, 0, 3],[2, 1, -1, 1],[3, -1, -1, 2],[-1, 2, 3, -1]]

def MulSumRenglon(tam, matriz, r1, r2, direc):

    pivote2 = 0
    aux=[0]*tam

    if(direc==1):
        for i in range(tam):
            if (matriz[r2][i] != 0):
                pivote2 = -matriz[r2][i]/matriz[r1][i]
                break
        for e in range(tam):
            aux[e]=(pivote2*(matriz[r1][e]))

        for j in range(tam):
            matriz[r2][j] = (matriz[r2][j] + aux[j])
    elif(direc==0):
        for i in range(tam):
            if(matriz[r1][i] != 0):
                pivote1 = -matriz[r2][i]/matriz[r1][i]
                break
        for e in range(tam):
            aux[e] = (pivote1*matriz[r1][e])

        for j in range(tam):
            matriz[r2][j] = (matriz[r2][j]+ aux[j])

            
MulSumRenglon(4, matriz, 0, 1, 1)
MulSumRenglon(4, matriz, 0, 2, 1)
MulSumRenglon(4, matriz, 0, 3, 1)
MulSumRenglon(4, matriz, 1, 2, 1)
MulSumRenglon(4, matriz, 1, 3, 1)
print(matriz)
