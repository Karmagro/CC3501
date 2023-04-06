# CC3501: Tarea 1

## Lo que hace mi codigo

Crea una mariposa principal la cual el usuario puede mover (trasladar) usando las teclas direccionales de arriba a abajo y izquierda a derecha,  y un enjambre de mariposas de menor tamaño
las cuales tienen un movimiento propio dependiente del tiempo (rotacion, traslacion y cambio de escala de las alas para la sensacion de aleteo, esta ultima tambien es parte de la mariposa grande), para la rotacion y aleteo uso una funcion sin, mientras que para la traslacion uso una matriz de ruido (Busque formas de provocar aleatoridad en internet) la cual luego de varios juegos con los valores de esta dio como resultado un movimiento natural y diferente para cada una de las mariposas del enjambre.

Siguiendo con las mariposas, estas estan compuestas de varios triangulos y cuadrangulos, me guie de las basic_shapes para crear funciones que recibieran las 3 posiciones (x,y,z) ademas de los colores para cada vertice, esto lo aproveche para darles colores distintos a los vertices dandole un gradiente a la mariposa. Las partes las puse en una lista llamada mariposa en la cual luego itero para darle el movimiento descrito anteriormente.

En general mi tarea hace todo lo que se pide que haga ademas de lo extra (el enjambre, movimientos, ilusion de aleteo, cambio de color de pantalla..), considerando lo que no hace mi mariposa podria tenerse en cuenta que no agregue transformaciones del tipo shearing, o que no hice nada demasiado alejado de lo que se pidio.

## Consideraciones para correr el codigo

Mi codigo utiliza todas las librerias y modulos del curso, pero adicionalmente hago uso de "noise", en el caso de mi ordenador fue algo complicado instalarlo (lo tuve que descargar como archivo .whl desde <https://www.lfd.uci.edu/~gohlke/pythonlibs/#noise> , la version noise-1.2.3-cp311-cp311-win_amd64)
