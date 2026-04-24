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