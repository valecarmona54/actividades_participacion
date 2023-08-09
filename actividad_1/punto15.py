cadena_texto=input("Ingrese el texto: ")
texto = cadena_texto.lower().replace("","")
palindromo = cadena_texto==texto[::-1]
if palindromo:
    print("La cadena de texto es un palindromo")
else:
    print("La cadena de texto no es un palindromo")