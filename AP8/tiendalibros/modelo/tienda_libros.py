from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro import Libro

class TiendaLibros: 
    def __init__(self):
        self.catalogo={}
        self.carrito = CarroCompras()  

    def adicionar_libro_a_catalogo (self, isbn:str, titulo:str, precio:float, existencias:int)->Libro:
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn)
        nuevo_libro =Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro
    
    def agregar_libro_a_carrito_de_compras (self, isbn, cantidad):
        libro =self.catalogo.get(isbn)

        if libro.existencias==0:
            raise LibroAgotadoError(libro)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro, cantidad)

        self.carrito.agregar_item(libro, cantidad)

    def  retirar_libro_de_carrito_de_compras(self, isbn):
        self.carrito.quitar_item(isbn) 
             
             


    
    

