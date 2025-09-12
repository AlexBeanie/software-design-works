# Reporte de análisis del código

## Problemas encontrados

1. **Método agregar libro:** Este método tiene una sección de ingreso de datos, la cual debería de estar en otro método, pues el método agregar libros debería limitarse a añadir el libro nuevo a la lista.

2. **Método generar reporte:** Este método es bastante largo y podría ser más adecuado dividirlo en más métodos.

3. **Constructuor de libro:** El constructor tiene muchos parámetros de entrada

4. **Método Calcular popularidad:** Se calcula la popularidad para cada género de libro, lo que incrementa la longitud del método.

5. **Método es antiguo:** Este método puede simplificarse.

6. **Tipado de género:** El género se está manejando como un string, lo que podría dar problemas por errores de redacción.

7. **Falta de validaciones:** No se valida que los datos ingresados sean correctos.

## Soluciones y buenas prácticas

1. **Método agregar libro:** Este método se podría separar en dos métodos `leerDatosDeLibro` y `insertarLibroEnLibreria` para cumplir con SoC.
