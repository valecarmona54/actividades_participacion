lista=[6, 2, 74, 198, 1, 64, 220,48]
numero_mayor = lista[0]
numero_menor = lista[0]
for i in range(1, len(lista)):
    if lista[i] > numero_mayor:
        numero_mayor = lista[i]
    if lista[i] < numero_menor:
        numero_menor = lista[i]
print ("El número mayor es: ", numero_mayor)
print ("El número menor: ", numero_menor)