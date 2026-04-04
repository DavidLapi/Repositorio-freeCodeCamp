# Cadenas, parte 2

## ¿Qué son la concatenación de cadenas y la interpolación de cadenas?

Cuando trabajas con cadenas, combinar diferentes fragmentos de texto es una operación común con la que a menudo te encontrarás.

En Python, puedes combinar múltiples cadenas juntas con el operador más (*+*). Este proceso se llama **concatenación de cadenas**. Aquí te mostramos cómo concatenar dos cadenas con el operador más:

```py
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
```

Pero ten en cuenta que esto solo funciona con cadenas. Si intentas concatenar una cadena con un número, obtendrás un *TypeError*:

```py
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str
```

Esto sucede porque Python no convierte automáticamente otros tipos de datos como enteros en cadenas cuando los concatenas. Python requiere que todos los elementos sean cadenas antes de poder concatenarlos. 

Para solucionarlo, puedes convertir el número en una cadena de caracteres con la función integrada *str()*, que devuelve la representación en forma de cadena del objeto dado sin modificar el objeto original:

```py
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26
```

También puedes usar el operador de asignación aumentada para la concatenación. Este se representa con un más y un signo igual (*+=*), y realiza tanto la concatenación como la asignación en un solo paso. Aquí tienes cómo funciona:

```py
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26
```

El proceso de insertar variables y expresiones en una cadena se llama **interpolación de cadenas**. Python tiene una categoría de cadena llamada **f-strings** (abreviatura de literales de cadena formateados), que te permite manejar la interpolación con una sintaxis compacta y legible.

Las cadenas f comienzan con *f* (ya sea en minúsculas o mayúsculas) antes de las comillas, y te permiten insertar variables o expresiones dentro de campos de reemplazo indicados por llaves (*{}*). Aquí tienes un ejemplo:

```py
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
```

Observa que no necesitas convertir tipos no cadena con la función *str()*. En el ejemplo anterior, el valor de las variables *age*, *num1* y *num2* se convierte internamente en una cadena durante el proceso de interpolación.

## Preguntas

1. ¿Cómo puedes concatenar cadenas en Python?

- [X] Al usar el operador +.
- [ ] Usando el operador * para unir cadenas.
- [ ] Al usar el operador & para combinar cadenas.
- [ ] Asignando múltiples cadenas a una lista y luego imprimiéndolas juntas.

2. ¿Qué hace la función str()?

- [ ] Concatena dos cadenas juntas.
- [X] Devuelve una versión en cadena del objeto dado.
- [ ] Extrae caracteres numéricos de una secuencia alfanumérica.
- [ ] Reemplaza los caracteres proporcionados dentro de una cadena.

3. ¿Qué es la interpolación de cadenas?

- [ ] El proceso de analizar una cadena para extraer porciones específicas.
- [ ] El proceso de dividir una cadena en subcadenas.
- [X] El proceso de insertar variables y expresiones en una cadena.
- [ ] El proceso de unir dos o más cadenas juntas.