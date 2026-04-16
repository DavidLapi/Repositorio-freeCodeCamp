# Ejercicio 2: Construye un generador de perfiles de empleados

## Paso 1

Las cadenas son secuencias de caracteres usadas para almacenar datos de texto. Como recordarás de lecciones anteriores, puedes crear una cadena encerrando texto dentro de comillas simples (*'*) o dobles (*"*). Por ejemplo:

```py
greeting = 'Hello'
print(greeting) # Output: Hello
```

Crea una variable *first_name* que almacene la cadena *John* y una variable *last_name* que almacene la cadena *Doe*. Luego imprime *first_name* y *last_name*.

## Paso 2 

En Python, puedes combinar cadenas usando el operador *+*. Esto se llama **concatenación**. Aquí tienes un ejemplo:

```py
greeting = 'Hello' + 'World'
print(greeting) # Output: HelloWorld
```

Crea una variable *full_name* concatenando *first_name* y *last_name*. Luego imprime *full_name*.

## Paso 3

Si concatenas dos cadenas como *'John' + 'Doe'*, el resultado es *'JohnDoe'* sin espacio. Para arreglar esto, necesitas concatenar una cadena que contenga un espacio (' ') entre ellas.

Actualiza tu variable full_name para que concatene first_name, un espacio y last_name.

## Paso 4

A continuación, crea una variable *address* para almacenar la dirección del empleado. Asígnale la cadena *123 Main Street* y finalmente imprime *address*.

## Paso 5

Ahora, tu dirección parece incompleta. También quieres agregar el número del apartamento donde vive el empleado, así que debes modificar la variable.

Cuando quieras agregar contenido al final de una variable de cadena existente, puedes usar el operador de **asignación aumentada** ,+=. Esto es más corto que escribir *var = var + 'new text'*. Por ejemplo:

```py
greeting = 'Hello'
greeting += ' World'
print(greeting) # Hello World
```

Recuerda que las cadenas son inmutables, por lo tanto esta operación no cambia la cadena original. En cambio, crea una nueva cadena y la reasigna a la variable.

Usa el operador += para agregar la cadena *, Apartment 4B* a tu variable *address*.

## Paso 6

La salida en el terminal se está llenando. Antes de continuar, es hora de limpiarla.

Elimina todas las sentencias *print()* de tu código.

## Paso 7

Ahora crea una variable llamada *employee_age* y asígnale el entero *28*.

## Paso 8

Ahora, quieres crear una cadena que muestre la edad del empleado.

Comienza creando una variable *employee_info* y asígnale el resultado de concatenar:

- la variable *full_name*.
- una cadena que consiste en los caracteres *is* precedidos y seguidos por un espacio (' is ').

## Paso 9

Actualiza la asignación de *employee_info* para también concatenar *employee_age* al final.

Una vez que lo hayas hecho, verás un *TypeError* en el terminal. En el siguiente paso, trabajarás en corregirlo.

## Paso 10

Como puedes ver, Python generó un *TypeError: can only concatenate str (not "int") to str*. Esto sucede porque Python no permite concatenar texto (cadenas) y números (enteros) directamente.

Para solucionar esto, debes convertir el número a una cadena primero usando la función *str()*, que devuelve la versión en cadena de un objeto:

```py
my_num = str(42)
print(type(my_num)) # <class 'str'>
```

Actualiza tu asignación de *employee_info* para convertir *employee_age* a una cadena usando *str(employee_age)*.

## Paso 11

Ahora completa la oración actualizando la asignación de *employee_info* para también concatenar la cadena * years old* al final. Recuerda incluir un espacio al principio de tu cadena.

Finalmente, imprime *employee_info*.

## Paso 12

Ahora vas a usar la función *str()* una vez más. Al igual que con age, debes convertir cualquier variable numérica a una cadena antes de concatenarla con otro texto.

Crea una variable llamada *experience_years* y asígnale el entero *5*.

Luego, crea una variable *experience_info*. Asígnale una cadena formada por la concatenación de *'Experience: '*, la variable *experience_years* (convertida a cadena) y *' years'*. Imprime el resultado en el terminal.

## Paso 13

Concatenar muchas cadenas usando + y convertir números usando *str()* puede volverse desordenado y difícil de leer.

Python 3.6 introdujo las **f-strings** para resolver esto. Al agregar la letra *f* antes de la comilla de apertura, puedes poner variables y expresiones dentro de campos de reemplazo representados por llaves *{}*. Por ejemplo:

```py
name = 'John'
print(f'Hello {name}') # Output: Hello John
```

Crea una variable *employee_card* y asígnale un *f-string* que muestre *Employee:* seguido de un espacio y el valor de la variable *full_name*.

## Paso 14

Actualmente, *employee_card* solo muestra el nombre del empleado. Ahora vas a agregar más información a esta estructura.

Actualiza la asignación de *employee_card* para incluir la edad del empleado. La cadena final debe verse así: *Employee: [name] | Age: [age]* con *[name]* reemplazado por el nombre del empleado, y *[age]* reemplazado por la edad del empleado.

## Paso 15

Ahora es momento de agregar los detalles finales a la tarjeta.

Crea una variable llamada *position* con el valor de la cadena *Data Analyst* y una variable llamada *salary* con el valor del entero *75000*.

Luego, actualiza tu f-string *employee_card* para incluir el puesto y el salario. Debe seguir este formato exacto: *Employee: [full_name] | Age: [employee_age] | Position: [position] | Salary: $[salary]*. Reemplaza los marcadores con las variables correspondientes.

Finalmente, imprime *employee_card* para ver el resultado.

## Paso 16

Cuando trabajas con cadenas, a menudo necesitarás extraer una porción específica de una cadena. Esto se llama **slicing**.

La sintaxis es *string[start:stop]*, donde:

- *start* es el índice donde comienza el slice (inclusive).
- *stop* es el índice donde termina la porción (exclusivo).

Por ejemplo, si *text = 'Python'*, entonces *text[0:2]* da *'Py'*.

Define *employee_code* como *'DEV-2026-JD-001'*. Después, crea una variable *department* y asígnale el segmento de *employee_code* desde el índice *0* hasta el *3*. Luego imprime *department* en la terminal.

## Paso 17

Puedes cortar desde cualquier parte de la cadena, no solo desde el principio. Y es útil en muchos casos.

Crea una variable *year_code* y asígnale el segmento de *employee_code* desde el índice *4* hasta el *8*. Esto extraerá *2026*.

Luego crea una variable *initials* y asígnale el segmento de *employee_code* desde el índice *9* hasta el *11*. Esto extraerá *JD*.

Finalmente, imprime ambas variables en el terminal.

## Paso 18

También puedes usar números negativos para cortar desde el final de una cadena. Por ejemplo, *-1* se refiere al último carácter, *-2* se refiere al penúltimo carácter, y así sucesivamente.

Para obtener los últimos tres caracteres de una cadena, puedes usar *string[-3:]*. Observa cómo el parámetro stop se omite después de los dos puntos. Esto significa que el corte debe continuar hasta el límite de la cadena.

Crea una variable llamada *last_three*. Usa indexación negativa para extraer los últimos tres caracteres de *employee_code* (que representan el número de identificación). Finalmente, imprime *last_three* en la terminal.

Con eso, el taller de tarjetas de empleado está completo.