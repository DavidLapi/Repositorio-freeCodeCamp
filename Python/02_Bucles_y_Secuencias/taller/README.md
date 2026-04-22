# Taller: Construir un estractor de pines

## Paso 1

En este taller crearás un extractor de pines, los dígitos del pin están ocultos en cada línea de un poema.

Comienza creando una función llamada *pin_extractor* con un parámetro *poem*. Una función vacía da un error, así que agrega **pass** dentro de la función momentáneamente para que sea válida.

## Paso 2

Necesitarás una variable para almacenar el código secreto mientras lo descifras, así que elimina **pass** y crea una variable llamada *secret_code* dentro de la función y asígnale una cadena vacía.

## Paso 3

Mientras trabajas en la función, sería útil tener una llamada a la función para propósitos de depuración, así que crea una variable *poem*, fuera de la función, que contenga este poema:

```py
# Código de ejemplo
"""
Stars and the moon
shine in the sky
white and bright
until the end of the night
"""
```

Puedes usar una cadena de múltiples líneas para eso.

Y luego, llama a la función con la variable poem como argumento.

## Paso 4

Ahora que has agregado una llamada a función, puedes ver cualquier error creado dentro de la función en la terminal, y siempre puedes usar *print* para ver el valor de las cosas.

Hay un dígito del pin oculto en cada línea, así que dentro de la función usa el método *split* para dividir la cadena en una lista de líneas. Divide las líneas usando el carácter de nueva línea (\n), y asigna la lista resultante a una variable llamada *lines*.

## Paso 5

Necesitas trabajar en cada línea de forma independiente: crea un bucle *for* sobre *lines* que use *line* como variable del ciclo. Dentro del bucle, imprime *line*.

## Paso 6

El dígito n-ésimo del pin está oculto como la longitud de la palabra n-ésima en la línea n-ésima.

Para encontrar la longitud de la palabra n, el siguiente paso es separar la línea del poema en una lista de palabras: dentro del bucle, crea una variable *words* y asígnale el valor de *line* dividido en palabras usando el método *split*.

Luego, agrega una llamada a *print* con *words* como argumento.

## Paso 7

Como aprendiste en una lección anterior, la función *enumerate* permite llevar un registro del índice mientras se itera sobre un iterable:

```py
# Código de ejemplo
fruits = ['apple', 'plum', 'bananas']

for index, item in enumerate(fruits):
    print(index, item)

# 0 apple
# 1 plum
# 2 bananas
```

El dígito n-ésimo del código secreto proviene de la palabra n-ésima de la línea n-ésima, así que necesitas saber cuál es el número de cada línea.

Cambia el bucle para que itere sobre *enumerate(lines)*, y agrega otra variable de bucle antes de *line* llamada *line_index*.

Además, actualiza la llamada *print* a *print(line_index, line)*.

## Paso 8

En la última línea del ciclo, actualiza la llamada a *print* para que imprima la palabra dentro de la lista *words* en el índice *line_index*.

```py
print(words[line_index])
```

## Paso 9

La función *len* da la longitud de una cadena. Actualiza la segunda llamada a *print* para imprimir la longitud de esa palabra.

```py
print(len(words[line_index]))
```

## Paso 10

La longitud devuelta por *len* es un entero, necesitas convertirlo a una cadena usando la función *str* para poder agregarlo a la cadena *secret_code*.

Actualiza la llamada a *print* para imprimir la longitud como una cadena.

```py
print(str(len(words[line_index])))
```

## Paso 11

Ahora puedes concatenar **str(len(words[line_index]))** a **secret_code**. Elimina la llamada a *print* y usa la asignación aumentada += para la concatenación.

```py
secret_code += str(len(words[line_index]))
```

## Paso 12

Elimina las dos llamadas a print y agrega una sentencia *return* que devuelva *secret_code* en la última línea de la función.

```py
return secret_code
```

## Paso 13

Pasa *pin_extractor(poem)* a la función *print* para que puedas ver qué está devolviendo la función.

## Paso 14

Ahora la función está haciendo un buen trabajo extrayendo el código del poema, pero hay un caso límite que considerar: la línea del poema podría ser más corta de lo esperado, y eso haría que la función falle (puedes probar esto eliminando la palabra *bright* del poema).

Pon la línea **secret_code += str(len(words[line_index]))** dentro de una estructura *if* que verifique que hay suficientes palabras en la lista *words*.

```py
if (len(words) > line_index):
    secret_code += str(len(words[line_index]))
```

## Paso 15

La tercera línea del poema carece de una tercera palabra, por lo que el pin es más corto de lo esperado.

Agrega una cláusula *else* que concatene un *'0'* a *secret_code* cuando no haya suficientes palabras, para que todas las líneas del poema se usen para encontrar dígitos.

```py
else:
    secret_code += "0"
```

## Paso 16

Ahora el extractor de pines funciona, ¡pero podría ser más eficiente! ¡Podría extraer el pin de muchos poemas al mismo tiempo!

Agrega dos poemas más en el ámbito global, **poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'** y **poem3 = 'There\nonce\nwas\na\ndragon'**, y por ahora, comenta el *print* con la llamada a *pin_extractor*.

## Paso 17

Actualiza el argumento de la función para que sea *poems*, luego crea un bucle *for* alrededor de todo el contenido actual de la función que itere sobre *poems* y use *poem* como variable del bucle.

```py
def pin_extractor(poems):
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        return secret_code
```

## Paso 18

Antes del bucle, crea una nueva variable *secret_codes* que tenga un valor inicial de una lista vacía.

Luego reemplaza la línea *return secret_code* con una línea que agregue *secret_code* a la lista *secret_codes*.

```py
def pin_extractor(poems):
    # Variable de lista vacia 
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        # Agregar variable de codigo a la lista
        secret_codes.append(secret_code)
```

## Paso 19

Finalmente, devuelve *secret_codes*, luego descomenta la llamada a la función y actualiza el argumento para que sea **[poem, poem2, poem3]**. Ahora tu función funciona con varios poemas a la vez y puede extraer múltiples pines.

La función *pin_extractor* está completada.

## Resultado

```py
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))

# Output: ['5262', '3346', '50000']
```

