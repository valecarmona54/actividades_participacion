from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self, isbn):
        super().__init__(isbn)
    
    def __repr__(self):
        return (f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} esta agotado")