# snake
Recursive code to analyze a simple snake moves

modelo matemático evaluativo determinista. Se pretende encontrar todas las posibilidades. Hay que diseñar un arbol de decisión y todos los datos del problema son conocidos.

Las restricciónes de integridad y frontera están claramente definidas y no suponen ningún problema de resolución

El principal reto consiste en determinar el procedimiento de resolución del problema.

Aunque el asunto de los recursos necesarios de cálculo son un tema importante, la falta de tiempo para dar una solución al problema no se va a tener en cuenta para buscar el algoritmo de resolución

En un primer análisis, se puede observar que cada posible movimiento de la cabeza va a tener cuatro movimientos posibles, por lo que se puede estimar que el orden de complejidad del problema será de típo polinómico. No se trata de un problema de una complejidad grande que requiera una cantidad grande de memoria. La cantidad máxima teórica de movimientos disponibles a estudiar será 3 elevado a (depth)

Debido a que para poder analizar la viabilidad de cada solución es necesario analizar todas las combinaciones, se llega a la conclusión de que un método apropiado para proceder es el llamado Backtracking o Vuelta Atrás, de manera que se genera primero un arbol con todas las posibles soluciones y luego se va analizando cada rama con un algoritmo de Ramificación y Poda hasta haber explorado todas las posibilidades.

Para evitar la exploración completa de todas las opciones, debe diseñarse un algoritmo basado en las restricciones del problema que sea sencilla para que no haya que acudir a la fuerza bruta para conseguir el resultado final.

Como algoritmo de inicio para resolver el problema, se va a hacer uso del famoso problema de las 4 reinas en 4x4 y a partir de ahí se adaptará al problema concreto de la serpiente.

