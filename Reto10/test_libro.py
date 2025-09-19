from libro import Libro

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

# Mostrar la información de cada libro
libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()

# Verificar si alguno de los libros es "grande"
print(f"¿El libro '{libro1.titulo}' es grande? {Libro.es_grande(libro1.paginas)}")
print(f"¿El libro '{libro2.titulo}' es grande? {Libro.es_grande(libro2.paginas)}")
print(f"¿El libro '{libro3.titulo}' es grande? {Libro.es_grande(libro3.paginas)}")

# Mostrar el total de libros creados
print(f"Total de libros creados: {Libro.total_libros()}")