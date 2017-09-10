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
    ListaMatrices=[] # hacemos un arreglo que guardará las matrices escalonadas reducidas
    for s in range(N):

        #######################
        ecu=datos[cont][0] #guardamos el numero de ecuaciones de la matriz
        tam=datos[cont][1]+1 #guardamos el numero de variables de la matriz y agregamos 1 para tomar en cuenta el vector resultado
        cont=cont+1 #aumentamos el contador
        matriz=[]

        for h in range(cont, cont+ecu): #guardamos la matriz con la que vamos a trabajar
            matriz.append(datos[h])


        i=0        #inicializamos un contador que itererá en las filas de la matriz

        cont=cont+ecu
        while(i<ecu):
            #comprobamos que el pivote no sea cero, de serlo se le intercambiará con el renglón más próximo donde dicho pivote no sea cero
            if(matriz[i][i]==0):
                for g in range(i,ecu):
                    if(matriz[g][i]!=0):
                        IntercambiarRenglon(tam, matriz, i, g)
                        break
            # hacemos 1 nuestro pivote
            UnificarRenglon(tam, matriz, i)

            # una vez que el pivote es 1 se eliminan los valores debajo de su columna
            j=i+1

            while(j<ecu):
                MulSumRenglon(tam, matriz, i, j)
                j=j+1

            i=i+1
        #se elimina hacia arriba
        aux=ecu-1
        while(aux>0):
            UnificarRenglon(tam, matriz, aux)
            j=aux-1
            while(j>=0):
                MulSumRenglon(tam, matriz, aux, j)
                j=j-1
            aux=aux-1
        #se guarda la matriz escalonada reducida en una lista de matrices
        ListaMatrices.append(matriz)

        ###################################


    print(ListaMatrices)
    output1=open("output1(GC).txt", "w")
    for elemento in ListaMatrices:
        for renglon in elemento:
            output1.write('%s\n'%renglon)
        output1.write('\n\n\n')
    output1.close()

input1="input1.txt"
gaussjordan(input1)
