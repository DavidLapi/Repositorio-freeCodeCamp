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

