# Tarea 4 - Cafetería

Link al repositorio: [software-design-works](https://github.com/AlexBeanie/software-design-works.git)

## Funcionamiento

Se utiliza una clase `meal` que contiene un nombre, un tipo y una lista de ingredientes, para representar la comida o alimento. Una clase `Order` implementa el patrón composite para manejar un conjunto de _meals_, aunque no se toma en cuenta como patrón implementado por la falta de funcionalidades. De esta forma, se puede transmitir una orden a cada etapa de una cadena de ensamblaje donde será procesado adecuadamente, hasta que esté listo para que el cliente lo reciba.

## Patrones implementados

### Chain of Responsability

Se decidió utilizar CoR para manejar el flujo de trabajo, puesto que el caso se presta para implementar una cadena de ensamblaje. De esta forma, si es necesario añadir más actividades, como por ejemplo, una preparación extra o un proceso de revisión, se podría hacer este escalado de forma fácil. Para implementarlo se utiliza la clase `IChainHandler`, `BaseChainHandler` y por último las clases concretas en `chainHandlers`.

### Observer

Asimismo se decide implementar el patrón observer en uno de los handlers de `chainHandlers`, específicamente en `PrepHandler`. El objetivo es que cada preparación tenga un handler suscrito al `PrepHandler`, de modo que cuando se encuentre una `meal`, se utilice el handler adecuado dependiendo del tipo de `meal`. De tal modo que se puedan agregar más tipos de comida y su proceso respectivo más fácilmente.

Implementarlo en el `NotifHandler` también sería obvio, pero en este caso se asume que el notificador simplemente notifica en consola (como un recepcionista que grita el número de orden para que el cliente lo venga a recoger), si existieran más medios de notificación, sí tendría más sentido implmentarlos aquí también.
