# Variables y tipos de datos, parte 3

## ¿Cuáles son los tipos de datos comunes en Python y cómo obtienes el tipo de una variable?

Antes de trabajar con variables de Python, es importante entender los tipos de datos. Un tipo de dato describe el tipo de valor que una variable contiene. Por ejemplo, un número, un texto o una lista de elementos. Los lenguajes de programación usan tipos de datos para saber cómo almacenar y trabajar con diferentes tipos de información.

Python es un lenguaje de tipado dinámico como JavaScript, lo que significa que no es necesario declarar explícitamente tipos para las variables. El lenguaje sabe qué tipo de dato es una variable basado en lo que le asignes.

Aquí hay algunos ejemplos:

```py
name = 'David Hasselhoff' # Python sabe que esto es una cadena de texto o 'string'
age = 25 # Python sabe que esto es un numero entero o 'integer'
```

Esto contrasta con algunos lenguajes de tipado estático como C#, Java y C++, donde tienes que declarar tipos con variables, como esto:

```py
string name = 'David Hasselhoff'
int age = 25
```

La naturaleza de tipado dinámico de Python hace que la codificación sea realmente rápida y más flexible, pero puede llevar a errores inesperados porque los errores de tipo solo se detectan cuando se ejecuta un programa, no cuando se compila.

Como Python determina los tipos de datos mientras tu programa está **ejecutándose**, los errores relacionados con tipos solo se descubren en ese momento. Cuando un programa se ejecuta, Python procesa tu código línea por línea. Si llega a una línea donde se espera que un cierto objeto se comporte de una manera que no puede, Python se detendrá y mostrará un error.

En contraste, algunos lenguajes **compilan** tu programa antes de que se ejecute. Compilar significa que la computadora verifica tu código con anticipación y lo prepara para ejecutarse. Durante este paso, esos lenguajes pueden detectar errores de tipo antes de que el programa siquiera comience.

No necesitas conocer esos lenguajes todavía. La idea importante es simplemente:

- **En Python, los errores de tipo pueden revelarse durante la ejecución**, cuando el programa está realmente corriendo y usando tu código.

- **Los lenguajes compilados detectan errores de tipo durante el paso de compilación**, antes de que se permita ejecutar el programa.

Debido a esto, puede que no te des cuenta de un error de tipo en Python hasta que el programa llegue a esa línea específica de código mientras se ejecuta.

Estos son los tipos de datos más comunes que usarás en Python:

1. **Entero**: Un número entero sin decimales, por ejemplo, *10* o *-5*.

```py
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10
```

2. **Flotante**: Un número con un punto decimal, como *4.41* o *-0.4*.

```py
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5
```

3. **Cadena**: Una secuencia de caracteres encerrados en comillas simples o dobles como *'¡Hola mundo!'*.

```py
my_string_var = 'hello'
print('String:', my_string_var) # String: hello
```

4. **Booleano**: Un tipo verdadero o falso, escrito como *True* o *False*.

```py
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
```

5. **Conjunto**: Una colección no ordenada de elementos únicos, como *{0.5, 4, 'apple'}*.

```py
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}
```

6. **Diccionario**: Una colección de pares clave-valor encerrados en llaves, como *{'nombre': 'John Doe', 'edad': 28}*.

```py
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
```

7. **Tupla**: Una colección ordenada e inmutable, encerrada entre paréntesis, como *('apple', 4.5, 7)*.

```py
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)
```

8. **Rango**: Una secuencia de números, a menudo usada en bucles, por ejemplo, *range(5)*.

```py
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)
```

9. **Lista**: Una colección ordenada de elementos que admite diferentes tipos de datos.

```py
my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]
```

10. **Ninguno**: Un valor especial que representa la ausencia de un valor.

```py
my_none_var = None
print('None:', my_none_var) # None: None
```

Para obtener el tipo de dato de una variable, puedes usar la función *type()*:

```py
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1)) # <class 'str'>
print(type (my_var_2)) # <class 'int'>
```

Y aquí están todos los tipos de datos cubiertos en esta lección, junto con sus tipos en el terminal:

```py
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>
```

La función incorporada *isinstance()* te permite verificar si una variable coincide con un tipo de dato específico. Recibe un objeto y el tipo contra el que quieres comprobarlo, luego devuelve un booleano. Aquí tienes algunos ejemplos:

```py
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False
```

## Preguntas

1. ¿Qué significa que Python sea de tipado dinámico?

- [ ] Debe especificar manualmente el tipo de dato de cada variable.
- [ ] Python no admite diferentes tipos de datos.
- [X] Python determina automáticamente el tipo de dato según el valor asignado.
- [ ] Las variables en Python no pueden cambiar su tipo de dato después de la asignación.

2. ¿Cuál es la diferencia entre los tipos de datos enteros y flotantes?

- [ ] Los enteros pueden almacenar números positivos y negativos, mientras que los flotantes solo pueden almacenar números positivos.
- [X] Los enteros son números enteros sin decimales, mientras que los flotantes son números con puntos decimales.
- [ ] Los flotantes ocupan menos memoria que los enteros en Python.
- [ ] Los enteros solo pueden almacenar números hasta 1000, mientras que los flotantes no tienen límite.

3. ¿Cómo se puede comprobar el tipo de dato de una variable en Python?

- [X] Usando la función *type()*, como *type(my_var)*.
- [ ] Comprobando manualmente el valor de la variable.
- [ ] Usando la función *typeof*, como *typeof(my_var)*.
- [ ] Convirtiendo la variable a una cadena y analizando sus caracteres. 