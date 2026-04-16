# Ejercicio 5: Construir un Cifrado César

## Paso 1

Como recordarás de lecciones anteriores, en Python, declaras una variable escribiendo el nombre de la variable a la izquierda del operador de asignación (=) y el valor a asignar a la derecha:

```py
variable_name = value
```

Crea una variable llamada *shift* y asigna el valor 5 a tu nueva variable.

## Paso 2

En lecciones anteriores, aprendiste sobre diferentes tipos de datos que puedes almacenar en una variable. Acabas de asignar un valor entero. Ahora necesitas asignar una cadena, que es una secuencia de caracteres encerrada entre comillas simples o dobles:

```py
string_1 = 'I am a string'
string_2 = "I am also a string"
```

Declara otra variable llamada *alphabet* y asigna la cadena *'abcdefghijklmnopqrstuvwxyz'* a esta variable.

## Paso 3

En este taller, vas a construir un **cifrado de César**. Ésta es una de las técnicas más simples para encriptar texto, que consiste en sustituir cada letra del texto plano con la letra que se encuentra a un número fijo de posiciones hacia abajo en el alfabeto. Por ejemplo, con un desplazamiento de *5*, *a* se reemplazaría por *f*, *b* por *g* y así sucesivamente.

Para implementar este cifrado, necesitarás crear una nueva versión de tu alfabeto que comience en la posición indicada por el desplazamiento. Como aprendiste en una lección anterior, puedes extraer parte de una cadena usando el corte de cadenas (*string slicing*):

```py
# Codigo de ejemplo
fcc = 'freeCodeCamp'
print(fcc[8:]) # Camp
```

Crea una variable llamada *shifted_alphabet* y usa la sintaxis de segmentación para asignarle la porción de *alphabet* que comienza en el índice de *shift*. Luego, llama a la función incorporada *print()* para imprimir *shifted_alphabet* en la terminal y observa el resultado.

## Paso 4

Como puedes ver en la salida, el alfabeto desplazado empieza en la letra *f* porque *shift* tiene el valor 5. Pero ahora las primeras cinco letras del alfabeto *– a, b, c, d y e –* faltan en el alfabeto desplazado, por lo que necesitarás agregarlas al final del alfabeto desplazado.

El operador *+* se utiliza para combinar dos o más cadenas juntas en un proceso llamado concatenación de esta manera:

```py
# Código de ejemplo
greeting = 'Hello' + ' ' + 'World'
print(greeting) # Hello World
```

Modifica la asignación existente de la variable *shifted_alphabet*: usa la sintaxis de *slicing* para extraer la primera porción faltante de *alphabet* y concatenarla a *alphabet[shift:]*.

Como recordatorio, *sentence[start:stop]* devuelve los caracteres de *sentence* desde la posición *start* (incluida) hasta *stop* (excluida).

## Paso 5

Ahora que tienes todo tu alfabeto desplazado, elimina la llamada *print(shifted_alphabet)*.

## Paso 6

El método *str.maketrans()* toma dos cadenas de igual longitud y devuelve una tabla de traducción que asigna cada carácter de la primera cadena con el carácter correspondiente de la segunda cadena. Cada carácter en la tabla de traducción se almacena como un ordinal Unicode, un número que identifica de manera única al carácter.

```py
# Código de ejemplo
lower_chars = 'abc'
upper_chars = 'ABC'

table = str.maketrans(lower_chars, upper_chars)
print(table) # {97: 65, 98: 66, 99: 67}
```

Aprenderás más sobre el tipo de estructura que devuelve *str.maketrans()* más adelante en el plan de estudios. Por ahora, crea una tabla de traducción que asigne los caracteres en *alphabet* a los caracteres en *shifted_alphabet* y asígnala a una variable llamada *translation_table*.

## Paso 7

Declare una nueva variable llamada *text* y asígnale la cadena *'hello world'*. Este será el mensaje para encriptar.

## Paso 8

El método *translate()* toma como argumento la tabla de traducción generada por *str.maketrans()*. Se llama en una cadena y devuelve una copia de la cadena original donde los caracteres han sido reemplazados según la tabla de traducción:

```py
# Código de ejemplo
t = str.maketrans('lk', 'br')
sentence = 'The tent gave in to the leaks.'

print(sentence.translate(t))
# Output: The tent gave in to the bears.
```

Llama al método *translate()* en *text* pasando como argumento *translation_table* y asigna el resultado a una variable llamada *encrypted_text*.

## Paso 9

Ahora imprime *encrypted_text* para ver la salida en el terminal.

## Paso 10

Como puedes ver en la salida, el mensaje ha sido cifrado. El siguiente paso será hacer que tu código sea reutilizable en caso de que quieras cifrar diferentes mensajes.

Para eso, necesitas crear una función. Como recordatorio, aquí está cómo crear una función llamada *spam* que imprime *'Spam!'* en la terminal:

```py
# Código de ejemplo
def spam():
    print('Spam!')
```

Crea una función llamada *caesar*. Coloca todo tu código existente dentro del cuerpo de la función. Presta atención para mantener el mismo nivel de sangría en todas las líneas dentro del cuerpo de la función.

## Paso 11

Como aprendiste en una lección anterior, las funciones pueden tener parámetros, que son variables que pueden ser referenciadas dentro de la función. Aquí tienes una función *sum* con dos parámetros, *num1* y *num2*.

```py
# Codigo de ejemplo
def sum(num1, num2):
    print(num1 + num2)
```

El mensaje para cifrar y el desplazamiento siguen estando codificados de manera fija en tu función. Dale a tu función dos parámetros llamados *text* y *shift*, y elimina las declaraciones de ambas variables, *text* y *shift*, del cuerpo de la función *caesar*.

