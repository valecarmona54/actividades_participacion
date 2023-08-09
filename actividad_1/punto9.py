import random 
filas = int(input("Hola usuario, ingrese el numero de filas de la matriz: "))
columnas = int(input("Hola usuario, ingrese el numero de colomnas de la matriz: "))
matriz_aleatoria=[[random.randint(1, 1000)for i in range(columnas)] for j in range(filas)]
for fila in matriz_aleatoria:
    print (fila)