# Revisión de Diccionarios y Conjuntos

## Diccionarios

- **Definición**: Los diccionarios son estructuras de datos integradas que almacenan colecciones de pares clave-valor. Las claves deben ser tipos de datos inmutables. Esta es la sintaxis general de un diccionario en Python:

```py
dictionary = {
    key1: value1,
    key2: value2
}
```

- **Constructor `dict()`**: El constructor `dict()` es una forma alternativa de construir el diccionario. Pasas una lista de tuplas como argumento al constructor `dict()`. Estas tuplas contienen la clave como el primer elemento y el valor como el segundo elemento.
```py
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
```

- **Notación de corchetes:** Para acceder al valor de un par clave-valor, puedes usar la sintaxis conocida como notación de corchetes.

```py
dictionary[key]
```

## Métodos Comunes del Diccionario

- **Método `get()`:** El método `get()` recupera el valor asociado con una clave. Es similar a la notación de corchetes, pero te permite establecer un valor predeterminado, evitando errores si la clave no existe.

```py
dictionary.get(key, default)
```

- **Métodos `keys()` y `values()`:** Los métodos `keys()` y `values()` devuelven un objeto vista con todas las claves y valores del diccionario, respectivamente. Un objeto vista es una forma de ver el contenido de un diccionario sin crear una copia separada de los datos.

```py
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250
}

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])
```

- **Método `items()`:** El método items() devuelve un objeto vista con todos los pares clave-valor en el diccionario, incluyendo tanto las claves como los valores.

```py
pizza.items()
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])
```

- **Método `clear()`:** El método `clear()` elimina todos los pares clave-valor del diccionario.

```py
pizza.clear()
```

- **Método `pop()`:** El método `pop()` elimina el par clave-valor con la clave especificada como el primer argumento y devuelve su valor. Si la clave no existe, devuelve el valor predeterminado especificado como el segundo argumento. Si la clave no existe y no se especifica un valor predeterminado, se genera un `KeyError`.

```py
pizza.pop('price', 10)
pizza.pop('total_price') # KeyError
```
