"Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje."
class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje =kilometraje
    
Vehiculo1=Vehiculo(80, 35000)
print ("La velocidad maxima del vehiculo 1 es: ", Vehiculo1.velocidad_maxima)
print ("El kilometraje del vehiculo 1 es: ", Vehiculo1.kilometraje)