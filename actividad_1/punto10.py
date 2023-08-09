numero= int(input("Hola usuario, ingrese en número para sacar su factorial: "))
def factoriales_numero(numero):
    contador=1
    for i in range (1, numero + 1):
        contador*=i
    return contador
factoriales=factoriales_numero(numero)
print ("Los factoriales del", numero, "es: ", factoriales)
