"""Cree una clase Circulo que tenga las propiedades centro y radio,las cuales se inicializan 
  con parámetros en el constructor. Defina métodos en la clase para calcular el área,
 el perímetro e indicar si un punto pertenece al círculo o no."""
import math
class Circulo:
    def __init__(self, radio, centro):
        self.radio = radio
        self.centro = centro


    def area_circulo(self):
        area=2 * math.pi * self.radio
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto[0] - self.centro[0])**2 + (punto[1] - self.centro[1])**2)
        return distancia_centro_punto <= self.radio
       
radio = 10
centro = (0,0)
circulo1=Circulo(radio, centro)

print("El area del circulo es:", circulo1.area_circulo())

print("El perimetro del circulo es:", circulo1.calcular_perimetro())

punto1= (2,8)
punto2= (7,9)

if circulo1.punto_pertenece(punto1):
    print("El punto ", punto1, " pertenece al círculo.")
else:
    print("El punto ", punto1, " no pertenece al círculo.")
 


