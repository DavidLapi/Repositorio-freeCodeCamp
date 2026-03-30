# Cadenas, parte 1

## ¿Qué son las cadenas y qué es la inmutabilidad de las cadenas?

Una cadena es una secuencia de caracteres rodeada por comillas simples o dobles. En algunos lenguajes de programación, los caracteres entre comillas simples se tratan de manera diferente que los rodeados por comillas dobles, pero en Python, se tratan por igual. Entonces, puedes usar cualquiera de las dos cuando trabajes con cadenas. Aquí hay algunos ejemplos de cadenas:

**Código de ejemplo:**

```py
my_str_1 = 'Hello'
my_str_2 = "World"
```

Si necesitas una cadena de múltiples líneas, puedes usar comillas triples dobles o simples:

**Código de ejemplo:**

```py
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
```

Si tu cadena contiene comillas simples o dobles, entonces tienes dos opciones:

1. Usa el tipo opuesto de comillas. Es decir, si tu cadena contiene comillas simples, usa comillas dobles para envolver la cadena, y viceversa:

```py
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```

2. Escapa la comilla simple o doble en la cadena con una barra invertida (*&#92;*). Con este método, puedes usar comillas simples o dobles para envolver la cadena en sí:

```py
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

A veces, puede que necesites verificar si una cadena contiene uno o más caracteres. Para eso, Python proporciona el operador *in*, que devuelve un booleano que especifica si el carácter o los caracteres existen en la cadena o no.

Aquí hay algunos ejemplos:

```py
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
```

Para obtener la longitud de una cadena, puedes usar la función incorporada *len()*. Aquí tienes un ejemplo:

```py
my_str = 'Hello world'
print(len(my_str))  # 11
```

Cada carácter en una cadena tiene una posición llamada índice. El índice es cero basado, lo que significa que el índice del primer carácter de una cadena es *0*, el índice del segundo carácter es *1*, y así sucesivamente. Para acceder a un carácter por su índice, usas corchetes (*[]*) con el índice del carácter que deseas acceder dentro. Aquí hay algunos ejemplos:

```py
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```

La indexación negativa también está permitida, por lo que puedes obtener el último carácter de cualquier cadena con *-1*, el penúltimo carácter con *-2*, y así sucesivamente:

```py
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l
```

Muchos otros lenguajes de programación agrupan los tipos de datos en tipos primitivos o de referencia. Los tipos primitivos son simples e inmutables, es decir, no se pueden cambiar una vez declarados. Los tipos de referencia pueden contener múltiples valores, y pueden ser mutables o inmutables. Pero Python no traza una línea dura entre esos dos grupos. En su lugar, todos los datos se tratan como objetos, y algunos objetos son inmutables mientras que otros son mutables.

Los tipos de datos inmutables no se pueden modificar o alterar una vez que se declaran. Puedes apuntar sus variables a algo nuevo, lo que se llama reasignación, pero no puedes cambiar el objeto original en sí mismo agregando, eliminando o reemplazando cualquiera de sus elementos.

Las cadenas son tipos de datos inmutables en Python. Esto significa que puedes reasignar una cadena diferente a una variable:

```py
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```

Pero no se permite la modificación directa de una cadena:

```py
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```

Ejemplos de otros tipos de datos inmutables en Python son integer, float, boolean, tuple y range. Conocerás cada uno de estos tipos en las próximas lecciones.

## Preguntas

1. ¿Cómo obtienes la longitud de una cadena *s*?

- [X] len(s)
- [ ] s.length
- [ ] Una cadena no tiene longitud.
- [ ] s.len()

2. ¿Cómo defines una cadena de múltiples líneas en Python?

- [ ] Usando paréntesis *()* alrededor de la derecha.
- [X] Usando comillas triples dobles *"""* o comillas triples simples *'''*.
- [ ] Usando una barra invertida *&#92;* al final de cada línea.
- [ ] Usando corchetes *[]* para encerra la cadena.

3. ¿Qué significa que una cadena sea inmutable?

- [ ] Una variable no puede ser reasignada a una cadena diferente.
- [ ] La reasignación de variables modifica directamente la cadena oeiginal.
- [X] Una cadena no puede ser modificada directamente cambiando sus caracteres individuales.
- [ ] Los caracteres de cadena solo pueden modificarse bajo condiciones específicas.