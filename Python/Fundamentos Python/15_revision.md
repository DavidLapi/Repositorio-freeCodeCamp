# Revisión de conceptos básicos de Python

## ¿Qué es Python?

- **Introducción:** Python es un lenguaje de programación de propósito general conocido por su simplicidad y facilidad de uso. Python se usa en muchos campos como la ciencia de datos y el aprendizaje automático, desarrollo web, secuencias de comandos y automatización, sistemas embebidos e IoT, y mucho más.

- **Casos de Uso Comunes:** Python se usa en la ciencia de datos, el aprendizaje automático, el desarrollo web, la ciberseguridad, la automatización y microcomputadores como las placas Raspberry Pi y compatibles con MicroPython.

## Python en tu Entorno Local

- **Instalación:** La mejor manera de instalar Python en Windows, Mac y Linux es descargar el instalador desde el sitio web oficial de Python (*https://www.python.org/*).

## Variables

- **Declaración:** Para declarar una variable, se empieza con el nombre de la variable seguido por el operador asignado (*=*) y después el valor. Ese valor puede ser un número, cadena, booleano, etc. Aquí hay algunos ejemplos:

```py
name = 'John Doe'
age = 25
```

- **Convenciones para Nombrar Variables:** Aquí están las convenciones de nombres que debes usar para variables:

1. Los nombres de las variables sólo pueden comenzar con una letra o un guion bajo (_) y no un número.
2. Los nombres de las variables sólo pueden contener caracteres alfanuméricos (a-z, A-Z, 0-9) y guiones bajos (_).
3. Los nombres de las variables son sensibles a mayúsculas — *age*, *Age*, y *AGE* se consideran únicos.
4. Los nombres de las variables no pueden ser una de las palabras clave reservadas de Python como *if*, *class* o *def*.
5. Los nombres de variables con múltiples palabras están separados por guiones bajos. Ej. *snake_case*.

## Comentarios

- **Comentarios de Línea Única:** Este tipo de comentarios debe utilizarse para notas cortas que desees dejar en tu código.
```py
# This is a single line comment
```

- **Cadenas multilínea:** Este tipo de cadenas se pueden usar para dejar notas más extensas o para comentar secciones de código.

```py
"""
This is a multi-line string.
Here is some code commented out.

name = 'John Doe'
age = 25
"""
```

- **Función print():** Para imprimir datos en la consola, puedes usar la función *print()* de esta manera:

```py
print('Hello world!') # Hello world!
```

## Tipos Comunes de Datos de Python

- **Introducción:** Python es un lenguaje de tipado dinámico como JavaScript, lo que significa que no necesitas declarar explícitamente los tipos para las variables. El lenguaje sabe cuál es el tipo de una variable según lo que asignes a la variable.

- **Entero:** Un número entero sin decimales:

```py
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10
```

- **Flotante:** Un número con decimales:

```py
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5
```

- **Cadena:** Una secuencia de caracteres envuelta entre comillas:

```py
my_string_var = 'hello'
print('String:', my_string_var) # String: hello
```

- **Booleano:** Un valor que representa *True* o *False*:

```py
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
```

- **Conjunto:** Una colección desordenada de elementos únicos:

```py
my_set_var = {7, 5, 8}
print('Set:', my_set_var) # Set: {7, 5, 8}
```

- **Diccionario:** Una colección de pares clave-valor encerrados entre llaves:

```py
my_dictionary_var = {"name": "Alice", "age": 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
```

- **Tupla:** Una colección ordenada e inmutable, rodeada por paréntesis:

```py
my_tuple_var = (7, 5, 8)
print('Tuple:', my_tuple_var) # Tuple: (7, 5, 8)
```

- **Rango:** Una secuencia de números, que se usa a menudo en bucles:

```py
my_range_var = range(5)
print(my_range_var) # range(0, 5)
```

- **Lista:** Una colección ordenada de elementos que admite diferentes tipos de datos:

```py
my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]
```

- **Ninguno:** Un valor especial que representa la ausencia de valor:

```py
my_none_var = None
print('None:', my_none_var) # None: None
```

## Tipos Inmutables y Mutables

- **Tipos Inmutables:** Estos tipos no pueden cambiar una vez declarados, aunque se puede redirigir sus variables a algo nuevo, lo que se llama reasignación. Incluyen entero, flotante, complejo, booleano, cadena, tupla, rango y *None*.

- **Tipos Mutables:** Estos tipos pueden cambiar una vez declarados. Puedes agregar, eliminar o actualizar sus elementos. Incluyen tipos de colección como listas, conjuntos y diccionarios.

- **Función type():** Para ver el tipo de una variable, puedes usar la función *type()* de esta manera:

```py
greeting = 'Hello there!'
age = 21

print(type(greeting)) # <class 'str'>
print(type(age)) # <class 'int'>
```

- **Función isinstance():** Se usa para verificar si una variable coincide con un tipo de dato específico:

```py
greeting = 'Hello world'
name = 'John Doe'

print(isinstance(greeting, str)) # True
print(isinstance(name, int)) # False
```

## Trabajando con Cadenas de Caracteres

- **Definición:** Como recuerdas de JavaScript, las cadenas de caracteres son inmutables, lo que significa que no puedes cambiarlas después de que se hayan creado. En Python, puedes usar comillas simples o dobles. Es recomendable elegir una comilla y cumplirla:

```py
developer = 'Jessica'
city = "Los Angeles"
```

- **Accediendo a Caracteres de Cadenas:** Puedes acceder a caracteres de cadenas utilizando la notación de corchetes de esta manera:

```py
my_str = 'Hello world'

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l
```

- **Escape de Cadenas:** Puedes usar una barra invertida (\\) si tu cadena contiene comillas de esta manera:

```py
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

- **Concatenación de Cadenas:** Para concatenar cadenas, puedes usar el operador + de esta manera:

```py
developer = 'Jessica'
print('My name is ' + developer + '.') # My name is Jessica.
```
