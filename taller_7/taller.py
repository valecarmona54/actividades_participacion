from dataclasses import dataclass

@ dataclass
class Elemento:
    nombre:str
    
    def __eq__(self,other):
        return self.nombre == other.nombre
        
class Conjunto:
    contador=0
    def __init__(self, nombre:str):
        # self al objeto
        # Conjunto a la clase
        # Atributo de clase, es el mimso para todos los objetos de la clase 
        #Atributos unicos de cada objeto, variables distintas 
        
        Conjunto.contador+=1
        self.__id = Conjunto.contador
        self.lista_objetos:list = []
        self.nombre = nombre
    @property
    def id(self):
        return self.__id
    
    def contiene(self, elemento:Elemento)->bool:
            for i in self.lista_objetos:
                if elemento == i:
                    return True
            return False 
                 
    def agregar_elemento(self, elemento:Elemento):
        if not self.contiene(elemento):
             self.lista_objetos.append(elemento)

    def unir (self, conjunto):
        for elemento in conjunto.lista_objetos:
            self.agregar_elemento(elemento)

    def __add__(self, conjunto):
        conjuntos=Conjunto(f"{self.nombre} UNION {conjunto.nombre}")
        conjuntos.lista_objetos = self.lista_objetos.copy()
        conjuntos.unir(conjunto)
        return conjuntos
    @classmethod

    def intersectar(cls, conjunto1, conjunto2):
        conjunto3 = Conjunto(f"<{conjunto1.nombre}> INTERSECTADO <{conjunto2.nombre}>")
        for elemento in conjunto1.lista_objetos:
            if conjunto2.contiene(elemento):
                conjunto3.agregar_elemento(elemento)
        return conjunto3
    
    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.lista_objetos])
        conjunto_legible = f"Conjunto <{self.nombre}>: ({elementos_str})"
        return conjunto_legible
    
elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

conjunto1 = Conjunto("Conjunto 1")
conjunto2 = Conjunto("Conjunto 2")

conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)

conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

print(conjunto1)
print(conjunto2)

conjunto_interseccion = Conjunto.intersectar(conjunto1, conjunto2)

print(conjunto_interseccion)



                 
    
             
         


