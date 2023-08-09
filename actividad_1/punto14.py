lista = [5, 4, 8, 9, 4, 2 ]
def aritmetica(lista):
    suma=sum(lista)
    numeros=len(lista)
    media_aritmetica=suma/ numeros
    return numeros

media_aritmetica=aritmetica(lista)
print ("La media aritmetica de la lista es: ", media_aritmetica)