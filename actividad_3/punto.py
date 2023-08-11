"Cree una clase Punto que represente un punto en el plano cartesiano."
"""A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto
- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto."""
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def mostrar(self):
        print("La coordenada del punto es:", self.x, self.y)

    def mover(self, mover_x, mover_y):
        self.x = mover_x
        self.y = mover_y
    
    def calcular_distancia(self, otro_punto):
        distancia_x=self.x - otro_punto.x
        distancia_y=self.y - otro_punto.y
        distancia =math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia
    

punto1=Punto(30, 7)
punto2=Punto(4,-9)
print("Las coordenadas del punto 1 son:" )
punto1.mostrar()


punto1.mover(7,30)
punto1.mostrar()

distancia= punto1.calcular_distancia(punto2)
print ("La distancia es:", distancia)





