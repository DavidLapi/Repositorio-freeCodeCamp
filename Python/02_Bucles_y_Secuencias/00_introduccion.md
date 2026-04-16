# Trabajar con Bucles y Secuencias

## ¿Qué son las listas y cómo funcionan?

En las próximas lecciones vamos a aprender sobre *listas*, *tuplas* y *rangos*, que son tres tipos básicos de secuencias usadas en Python.

El tipo de dato **lista** (*array*) es una secuencia ordenada de elementos que pueden estar compuestos por cadenas, números o incluso otras listas. Las listas son mutables y usan indexación basada en cero, lo que significa que el primer elemento de la lista está en el índice cero.

Aquí está la sintaxis básica para una lista:

```py
cities = ['Los Angeles', 'London', 'Tokyo']
```

Para acceder a un elemento de la lista *cities*, puedes referenciar su número de índice en la secuencia. Aquí tienes un ejemplo de cómo acceder al primer elemento de la lista *cities*:

```py
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'
```

El indexado negativo se usa para acceder a elementos comenzando desde el final de la lista en lugar del principio en el índice *0*. Para acceder al último elemento de cualquier lista, puedes usar *-1* así:

```py
cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1] # 'Tokyo'
```

Otra forma de crear una lista es usar la estructura *list()*. La estructura *list()* se usa para convertir un iterable en una lista así:

```py
developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']
```

Un iterable es un tipo especial de objeto que puede ser recorrido uno por uno. Aprenderás más sobre los bucles en Python más adelante.

Para obtener el número total de elementos en una lista, puedes usar la función *len()* así:

```py
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5
```

Si quieres actualizar un valor en un índice particular, puedes hacer algo así:

```py
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']
```

Dado que las listas son mutables, puedes actualizar cualquier elemento en la lista siempre que pases un número de índice válido. Si pasas un índice (ya sea positivo o negativo) que está fuera de los límites de la lista, recibirás un *IndexError*:

```py
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""
```

Si quieres eliminar un elemento de una lista puedes usar la palabra clave **del** así:

```py
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']
```

A veces es útil verificar si un elemento está dentro de la lista. Para hacer eso, puedes usar la palabra clave **in** así:

```py
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False
```

A veces es común tener listas anidadas dentro de otras listas así:

```py
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
```

En este ejemplo, tenemos una lista anidada que contiene tres lenguajes de programación populares. Para acceder a la lista anidada, necesitarás acceder a ella usando el índice *2* ya que las listas están indexadas desde cero:

```py
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']
```

Luego, para acceder al segundo idioma de esa lista anidada, necesitarás acceder a él usando el índice *1* así:

```py
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # 'Rust'
```

Otra técnica común utilizada con listas es **desempaquetar valores**.

Desempaquetar valores de una lista es una técnica usada para asignar valores de una lista a nuevas variables. Aquí tienes un ejemplo de cómo desempaquetar una lista *developer* en nuevas variables llamadas *name*, *age* y *job*.

```py
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'
```

Aquí, *name* tiene el valor *'Alice'*, *age* tiene el valor *34*, y *job* tiene el valor *'Rust Developer'*.

Si necesitas recolectar cualquier elemento restante de una lista, puedes usar el operador asterisco (*) así:

```py
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']
```

En este ejemplo, *name* seguirá teniendo el valor *'Alice'*, y *rest* es una lista de dos elementos: el número *34* y la cadena *'Rust Developer'*.

Si la cantidad de variables en el lado izquierdo del operador de asignación no coincide con la cantidad total de elementos en la lista, entonces recibirás un *ValueError*:

```py
developer = ['Alice', 34, 'Rust Developer']
name, age, job, city = developer

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""
```

El último concepto que veremos es el operador slice (:). Similar a las cadenas, puedes acceder a porciones de una lista usando el operador slice de esta manera:

```py
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']
```

En este ejemplo, el índice de inicio es *1* ya que apunta al segundo elemento en la lista. Luego usamos el operador *slice* seguido de un índice final de *4*, que incluye todo hasta (pero sin incluir) el elemento en ese índice.

Otra cosa que puedes hacer con el operador de corte *:* es especificar un intervalo de paso que determina cuánto incrementar entre los índices. Supongamos que tienes una lista de números como esta:

```py
numbers = [1, 2, 3, 4, 5, 6]
```

Si quieres extraer una lista de solo números pares, puedes usar el operador de slicing así:

```py
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]
```

El primer número par está en el índice *1*, así que ese será el índice de inicio. Como queremos recorrer hasta el final de la lista, omitimos el índice de fin. Por último, especificamos *2* para el intervalo de paso opcional, de modo que solo incrementará en *2* en lugar del valor predeterminado *1*.

Las listas son una estructura de datos útil y flexible que usarás mucho en tus programas de Python. En la próxima lección, aprenderás sobre métodos comunes que puedes usar con listas.

## Preguntas

1. ¿Cuál de las siguientes afirmaciones es verdadera sobre las listas?

- [ ] Están indexadas con base en dos.
- [X] Están indexadas con base en cero.
- [ ] Sólo se utilizan dentro de las clases.
- [ ] Rara vez se utilizan en programas de Python.

2. ¿Cuál de las siguientes es la forma correcta de acceder a segundo elemento de la lista?

```py
cities = ['Los Angeles', 'London', 'Tokyo']
```

- [X] cities[1]
- [ ] cities[2]
- [ ] cities[0]
- [ ] cities[-1]

3. ¿Cuál de las siguientes es la forma correcta de acceder al segundo elemento desde el final?

```py
numbers = [1, 2, 3, 4, 5, 6]
```

- [ ] numbers[-5]
- [ ] numbers[2]
- [ ] numbers[0]
- [X] numbers[-2]