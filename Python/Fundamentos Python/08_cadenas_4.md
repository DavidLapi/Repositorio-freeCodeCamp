# Cadenas, parte 4

## ¿Cuáles son algunos métodos comunes de cadenas?

Python ofrece una serie de métodos integrados que hacen que trabajar con cadenas sea muy fácil. Incluyen, pero no se limitan a, los siguientes:

- *upper()*: Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas.

```py
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

- *lower()*: Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas.

```py
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```

- *strip()*: Devuelve una nueva cadena con los caracteres especificados de inicio y final eliminados. Si no se pasa ningún argumento, elimina los espacios en blanco de inicio y final.

```py
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
```

- *replace(viejo, nuevo)*: Devuelve una nueva cadena con todas las ocurrencias de *viejo* reemplazadas por *nuevo*.

```py
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
```

- *split(separador)*: Divide una cadena en un separador especificado en una lista de cadenas. Si no se especifica un separador, divide por espacios en blanco.

```py
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```

- *join(iterable)*: Une elementos de un iterable en una cadena con un separador.

```py
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```

- *startswith(prefijo)*: Devuelve un valor booleano indicando si una cadena comienza con el prefijo especificado.

```py
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```

- *endswith(sufijo)*: Devuelve un valor booleano indicando si una cadena termina con el sufijo especificado.

```py
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```

- *find(subcadena)*: Devuelve el índice de la primera ocurrencia de *subcadena*, o *-1* si no encuentra ninguna.

```py
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```

- *count(subcadena)*: Devuelve el número de veces que una *subcadena* aparece en una cadena.

```py
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```

- *capitalize()*: Devuelve una nueva cadena con el primer carácter en mayúscula y los demás caracteres en minúscula.

```py
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

- *isupper()*: Devuelve True si todas las letras en la cadena están en mayúsculas y False si no.

```py
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

- *islower()*: Devuelve True si todas las letras en la cadena están en minúsculas y False si no.

```py
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

- *title()*: Devuelve una nueva cadena con la primera letra de cada palabra en mayúscula.

```py
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```

## Preguntas

1. ¿Qué métodos verifican si todas las letras en una cadena están en mayúsculas y si todas las letras están en minúsculas?

- [ ] upper() y lower()
- [X] isupper() y islower()
- [ ] toupper() y tolower()
- [ ] uppercase() y lowercase()

2. ¿Cómo puedes reemplazar todas las ocurrencias de una o más partes de una cadena por otra cadena?

- [ ] Usando el método change() con dos argumentos.
- [X] Usando el método replace() con texto viejo y nuevo.
- [ ] Usando la función modify() con reglas de reemplazo.
- [ ] Usando el método update() con un diccionario de mapeo.

3. ¿Qué hace el método upper()?

- [ ] Convierte todos los caracteres a minúsculas.
- [ ] Solo capitaliza la primera letra.
- [X] Convierte todos los caracteres a mayúsculas.
- [ ] Elimina todos los espacios en blanco.