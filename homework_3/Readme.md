# Tarea 3

## Enunciado

Debe crear un sistema que simule un restaurante donde:

- Clientes realizan pedidos de diferentes tipos de pedidos (hamburguesas y pizzas)
- Cocineros (hilos independientes) procesan los pedidos concurrentemente

## Documentación

### Cambios al código base

- Se cambian los nombres de los métodos por consistencia con la implementación
- Se añade la creación del `PizzaFactory` al código Main para poder ser utilizado en el mismo
- Se modifica ligeramente la implementación del método `processOrders` de modo que se puede indicar la cantidad de hilos deseado

### Código implementado

#### Services.py

En este archivo se encuentra la clase `Services` la cual contiene como atributo una cola de tipo `Queue`, puesto que este tipo de cola es thread safe. Asimismo, se cuenta con una función para añadir elementos a dicha cola.

Por otro lado, se implementa la función `processOrders`, la cual se encarga de crear tantos hilos como sean indicados, que ejecutarán la función interna `serveOrder`, la cual se encarga de "cocinar" los pedidos que los clientes dejan en la cola.

#### Factories.py

En este archivo se encuentran las clases Factory necesarias para la ejecución del código.

`BaseFactory` es la clase base de la cual `HamburgerFactory` y `PizzaFactory` heredan para su ejecución. Esta clase utiliza la librería `ABC` (Abstract Class) para asegurar que los métodos hijos sobreescriben la función `makeOrder` de acuerdo a sus necesidades.

La función `makeOrder` retorna una lista con el nombre del producto a servir ("Hamburger" o "Pizza") y el número de la orden.
