from enum import Enum

class Genero(Enum):
    NOVELA = 'novela'
    CIENCIA = 'ciencia'
    HISTORIA = 'historia'


class Libro:
    def __init__(self, titulo, autor, genero, paginas, anio_publicacion, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero  # 'novela', 'ciencia', 'historia'
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible
        self.popularidadBase = {
            Genero.NOVELA: 50,
            Genero.CIENCIA: 70,
            Genero.HISTORIA: 40
        }
        self.popularidadExtra = {
            Genero.NOVELA: self.paginas / 10,
            Genero.CIENCIA: self.paginas / 5,
            Genero.HISTORIA: self.paginas / 8
        }
    
    def calcular_popularidad(self):
        base = 10
        extra = 0
        
        if self.genero != '':
            base = self.popularidadBase[self.genero]
            extra = self.popularidadExtra[self.genero]
            
        return base + extra
    
    def es_antiguo(self):
        return self.anio_publicacion < 1980
    
    def imprimir_datos(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero.value}")
        print(f"Páginas: {self.paginas}")
        print(f"Año: {self.anio_publicacion}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print(f"Popularidad: {self.calcular_popularidad()}")
        print(f"Es antiguo: {'Sí' if self.es_antiguo() else 'No'}")
        print("------------------------")