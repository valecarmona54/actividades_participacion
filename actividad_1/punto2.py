def area_circulo(radio):
    pi_numero=3.1416
    area= pi_numero * radio**2
    return area

radio = float(input("La usuario, ingrese el radio del circulo: "))
area= area_circulo(radio)
print("El area del circulo es: ", area)


