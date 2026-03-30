# Ejercicio: Construye una impresora de boletas de calificaciones

## Paso 1

En este taller, practicarás los tipos de datos de Python construyendo una impresora de boletas simple.

Como aprendiste en lecciones anteriores, las variables se asignan de esta manera:

```py
greeting = 'Hello World'
```

En el ejemplo anterior, la variable *greeting* tiene el valor de una cadena, que es una secuencia de caracteres rodeada por comillas.

Crea una variable llamada *name* y asígnale la cadena *Alice*. Recuerda rodear el valor con comillas simples o dobles como se muestra en el ejemplo.

**Importante**: Python usa la indentación (los espacios al inicio de una línea) para organizar el código. Para este taller, asegúrate de que no haya espacios adicionales al comienzo de cada línea de código. Agregar espacios extra causará un *IndentationError* y evitará que tu código se ejecute.

## Paso 2

Puedes imprimir el valor de una variable usando la función *print()*. 

**Código de ejemplo:**

```py
greeting = 'Hello World'
print(greeting) # Output: Hello World
```

Aprenderás más sobre funciones en las próximas lecciones. Por ahora, sabe que una función es un bloque reutilizable de código que puede ser llamado, o invocado, para ejecutar su código, y se le pueden pasar argumentos.

En el ejemplo anterior, *print(greeting)* es una llamada a función, y *greeting* es el argumento de la función.

Consulta el ejemplo e imprime la variable *name*. Revisa la salida en el terminal.

## Paso 3

Ahora deberías ver el nombre del estudiante impreso en el terminal.

Python proporciona una función llamada *type()* que puedes usar para verificar el tipo de un valor.

**Código de ejemplo:**

```py
platform = 'freeCodeCamp'
print(type(platform)) # Output: <class 'str'>
```

En el ejemplo anterior, la salida *&lt;class 'str'&gt;* significa que la variable pasada a la función *type()* es una cadena.

Usa la función *type()* con *name* como argumento e imprime la salida como en el ejemplo. Revisa la salida en el terminal que muestra que *name* es del tipo *str* (cadena).

## Paso 4

La boleta de calificaciones también debe mostrar si el estudiante está actualmente inscrito. Esto puede representarse usando un valor booleano.

Los valores booleanos representan una condición de sí o no, y a menudo se usan para tomar decisiones en el código. Solo existen dos valores booleanos: *True* y *False*.

Declara una variable llamada *is_student* y asígnale el valor *True*.

## Paso 5

La función *print()* puede mostrar más de un valor a la vez. Separa los valores con una coma (*,*) para imprimirlos en la misma línea.

**Código de ejemplo:**

```py
subject = 'Python'
print(subject, type(subject)) # Output: Python <class 'str'>
```

Imprime tanto *is_student* como *type(is_student)* en la misma línea usando una coma *,* como se muestra en el ejemplo. Luego, verifica la salida en la terminal que muestra el valor de *is_student* y su tipo como *bool* (booleano).

## Paso 6

El nombre del estudiante debe seguir el mismo formato que los otros detalles.

Elimina las salidas anteriores de la variable *name*. Luego, imprime *name* y *type(name)* juntos en una línea separados por una coma como en el paso anterior.

## Paso 7

Ahora necesitas agregar la edad del estudiante a la boleta de calificaciones. Para eso usarás un entero, uno de los tipos de datos numéricos en Python.

Declara una variable llamada *age* y asígnale el valor entero *20*.

Luego, imprime el valor y el tipo de dato de *age* juntos separados por una coma. Revisa la salida en el terminal que muestra el valor de *age* y su tipo como *int* (entero).

## Paso 8

Ahora, añade la puntuación del estudiante.

Declara una variable llamada *score* y asígnale el valor *80.5*.

Aunque tanto *age* como *score* son números, pueden no ser del mismo tipo. Python proporciona una función llamada *isinstance()* para verificar esto.

**Código de ejemplo:**

```py
x = 10
print(isinstance(x, int)) # Output: True
```

Usa *isinstance()* para verificar si *score* es un *int*, y muestra el resultado en el terminal como se muestra en el ejemplo anterior.

## Paso 9

La salida es *False*, lo que muestra que *score* no es un *int*.

Otro tipo común de número en Python es *float*, que representa un número con decimales. Reemplaza *int* con *float* en la llamada existente a *isinstance()* para confirmar esto.

## Paso 10

La salida es *True*, confirmando que *score* es un *float*.

Completa la boleta imprimiendo el valor de *score* junto con su tipo de dato usando una sola instrucción *print()*.