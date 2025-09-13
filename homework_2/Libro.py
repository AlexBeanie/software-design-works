from enum import Enum

class Genero(Enum):
    NOVELA = 'novela'
    CIENCIA = 'ciencia'
    HISTORIA = 'historia'

POPULARIDAD_BASE = {
    Genero.NOVELA: 50,
    Genero.CIENCIA: 70,
    Genero.HISTORIA: 40
}

POPULARIDAD_FACTOR = {
    Genero.NOVELA: 10,
    Genero.CIENCIA: 5,
    Genero.HISTORIA: 8
}

class Libro:
    def __init__(self, titulo, autor, genero, paginas, anio_publicacion, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero  # 'novela', 'ciencia', 'historia'
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible
    
    def calcular_popularidad(self):
        base = 10
        extra = 0
        
        if self.genero != '':
            base = POPULARIDAD_BASE[self.genero]
            factor = POPULARIDAD_FACTOR[self.genero]
            extra = (self.paginas / factor) if factor else 0
            
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