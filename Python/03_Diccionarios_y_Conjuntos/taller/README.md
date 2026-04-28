# Taller: Crear un Validador de Datos Médicos

## Paso 1

En este taller, validarás un conjunto de datos médicos para asegurarte de que cumple con un conjunto de reglas.

Declara una variable llamada **medical_records** y asígnale una lista vacía. En los siguientes pasos, la vas a usar para almacenar tus datos médicos.

## Paso 2

Como aprendiste en lecciones anteriores, un diccionario es una estructura de datos que contiene pares clave-valor, donde las claves son tipos de datos inmutables (como cadenas) y únicas dentro de un diccionario:

```py
# Código de ejemplo
person = {
    'name': 'John',
    'age': 33
}
```

La lista **medical_records** almacenará diccionarios, cada uno representando a un paciente. Agrega un diccionario con una clave **patient_id** y un valor de la cadena **'P1001'** a la lista **medical_records**.

## Paso 3

Agrega una clave **age** con el valor del entero **34** y una clave **gender** con el valor de la cadena **'Female'** a tu diccionario. No olvides la coma entre los pares clave-valor.

## Paso 4

Completa el diccionario agregando los siguientes tres pares clave-valor:

- Una clave **diagnosis** con el valor de **'Hypertension'**.
- Una clave **medications** con el valor de la lista **['Lisinopril']**.
- Una clave **last_visit_id** con el valor de **V2301**.

## Paso 5

Siguiendo la misma estructura que usaste en los pasos anteriores, la lista **medical_records** ha sido completada para ti con los datos de otros pacientes. Siéntete libre de echarle un vistazo.

A continuación comenzarás a escribir la función para validar el conjunto de datos. Crea una función llamada **validate** con un solo parámetro **data**.

Quieres asegurarte de que tus datos sean una lista o una tupla. Por lo tanto, dentro de la función **validate**, declara una variable llamada **is_sequence** y asígnale una llamada a **isinstance**. Pasa **data** como el primer argumento y una tupla que contiene **list** y **tuple** como el segundo argumento.

## Paso 6

Crea una estructura **if**. Para su condición, usa el operador **not** para negar **is_sequence**. Dentro de la estructura *if*, imprime *'Invalid format: expected a list or tuple.'* y retorna False.

## Paso 7

Justo después de tu sentencia **if**, declara una variable llamada **is_invalid** y asígnale False. Más adelante, la usarás como una bandera para ejecutar una sentencia condicional.

## Paso 8

Como aprendiste en una lección anterior, la función **enumerate** permite llevar un registro del índice mientras se itera sobre un iterable:

```py
# Código de ejemplo
person = {'name': 'John', 'age': 33}

for index, item in enumerate(person):
    print(index, item)

# 0 name
# 1 age
```

Crea un bucle **for** que itere sobre **data**. Usa la función **enumerate** para obtener tanto el índice como el elemento en **data** en cada iteración. Usa **index** y **dictionary** como variables de iteración.

Por ahora usa **pass** para llenar el cuerpo del ciclo.

```py
# Código de muestra
for index, dictionary in enumerate(data):
        pass
```

## Paso 9

Estás verificando si los datos pasados a tu función son una lista o una tupla. Aún necesitas asegurarte de que cada elemento en la secuencia sea un diccionario.

Dentro de tu bucle **for**, si el elemento en **dictionary** no es una instancia de **dict**, imprime **'Invalid format: expected a dictionary at position &lt;index&gt;.'** (donde &lt;index&gt; debe ser reemplazado por el índice actual) y asigna True a **is_invalid**.

```py
# Código de muestra
if not isinstance(dictionary, dict):
    print(f"Invalid format: expected a dictionary at position {index}.")
    is_invalid = True
```

## Paso 10

Después de tu bucle **for**, aún dentro de la función **validate**, crea una estructura **if**. Si **is_invalid** es **True**, devuelve **False**.

## Paso 11

