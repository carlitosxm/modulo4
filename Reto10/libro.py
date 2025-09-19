class Libro:

    contador=0

    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        Libro.contador+=1

    def mostrar_info(self):
        print(f"Titulo: {self.titulo} Autor: {self.autor} Número de paginas: {self.paginas}")

    @staticmethod
    def es_grande(cantidad_paginas):
        if cantidad_paginas > 300:
            return True
        else:
            return False

    @classmethod
    def total_libros(cls):
        return cls.contador        
        