import random
lista=int(input("Hola usuario, por favor ingrese la cantidad de números que debe de tener la lista: "))
numeros_aleatorios =[random.randint(1, 999) for i in range(lista)]
print ("lista:")
for numero in numeros_aleatorios:
    print(numero)