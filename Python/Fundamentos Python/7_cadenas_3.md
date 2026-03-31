# Cadenas, parte 3

## ¿Qué es el corte de cadenas y cómo funciona?

En una lección anterior, aprendiste cómo cada carácter en una cadena puede ser identificado por su índice (comenzando desde cero) y accedido usando la notación de corchetes:

```py
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d
```

El **corte de cadenas** te permite extraer una porción de una cadena o trabajar solo con una parte específica de ella. Aquí está la sintaxis básica:

```py
string[start:stop]
```

Si deseas extraer caracteres desde un cierto índice hasta otro, simplemente separa los índices *inicio* (start) y *fin* (stop) con dos puntos:

```py
my_str = 'Hello world'
print(my_str[1:4]) # ell
```

Ten en cuenta que el índice *fin* no es inclusivo, por lo que *[1:4]* solo extrae los caracteres desde el índice *1*, y hasta, pero sin incluir, el carácter en el índice *4*.

También puedes omitir los índices de *inicio* y *fin*, y Python predeterminadamente tomará *0* o el final de la cadena, respectivamente. Por ejemplo, esto es lo que ocurre si omites el índice de *inicio*:

```py
my_str = 'Hello world'
print(my_str[:7])  # Hello w
```

Esto extrae todo desde el índice *0* hasta (pero sin incluir), el carácter en el índice *7*. Y esto es lo que ocurre si omites el índice de *fin*:

```py
my_str = 'Hello world'
print(my_str[8:])  # rld
```

Esto extrae todo desde el carácter en el índice *8* hasta el final de la cadena.

Ten en cuenta que cortar una cadena no modifica la cadena original:

```py
my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world
```

También puedes omitir tanto los índices de *inicio* como de *fin*, lo que extraerá toda la cadena:

```py
my_str = 'Hello world'
print(my_str[:])  # Hello world
```

Además de los índices *start+ y *stop*, también existe un parámetro opcional *step*, que se usa para especificar el incremento entre cada índice en el slice.

Aquí está la sintaxis para eso:

```py
string[start:stop:step]
```

En el ejemplo a continuación, la división comienza en el índice *0*, se detiene antes del *11*, y extrae cada segundo carácter:

```py
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
```

Un truco útil que puedes hacer con el parámetro *step* es invertir una cadena configurando el paso a *-1*, y dejando en blanco *inicio* y *fin*:

```py
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
```

## Preguntas

1. ¿Cómo extraes una porción específica de una cadena en Python?

- [ ] Usando paréntesis con posiciones de inicio y fin.
- [ ] Usando llaves con posiciones de inicio y fin.
- [X] Usando corchetes con posiciones de inicio y fin.
- [ ] Usando paréntesis angulares con posiciones de inicio y fin.

2. ¿Cuál es el resultado de 'Hello'[2:]?

- [X] *llo*
- [ ] *lo*
- [ ] *el*
- [ ] *l*

3. ¿Cuál es el propósito del parámetro opcional *step* en el corte de cadenas?

- [ ] Especifica si la cadena segmentada debe cambiarse en el lugar o no.
- [X] Especifica el incremento entre cada carácter a extraer.
- [ ] Garantiza que se extraigan todos los caracteres.
- [ ] Especifica un número máximo de caracteres repetidos para extraer.