Después de la sentencia **if**, imprime la cadena **'Valid format.'**. Luego retorna True.

## Paso 12

Al final de tu código, llama a la función **validate** con **medical_records** como argumento. Deberías ver **'Valid format.'** impreso en el terminal.

## Paso 13

Para probar la primera estructura **if** de tu función, convierte **medical_records** en una cadena. Deberías ver **'Invalid format: expected a list or tuple.'** impreso en el terminal.

## Paso 14

Ahora convierte **medical_records** de nuevo en una lista/tupla de diccionarios.

## Paso 15

Para probar la segunda estructura condicional, agrega dos elementos de tu elección que no sean diccionarios al final de la lista **medical_records**. Deberías ver dos mensajes de validación impresos en el terminal.

## Paso 16

Ahora que probaste la validación para esta parte, elimina los últimos dos elementos de la lista **medical_records**.

## Paso 17

Como aprendiste en una lección anterior, un conjunto es una colección desordenada de elementos únicos:

```py
# Código de ejemplo
integers = set([3, 5, 1, 2, 1, 3, 4])
print(integers) # {1, 2, 3, 4, 5}
```

Vas a usar un conjunto para asegurarte de que cada diccionario no contenga claves adicionales o mal escritas.

Dentro de la función **validate**, usa la estructura **set()** para crear un conjunto a partir de la siguiente lista de claves que cada diccionario debe tener: 

```py
['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
```

Asigna el conjunto a una variable llamada **key_set**.

```py
# Codigo de muestra
key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])
```

## Paso 18

El método **keys()** devuelve un objeto vista que contiene todas las claves de un diccionario:

```py
# Código de ejemplo
person = {
   'name': 'John',
   'age': 33
}

print(person.keys()) # dict_keys(['name, 'age'])
```

Dentro de tu bucle **for**, después de la primera sentencia **if**, crea una sentencia **if** que se ejecute cuando el conjunto de claves del diccionario actual sea diferente de **key_set**. Esto es para asegurar que no haya claves faltantes o inválidas en el diccionario.

Dentro de la nueva estructura **if**, imprime **'Invalid format: &lt;dictionary&gt; at position &lt;index&gt; has missing and/or invalid keys.'** (donde &lt;dictionary&gt; y &lt;index&gt; deben ser reemplazados por el diccionario y el índice en la iteración actual) y asigna True a **is_invalid**.

```py
# Código de muestra
if set(dictionary.keys()) != key_set:
    print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
    is_invalid = True
```

## Paso 19

Para probar que todo funciona correctamente, intenta comentar la clave **age** del primer diccionario en **medical_records**.

Deberías ver un mensaje de validación aparecer en el terminal.

## Paso 20

Ahora restaura la línea **'age': 34,**.

## Paso 21

Ahora vas a hacer que la validación sea más granular. Crea una función llamada **find_invalid_records** para encontrar valores inválidos en un diccionario. Dale los siguientes parámetros: **patient_id**, **age**, **gender**, **diagnosis**, **medications**, **last_visit_id**.

Dentro de tu nueva función, crea un diccionario vacío llamado **constraints**. Luego, devuelve **constraints** desde tu nueva función.

## Paso 22

El operador `**` puede usarse para desempaquetar los elementos en un diccionario y pasarlos como argumentos con nombre en una llamada a función:

```py
def sum(a, b, c):
    return a + b + c
nums = {'a': 2, 'b': 4, 'c': 1}

print(sum(**nums)) # 7
```

En el ejemplo anterior, `sum(**nums)` es equivalente a `sum(a=2, b=4, c=1)`.

Al final de tu código, imprime el resultado de llamar a la función **find_invalid_records**. Para sus argumentos, usa el operador `**` para desempaquetar `medical_records[0]`.

## Paso 23

El diccionario **constraints** contendrá cada clave que debes esperar tener en los datos para validar. El valor asociado a cada una indicará el resultado de la validación.

