from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def leerDatosDeLibro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género (novela/ciencia/historia): ").lower()
        paginas = int(input("Número de páginas: "))
        anio = int(input("Año de publicación: "))
        return [titulo, autor, genero, paginas, anio]
    
    def insertarLibroEnLibreria(self, args):
        l = Libro(args[0], args[1], args[2], args[3], args[4])
        self.libros.append(l)
        print("Libro agregado!")
    
    def agregar_libro(self):
        datos = self.leerDatosDeLibro()
        self.insertarLibroEnLibreria(datos)      
            
    def generar_reporte(self):
        total = len(self.libros)
        antiguos = 0
        disponibles = 0
        popularidad_total = 0
        
        for l in self.libros:
            l.imprimir_datos()
            if l.es_antiguo():
                antiguos += 1
            if l.disponible:
                disponibles += 1
            popularidad_total += l.calcular_popularidad()
        
        print("\nREPORTE BIBLIOTECA:")
        print(f"Total libros: {total}")
        print(f"Disponibles: {disponibles}")
        print(f"Antiguos: {antiguos}")
        print(f"Promedio de popularidad: {popularidad_total / total if total > 0 else 0}")