## Paso 12

Ahora, prueba la función *caesar* llamándola con la cadena *freeCodeCamp* y el número *3* como argumentos. Asignar la llamada de función a una variable llamada *encrypted_text*.

## Paso 13

Ahora tu código es reusable. Sin embargo, la función *caesar* imprime un mensaje en la terminal y devuelve por defecto *None*. Para probarlo, imprime *encrypted_text* al final de tu código.

## Paso 14

En lecciones anteriores, aprendiste que la sentencia *return* se usa para devolver un valor desde una función, para que puedas usarlo en otra parte de tu código:

```py
# Código de ejemplo
def spam():
    return 'Spam!'
```

Elimina la llamada *print(encrypted_text)* de tu función. Luego, borra la declaración de la variable *encrypted_text* y devuelve directamente *text.translate(translation_table)* de tu función.

## Paso 15

Podría haber notado que, aunque el mensaje está cifrado, los caracteres en mayúscula no se han modificado. Esto ocurre porque la tabla de traducción no incluye letras mayúsculas.

Para solucionarlo, necesitarás modificar las cadenas pasadas a su llamada *str.maketrans()* utilizando el método *upper()*:

```py
# Código de ejemplo
greet = "Hello"
print(greet.upper()) # HELLO
```

Actualice su llamada *str.maketrans()* concatenando a cada argumento la versión en mayúsculas del propio argumento.

## Paso 16

Ahora que has implementado las funcionalidades básicas del cifrado, es momento de agregar algo de validación. Para eso, necesitarás una declaración *if*. Aquí hay un recordatorio de la sintaxis para una declaración *if*:

```py
# Código de ejemplo
if condition:
    # code to run when condition is true
```

Al comienzo del cuerpo de tu función, crea una estructura *if*. Por ahora, usa *True* como condición, y dentro del cuerpo de la estructura *if* devuelve la cadena *'Shift must be an integer value'*.

## Paso 17

La función *isinstance()* devuelve *True* si su primer argumento es una instancia del segundo argumento, y *False* en caso contrario:

```py
# Código de ejemplo
print(isinstance('Hello World', str)) # True
print(isinstance(42, int)) # True
```

Reemplace la condición actual de su declaración *if* con una llamada a *isinstance()*. Pase *shift* como el primer argumento, y *int* como el segundo argumento.

## Paso 18

Como recuerdas de lecciones anteriores, el operador lógico unario *not* niega una expresión:

```py
# Código de ejemplo
print(not True) # False
print(not False) # True
```

Utiliza el operador *not* para corregir la condición de la instrucción *if* para que la función devuelva *'Shift must be an integer value.'* cuando *shift* no es un entero.

## Paso 19

No se debe aceptar un desplazamiento negativo o nulo en tu función. Por lo tanto, después de tu primera sentencia *if*, crea otra sentencia *if* que verifique si *shift* es menor que *1* y devuelva la cadena *'Shift must be a positive integer.'*

## Paso 20

Como ya has verificado, el desplazamiento para cifrar el texto debe ser un entero positivo. Sin embargo, no puede exceder 25 (el último índice de alfabeto).

Agrega una segunda condición a la declaración *if* que verifique si *shift* es mayor que *25*. Recuerda que la operación *OR* lógico en Python se implementa a través del operador *or*.

Además, actualiza el mensaje devuelto a *'Shift must be an integer between 1 and 25.'*

## Paso 21

Python te permite especificar un valor por defecto para los parámetros en una función, creando una función que puede ser llamada con menos o ningún argumento. Aquí hay cómo crear una función con un parámetro de *nombre* que tenga un valor por defecto:

```py
# Código de ejemplo
def greet(name='Polly'):
    return 'Hello ' + name
    
print(greet()) # Hello Polly
```

Agrega un tercer parámetro llamado *encrypt* a la función y asígnale un valor por defecto de *True*.

## Paso 22

Vas a utilizar el parámetro agregado en el paso anterior para determinar si la función debe cifrar el texto que se le pasa (comportamiento predeterminado, *encrypt=True*), o si debe descifrar un mensaje cifrado.

Crea una declaración *if* que verifique si *encrypt* no es verdadero. Dentro de la nueva declaración *if*, asigna *shift* a *- shift*. Esto es necesario para que el desplazamiento se realice en la dirección opuesta con respecto al proceso de cifrado.

## Paso 23

Declara dos funciones llamadas *encrypt* y *decrypt*, ambas con parámetros *text* y *shift*.

Usarás *encrypt* para el proceso de encriptación, y *decrypt* para la desencriptación, etiquetando las dos acciones con un nombre descriptivo.

Devuelve una llamada *caesar* pasando *text* y *shift* desde ambas funciones nuevas, pero asegúrate de pasar también *False* como el tercer argumento para la función decrypt.

## Paso 24

Es hora de probar la función *encrypt*. Usando los mismos argumentos, reemplaza tu llamada a *caesar* con una llamada a *encrypt*. Verás el mismo resultado en la terminal.

## Paso 25

Ahora vas a probar la función *decrypt*. Reemplaza el valor asignado a *encrypted_text* con la siguiente cadena, que representa un mensaje para descifrar: *'Pbhentr vf sbhaq va hayvxryl cynprf'*.

Luego, declara una variable llamada *decrypted_text* y asígnale una llamada a *decrypt* con *encrypted_text* como su primer argumento y un desplazamiento de *13* como el segundo argumento.

Finalmente, muestra el *decrypted_text* en la terminal. Con eso, el cifrado César está completo.