Agrega la clave `patient_id` al diccionario **constraints**. Para su valor, usa una llamada a **isinstance** pasando `patient_id` y `str` como argumentos.

## Paso 24

Como escribiste en el paso anterior, **patient_id** debería ser una cadena. Sin embargo, quieres verificar que también tenga un patrón específico.

Para eso, vas a usar una expresión regular. Por lo tanto, en la parte superior de tu código, usa la palabra clave `import` para importar el módulo `re`.

## Paso 25

Una expresión regular, o regex, es una estructura usada para coincidir con una secuencia de caracteres en texto. La función `search` del módulo `re` toma un patrón regex y una cadena como sus argumentos.

Devuelve un objeto de coincidencia correspondiente si el patrón produce una coincidencia. De lo contrario, devuelve **None**.

```py
# Código de ejemplo
import re

greeting = "Hello there!"
print(re.search('Hi', greeting)) # None
print(re.search('Hello', greeting)) # <re.Match object; span=(0, 5), match='Hello'>
```

Llama a `re.search` con la cadena **p** como primer argumento y **patient_id** como segundo argumento. Usa el operador `and` para agregar la llamada a la función como una segunda expresión al valor de tu clave **patient_id**.

```py
# Codigo de muestra
constraints = {
    'patient_id': isinstance(patient_id, str) and re.search('p', patient_id)
}
```

## Paso 26

Ahora puedes ver `{'patient_id': None}` impreso en el terminal porque la **p** minúscula no coincide con **P1001** y el operador `and` devuelve el primer valor falso de la expresión.

Quieres asegurarte de que el ID del paciente comience con la letra **p**, pero puede ser minúscula o mayúscula. Para modificar el comportamiento de coincidencia de las expresiones regulares, puedes usar flags. Por ejemplo, **re.search** acepta un tercer argumento para especificar cualquier flag:

```py
import re

greeting = "Hello there!"
print(re.search('hello', greeting)) # None

print(re.search('hello', greeting, re.IGNORECASE))
# <re.Match object; span=(0, 5), match='Hello'>
```

Agrega `re.IGNORECASE` como el tercer argumento a tu llamada **re.search**. Esto hará que tu búsqueda con regex no distinga entre mayúsculas y minúsculas.

Después de eso, verás que **None** es reemplazado por el objeto de coincidencia `<re.Match object; span=(0, 1), match='P'>`, donde **match** indica la coincidencia y **span** indica su ubicación en la cadena.

```py
# Codigo de muestra
constraints = {
    'patient_id': isinstance(patient_id, str) and re.search('p', patient_id, re.IGNORECASE)
}
# Output: {'patient_id': <re.Match object; span=(0, 1), match='P'>}
```

## Paso 27

