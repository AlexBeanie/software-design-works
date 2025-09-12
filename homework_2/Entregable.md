# Reporte de análisis del código

## Problemas encontrados

1. **Método agregar libro:** Este método tiene una sección de ingreso de datos, la cual debería de estar en otro método, pues el método agregar libros debería limitarse a añadir el libro nuevo a la lista.

2. **Método generar reporte:** Este método es bastante largo y podría ser más adecuado dividirlo en más métodos.

3. **Método Calcular popularidad:** Se calcula la popularidad para cada género de libro, lo que incrementa la longitud del método.

4. **Método es antiguo:** Este método puede simplificarse.

5. **Tipado de género:** El género se está manejando como un string, lo que podría dar problemas por errores de redacción.

6. **Falta de validaciones:** No se valida que los datos ingresados sean correctos.

## Soluciones y buenas prácticas

1. **Método agregar libro:** Este método se podría separar en dos métodos `leerDatosDeLibro` y `insertarLibroEnLibreria` para cumplir con SoC.

2. **Método generar reporte:** Separar método en `imprimirReporte` y `calcularDatosReporte`

3. **Método Calcular popularidad:** Se pueden implementar diccionarios para que se guarden los valores de popularidad base y extra, de modo que es más fácil de modificar o añadir géneros a la clase libro. De este modo se simplifica el método y se cumple con el principio Open/Close.

4. **Método es antiguo:** Se simplifica el método a una sola línea.

5. **Tipado de género:** Se cambia el tipo de variable de género a Enum.

6. **Falta de validaciones:** No se valida que los datos ingresados sean correctos.
