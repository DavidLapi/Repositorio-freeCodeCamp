# Laboratorio 3: Construir un personaje de RPG

En este laboratorio, practicarás los fundamentos de Python construyendo una pequeña aplicación que crea un personaje para una aventura RPG.

**Objetivo:** Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

## Historias de usuario:

1. Debes tener una función llamada *create_character*.

2. La función debe aceptar, en orden, un nombre de personaje seguido por tres estadísticas: fuerza, inteligencia y carisma.

3. Se debe validar el nombre del personaje:

- Si el nombre del personaje no es una cadena, la función debe devolver *'The character name should be a string.'*

- Si el nombre del personaje es una cadena vacía, la función debe devolver *'The character should have a name.'*

- Si el nombre del personaje tiene más de 10 caracteres, la función debe devolver *'The character name is too long.'*

- Si el nombre del personaje contiene espacios, la función debe devolver *'The character name should not contain spaces.'*

4. Las estadísticas también deben ser validadas:

- Si una o más estadísticas no son enteros, la función debe devolver *'All stats should be integers.'*

- Si una o más estadísticas son menores que 1, la función debe devolver *'All stats should be no less than 1.'*

- Si una o más estadísticas son mayores que 4, la función debe devolver *'All stats should be no more than 4.'*

- Si la suma de todas las estadísticas es diferente de 7, la función debe devolver *'The character should start with 7 points.'*

5. Si todos los valores pasan la verificación, la función debe devolver una cadena con cuatro líneas:

- la primera línea debe contener el nombre del personaje

- las líneas 2-4 deben comenzar con la abreviatura de la estadística, *STR*, *INT* o *CHA* (en ese orden), luego un espacio, y luego un número de puntos llenos (●) igual al valor de la estadística, y un número de puntos vacíos (○) para llegar a 10. **Ejemplo:** si el valor de fuerza es 3 debe haber 3 puntos llenos seguidos de 7 puntos vacíos. Los puntos se dan en el editor.

Aquí está la cadena que debe ser devuelta por *'create_character('ren', 4, 2, 1)'*:

ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○

**NOTA:** aunque str e int son abreviaturas comunes para las estadísticas, recuerda que son palabras clave reservadas en Python y no deben usarse como nombres de variables.