from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.item_compra import ItemCompra 

class CarroCompras:
    def __init__(self):
        self.items:list[ItemCompra]=[]
    
    def agregar_item(Self, libro:Libro, cantidad:int):
        item=ItemCompra(libro, cantidad)
        Self.items.append(item)
        return item 
    
    def calcular_total(self):
        total=0
        for item in self.items:
            total+=item.calcular_subtotal()
        return total

    def quitar_item(self, isbn:str):
        self.items=[item for item in self.items if item.libro.isbn != isbn]


        
    

