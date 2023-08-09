def cambio_de_grados(fahrenheit):
    celsius= (fahrenheit-32)* 5/9
    return celsius
temperatura_fahrenheit=int(input("Por favor digite la temperatura en grados fahrenheit: "))
celsius=cambio_de_grados(temperatura_fahrenheit)
print (temperatura_fahrenheit, "equivalen a: ", celsius, "grados celsius")