Las expresiones regulares pueden contener secuencias especiales que consisten en una barra invertida (`\`) seguida de un carácter. Estas secuencias tienen un significado especial. Por ejemplo, `\d` coincide con un dígito decimal.

```py
# Codigo de ejemplo
import re

book = "Fahrenheit 451"
print(re.search('\d', book))
# <re.Match object; span=(11, 12), match='4'>
```

Después de la letra **p**, `patient_id` debe tener una serie de números. Entonces, modifica tu patrón regex para que tenga el carácter **p** seguido de la secuencia especial `\d`.

```py
# Codigo de muestra
constraints = {
    'patient_id': isinstance(patient_id, str) and re.search('p\d', patient_id, re.IGNORECASE)
}
# Output: {'patient_id': <re.Match object; span=(0, 2), match='P1'>}
```

## Paso 28

Los cuantificadores se usan en expresiones regulares para especificar cuántas veces un carácter puede repetirse. Por ejemplo, el carácter `+` coincide con el carácter anterior una o más veces:

```py
# Código de ejemplo
import re

book = "Fahrenheit 451"
print(re.search('\d', book))
# <re.Match object; span=(11, 12), match='4'>

print(re.search('\d+', book))
# <re.Match object; span=(11, 14), match='451'>
```

Entonces añade un cuantificador `+` a tu patrón regex para que coincida con uno o más dígitos.

```py
# Codigo de muestra
constraints = {
    'patient_id': isinstance(patient_id, str) and re.search('p\d+', patient_id, re.IGNORECASE)
}
# Output: {'patient_id': <re.Match object; span=(0, 5), match='P1001'>}
```

## Paso 29

Ahora que tu regex coincide con la letra `p` seguida de uno o más dígitos, lo último que necesitas verificar es que no se encuentren caracteres adicionales en la cadena.

Para eso puedes usar otra función del módulo `re`. La función **fullmatch** devuelve un objeto match cuando el patrón regex coincide con toda la cadena y **None** en caso contrario.

```py
# Código de ejemplo
import re

book = "Fahrenheit 451"
print(re.fullmatch('\d+', book)) #None

print(re.fullmatch('Fahrenheit \d+', book))
# <re.Match object; span=(0, 14), match='Fahrenheit 451'>
```

Reemplaza la llamada `search` con una llamada `fullmatch` manteniendo los mismos argumentos.

```py
# Codigo de muestra
constraints = {
    'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE)
}
# Output: {'patient_id': <re.Match object; span=(0, 5), match='P1001'>}
```

## Paso 30

A continuación, quieres verificar que `age` sea un entero. Así que agrega otra clave `age` al diccionario **constraints**. Para su valor, llama a **isinstance** pasando `age` e `int` como sus argumentos.

## Paso 31

`age` no solo debe ser un entero, debe ser un entero positivo mayor o igual a **18**.

Usando el operador `and`, añade una segunda expresión al valor de la clave `age` para verificar eso.

```py
# Código de muestra
'age': isinstance(age, int) and age >= 18
```

## Paso 32

Agrega otra clave **gender** al diccionario **constraints**. Siguiendo el formato de la expresión que escribiste en los pasos anteriores, verifica que **gender** sea una cadena. Luego, usa el operador `and` para comprobar que el **gender** en minúsculas esté en **('male', 'female')**.

```py
# Código de muestra
'gender': (isinstance(gender, str) and gender.lower() in ('male', 'female'))
```

## Paso 33

Ahora agrega una clave **diagnosis** al diccionario **constraints**. Para su valor, escribe una expresión que verifique que **diagnosis** sea una instancia de **str** o sea `None`.

```py
# Codigo de muestra
'diagnosis': isinstance(diagnosis, str) or diagnosis is None
```

## Paso 34

A continuación, agrega una clave **medications** al diccionario **constraints**. Para su valor, usa `isinstance` para verificar que **medications** sea una lista.

```py
# Codigo de muestra
'medications': isinstance(medications, list)
```

## Paso 35

Como aprendiste en una lección anterior, se puede usar una comprensión de listas para crear una lista a partir de un iterable existente:

```py
# Código de ejemplo
squares = [0, 1, 4, 9, 16, 25]

roots = [i ** 0.5 for i in squares]
print(roots) # [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
```

Cada elemento en la lista **medications** debe ser una cadena. En este paso y en el siguiente escribirás una expresión para verificar eso. Usa el operador `and` para agregar otra expresión al valor de la clave **medications**.

En el lado derecho del operador `and`, usa la sintaxis de comprensión de listas para crear una lista evaluando `isinstance(i, str)` para cada **i** en **medications**.

```py
# Codigo de muestra
'medications': isinstance(medications, list) and [isinstance(i, str) for i in medications]
```

## Paso 36

La función **all** devuelve **True** si todos los elementos del iterable que se le pasa son verdaderos, y **False** en caso contrario:

```py
# Código de ejemplo
truthy = [1, 2, 3]
print(all(truthy)) # True

falsy = [0, 1, 2, 3]
print(all(falsy)) # False
```

Pasa la lista `[isinstance(i, str) for i in medications]` a la función **all** para asegurarte de que cada elemento en ella sea una cadena.

```py
# Código de muestra
'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications])
```

## Paso 37

Agrega una última clave **last_visit_id** al diccionario **constraints**. Para su valor, usa `isinstance` para verificar que **last_visit_id** sea una cadena.

```py
# Codigo de muestra
'last_visit_id': isinstance(last_visit_id, str)
```

## Paso 38

Es hora de usar otra expresión regular. De manera similar a lo que ya hiciste, usa el operador `and` para agregar una expresión al valor actual de `constraints['last_visit_id']`.

En el lado derecho del operador **and**, usa la función **fullmatch** del módulo **re** para asegurarte de que **last_visit_id** comience con la letra **v** (ya sea minúscula o mayúscula) seguida de uno o más dígitos.

```py
# Codigo de muestra
'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
```

## Paso 39

Ahora que tu diccionario **constraints** está completo, cambiarás la sentencia **return** de `find_invalid_records` para que devuelva una lista de las claves inválidas.

Usando la sintaxis de comprensión de listas, devuelve una lista que evalúa **key** para cada `key, value` en **constraints.items()**.

```py
# Codigo de muestra
return [key for key, value in constraints.items()]
```

## Paso 40

Las comprensiones de listas también aceptan cláusulas `if` para filtrar elementos de un iterable:

```py
# Código de ejemplo
nums = [1, 2, 3, 4, 5, 6]
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums) # [2, 4, 6]
```

Como quieres devolver una lista que contenga solo las claves inválidas, agrega una cláusula **if** a tu comprensión para que cada **key** se agregue a la lista solo cuando **value** sea falso.

```py
# Codigo de muestra
return [key for key, value in constraints.items() if value == False]
# Alt: return [key for key, value in constraints.items() if not value]
```

## Paso 41

La función **find_invalid_records** está completa. Ahora, elimina `print(find_invalid_records(**medical_records[0]))` de tu código.

## Paso 42

Volviendo a la función **validate**, después de las dos sentencias **if** y aún dentro del bucle **for**, crea una variable llamada **invalid_records**.

Luego, asígnale una llamada a **find_invalid_records** usando el operador `**` para desempaquetar **dictionary**.

```py
# Codigo de muestra
invalid_records = find_invalid_records(**dictionary)
```

## Paso 43

Si pasas datos inválidos a la función **validate**, por ejemplo una lista que contiene elementos que no son diccionarios o diccionarios con claves faltantes y/o inválidas, Python generará un `AttributeError` y un `TypeError`, respectivamente. Siéntete libre de verificarlo modificando la lista **medical_records**.

Para evitar eso, después de establecer **is_invalid** en **True**, usa la palabra clave **continue** para saltar a la siguiente iteración en ambas sentencias **if**.

## Paso 44

Justo después de la variable **invalid_records**, crea un bucle **for** para iterar sobre ella. Para cada registro inválido, imprime **'Unexpected format `'<key>: <val>'` at position `<index>`.'**. Reemplaza `<key>`, `<val>` y `<index>` con la clave, valor e índice actuales.

Recuerda que **invalid_records** es una lista de claves que se refieren a registros inválidos en el **dictionary** actual. Necesitarás tomar la clave de **invalid_records** y buscar el valor en **dictionary**.

Posición o **index** se refiere al diccionario actual en **medical_records**, definido por el bucle **for** externo en la función.

Revisa tu código hasta ahora si necesitas recordarte de los bucles y variables ya creados.

Luego, establece **is_invalid** en **True**.

Siéntete libre de probar la función **validate** con datos inválidos para ver los mensajes de validación.

Con eso, el taller del validador médico está completo.

```py
# Codigo de muestra
for index, (key, value) in enumerate(invalid_records):
    print(f"Unexpected format '{key}: {value}' at position {index}.")
    is_invalid = True
```


