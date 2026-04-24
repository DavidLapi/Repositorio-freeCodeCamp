# Trabajar con Diccionarios y Conjuntos

## ¿Cuáles son algunas técnicas comunes para iterar sobre un diccionario?

Puedes iterar sobre un diccionario si necesitas acceder y procesar sus pares clave-valor. Esto es útil para actualizar sus valores o aplicar alguna lógica a ellos.

Echemos un vistazo a algunas de las técnicas que puedes usar.

Digamos que tenemos un diccionario **products** que asocia cada producto con su precio:

```py
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
```

Si queremos ofrecer un descuento del 20% en todos nuestros productos, podemos recorrer todos los pares clave-valor y modificar los precios.

Los métodos **.values()**, **.keys()** y **.items()** son esenciales para estas técnicas. Los cubrimos brevemente en una lección anterior.

Devuelven un objeto vista con los valores, las claves y los pares clave-valor del diccionario. Puedes usar estos objetos vista en bucles **for** para iterar sobre los elementos.

Por ejemplo, puedes iterar sobre todos los valores del diccionario así.

Escribes **for**, la variable del bucle (**price** en este caso), **products.values()** para obtener todos los valores del diccionario **products**, dos puntos (:), y luego el cuerpo del bucle, donde puedes aplicar cualquier lógica a los valores. En este caso, los estamos imprimiendo.

La variable del ciclo tomará cada uno de los valores, uno por iteración:

```py
for price in products.values():
    print(price)
```

Y aquí está la salida. Como puedes ver, cada valor se imprime en la consola, uno por uno:

```py
990
600
250
70
```

Esto funciona exactamente igual para **.keys()** si necesitas iterar sobre las llaves de un diccionario. Solo necesitas iterar sobre **products.keys()** o directamente sobre **products**, y asignar un nombre descriptivo para la variable del ciclo:

```py
for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)
```

Esta es la salida. Cada clave se imprime en la consola, una a la vez:

```py
Laptop
Smartphone
Tablet
Headphones
```

Y esto funciona exactamente igual para pares clave-valor si necesitas iterar sobre las claves y sus valores correspondientes simultáneamente. Solo necesitas iterar sobre **products.items()**:

```py
for product in products.items():
    print(product)
```

Esta es la salida. Ahora obtienes tuplas individuales con las claves y sus valores correspondientes:

```py
('Laptop', 990)
('Smartphone', 600)
('Tablet', 250)
('Headphones', 70)
```

Si quieres almacenar la clave y el valor en variables de bucle separadas, solo necesitas definirlas y separarlas con una coma. Luego, puedes usarlas en el cuerpo del bucle.

Aquí, estamos definiendo una variable de bucle **product** y una variable de bucle **price**. Cada una contendrá su valor correspondiente. Es importante definirlas en orden: primero la clave y luego el valor:

```py
for product, price in products.items():
    print(product, price)
```

Esta es la salida. Las estamos imprimiendo lado a lado, pero puedes usar estos valores como los necesites en tu código.

```py
Laptop 990
Smartphone 600
Tablet 250
Headphones 70
```

Ahora que sabes más sobre esto, podemos volver a nuestro ejemplo inicial. Si queremos ofrecer un descuento del 20%, multiplicaríamos cada precio por **0.8** y lo reasignaríamos como el valor de esa clave de producto.

También podríamos redondear el resultado hacia abajo si queremos trabajar con enteros:

```py
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)
```

Luego, si imprimimos el diccionario, obtendríamos estos pares clave-valor con los precios descontados:

```py
{
    'Laptop': 792, 
    'Smartphone': 480, 
    'Tablet': 200, 
    'Headphones': 56
}
```

Y finalmente, si necesitas iterar sobre los pares clave-valor mientras llevas un contador, puedes llamar a la función **enumerate()**. Este contador actúa esencialmente como una especie de "índice" o "conteo" para ese elemento dentro del ciclo.

La función devuelve un objeto **enumerate**, que asigna un entero a cada par clave-valor, como un contador. Puedes iniciar el contador desde cualquier número, pero por defecto, comienza desde 0.

Aquí, estamos iterando sobre las claves del diccionario **products**:

```py
for product in enumerate(products):
    print(product)
```

Pero la función **enumerate()** también asigna un entero a cada clave, por lo que obtenemos tuplas con el entero y la clave.

Aquí está la salida:

```py
(0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones')
```

Si necesitas, puedes asignar estos valores a variables de bucle separadas. Aquí, tenemos dos variables de bucle (**index** y **product**). Esto es lo que comúnmente verás y usarás cuando trabajes con **enumerate()**:

```py
for index, product in enumerate(products):
    print(index, product)
```

Si necesitas iterar sobre los valores, puedes reemplazar **products** por **products.values()**:

```py
for price in enumerate(products.values()):
    print(price)
```

La salida tendrá el índice y el precio en cada tupla:

```py
(0, 990)
(1, 600)
(2, 250)
(3, 70)
```

También puedes asignarlos a variables de bucle separadas:

```py
for index, price in enumerate(products.values()):
    print(index, price)
```

Esta será la salida. Puedes usarlas como necesites en tu código:

```py
0 990
1 600
2 250
3 70
```

Y con **products.items()**, puedes obtener el par clave-valor completo además del "índice" o "contador":

```py
for index, product in enumerate(products.items()):
    print(index, product)
```

En este ejemplo, obtenemos el índice seguido de una tupla que contiene la clave y el valor del par clave-valor correspondiente:

```py
0 ('Laptop', 990)
1 ('Smartphone', 600)
2 ('Tablet', 250)
3 ('Headphones', 70)
```

Para personalizar el valor inicial del conteo, puedes pasar un segundo argumento a **enumerate()**. Por ejemplo, aquí estamos comenzando el conteo desde 1:

```py
for index, product in enumerate(products.items(), 1):
    print(index, product)
```

Puedes ver este cambio en la salida. Ahora el primer entero es 1 en lugar de 0:

```py
1 ('Laptop', 990)
2 ('Smartphone', 600)
3 ('Tablet', 250)
4 ('Headphones', 70)
```

Esto funciona con cualquier variación que hayamos visto hasta ahora. Solo necesitas pasar el número inicial como el segundo argumento.

Hay muchas técnicas para iterar sobre un diccionario. Estas son algunas formas comunes, y tendrás que elegir la mejor para tu proyecto.

## Preguntas

1. ¿Qué método de diccionario, cuando se usa en un bucle, te permite acceder a los pares clave-valor almacenados en el diccionario?

- [ ] .keys()
- [X] .items()
- [ ] .values()
- [ ] .enumerate()

2. Al usar la función **enumerate()** con **dictionary.items()**, ¿qué representa la primera variable del ciclo?

- [ ] Las claves del diccionario.
- [ ] Los valores del diccionario.
- [X] El indice o conteo del par clave-valor.
- [ ] El par clave-valor como una tupla.

3. ¿Qué método usarías si necesitas iterar sobre un diccionario y acceder solo a las claves?

- [X] .keys()
- [ ] .values()
- [ ] .enumerate()
- [ ] .items()

