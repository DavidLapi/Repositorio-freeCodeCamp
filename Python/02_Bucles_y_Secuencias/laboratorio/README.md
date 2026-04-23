# Laboratorio de Bucles y Secuencias

## Enunciado: Construir un Generador de Patrones Numéricos

En este laboratorio practicarás los conceptos básicos de Python construyendo una pequeña aplicación que crea un patrón numérico.

**Objetivo:** Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

**Historias de usuario:**

1. Debes definir una función llamada *number_pattern* que tome un solo parámetro *n* (representando un entero positivo).

2. *number_pattern* debe usar un bucle *for*.

3. *number_pattern(n)* debe devolver una cadena con todos los enteros empezando desde *1* hasta *n* (incluido) separados por un espacio. Por ejemplo, **number_pattern(4)** debe devolver la cadena **'1 2 3 4'**.

4. Si el argumento pasado a la función no es un valor entero, la función debe devolver **'Argument must be an integer value'**.

5. Si el argumento pasado a la función es menor que 1, la función debe devolver **'Argument must be an integer greater than 0'**.