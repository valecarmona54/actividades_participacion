"""Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas 
 solo al momento de la construcción del objeto (se pasan como parámetros en el constructor).
 Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta."""
class Cartas:

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

PINTA_DIAMANTE = "DIAMANTE" 
PINTA_PICA = "PICA"
PINTA_CORAZON = "CORAZON"
PINTA_TREBOL = "TREBOL"

carta1= Cartas(7, PINTA_PICA) 
print("La carta 1 tiene un valor de: ",carta1.valor, "Y tiene una pinta de: ",carta1.pinta)

     