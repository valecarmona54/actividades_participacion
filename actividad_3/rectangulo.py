"""Cree una clase Rectángulo la cual contiene dos atributos 
de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la
clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado."""

class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcular_el_perimetro(self):
        base = self.x2- self.x1
        altura = self.y2 - self.y1
        return 2*(base + altura)
    
    def calcular_area(self):
        base = self.x2- self.x1
        altura = self.y2 - self.y1
        return base * altura
    
    def rectangulo_cuadrado(self):
        base=self.x2 - self.x1
        altura =self.y2 - self.y1
        return base==altura
    
rectangulo1=Rectangulo(3,7,6,9)
print("El perimetro del rectangulo es: ", rectangulo1.calcular_el_perimetro())
print("El area del rectangulo es: ", rectangulo1.calcular_area())
if rectangulo1.rectangulo_cuadrado():
    print("El rectangulo es cuadrado")
else:
    print("El restangulo no es cuadrado")



    
