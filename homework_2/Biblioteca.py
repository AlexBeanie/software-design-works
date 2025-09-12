from libro import Libro
from libro import Genero

class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def leerDatosDeLibro(self):
        datos = {}
        datos["titulo"] = input("Título: ")
        datos["autor"] = input("Autor: ")
        datos["genero"] = Genero(input("Género (novela/ciencia/historia): ").lower()).name
        datos["paginas"] = int(input("Número de páginas: "))
        datos["anio"] = int(input("Año de publicación: "))
        return datos
    
    def insertarLibroEnLibreria(self, args):
        l = Libro(args["titulo"], args["autor"], args["genero"], args["paginas"], args["anio"])
        self.libros.append(l)
        print("Libro agregado!")
    
    def agregar_libro(self):
        datos = self.leerDatosDeLibro()
        self.insertarLibroEnLibreria(datos)      
        
    def imprimirReporte(datos):
        print("\nREPORTE BIBLIOTECA:")
        print(f"Total libros: {datos['total']}")
        print(f"Disponibles: {datos['disponibles']}")
        print(f"Antiguos: {datos['antiguos']}")
        print(f"Promedio de popularidad: {datos['popularidad_total'] / datos['total'] if datos['total'] > 0 else 0}")
        
    def calcularDatosReporte(self):
        datos = {}
        datos["total"] = len(self.libros)
        datos['antiguos'] = 0
        datos['disponibles'] = 0
        datos['popularidad_total'] = 0
        
        for l in self.libros:
            l.imprimir_datos()
            if l.es_antiguo():
                datos['antiguos'] += 1
            if l.disponible:
                datos['disponibles'] += 1
            datos['popularidad_total'] += l.calcular_popularidad()
        
        return datos
            
    def generar_reporte(self):
        datos = self.calcularDatosReporte()
        self.imprimirReporte(datos)