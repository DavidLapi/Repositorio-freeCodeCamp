# Trabajando con Módulos

## ¿Qué es la Biblioteca Estándar de Python y cómo importas un módulo?

En el desarrollo de software, una biblioteca es como una caja de herramientas para desarrolladores.

En lugar de tener que implementar cada parte del código tú mismo desde cero, una biblioteca te ofrece código preescrito y reutilizable, como funciones, clases y estructuras de datos que puedes usar en tus proyectos.

Python tiene una biblioteca estándar extensa con muchos módulos integrados diferentes. Todos son soluciones estandarizadas y bien evaluadas para muchos de los problemas y tareas que enfrentarás diariamente como programador, tales como:

- Interactuando con el sistema operativo.

- Trabajando con archivos.

- Redes.

- Trabajando con fecha y hora.

- Realizando operaciones matemáticas.

- Usando expresiones regulares.

- Probando y depurando tu código.

- ¡Y mucho más!

Algunos ejemplos de módulos integrados populares son **math**, **random**, **re** (abreviatura de "regular expressions") y **datetime**.

El módulo **math** tiene funciones útiles para realizar operaciones matemáticas más complejas.

El módulo **random** es útil para generar números aleatorios.

El módulo **re** se usa para trabajar con expresiones regulares.

Y el módulo **datetime** es útil para trabajar con fechas y horas en Python.

¿Pero cómo puedes acceder a las variables, constantes, funciones y clases definidas en estos módulos integrados?

Usas una sentencia **import**. Estas sentencias te permiten importar módulos en tu script de Python. Las sentencias **import** generalmente se escriben al principio del archivo. Además, puedes personalizarlas según tus necesidades. Primero, usas la sentencia **import**, seguida del nombre del módulo:

```py
import module_name
```

Digamos que quieres importar el módulo **math**. En ese caso, escribirías esto al principio de tu archivo:

```py
import math
```

Luego, si necesitas llamar a una función de ese módulo en tu script de Python, usarías la notación de punto, con el nombre del módulo seguido del nombre de la función:

```py
module_name.function_name() 
```

Por ejemplo, para obtener la raíz cuadrada de 36, escribirías **math** seguido de un punto y luego **sqrt**, una abreviatura de raíz cuadrada, y entre paréntesis, pasarías los argumentos necesarios. En este caso, solo necesitamos pasar el número del cual queremos la raíz cuadrada:

```py
math.sqrt(36) # Output: 6
```

Esta es la versión más básica de una declaración de importación, pero hay otras alternativas.

Si necesitas importar el módulo con un nombre diferente (también conocido como un "alias"), puedes usar esta sintaxis, con **as** seguido del alias al final de la declaración de importación:

```py
import module_name as module_alias
```

Esto se usa a menudo para acortar nombres largos de módulos o para evitar conflictos de nombres.

Por ejemplo, para referirte al módulo **math** como **m** en tu código, puedes asignarle un alias, así:

```py
import math as m 
```

Luego, puedes acceder a los elementos del módulo usando el alias:

```py
m.sqrt(36) # Output: 6
```

Pero a veces no necesitas importar todo de un módulo. Quizás solo necesitas una o dos funciones o clases específicas. Python tiene exactamente lo que necesitas en ese caso.

Ahora la sentencia de importación comienza con **from**, seguida del nombre del módulo, y luego la palabra clave **import** seguida del nombre de los elementos que quieres importar:

```py
from module_name import name1, name2
```

Luego, puedes usar estos nombres sin el prefijo del módulo en tu script de Python.

Si quieres asignar alias a estos nombres, puedes hacerlo usando la palabra clave **as** después de cada uno, seguida del alias que quieres usar:

```py
from module_name import name1 as alias1, name2 as alias2
```

Digamos que solo quieres importar las funciones **radians**, **sine** y **cosine** del módulo **math**. Escribirías:

```py
from math import radians, sin, cos
```

Ahora puedes llamar a estas funciones directamente en tu código, sin el módulo **math** como prefijo.

Aquí tenemos un ejemplo más detallado:

Para encontrar el seno y coseno de un ángulo específico inicialmente expresado en grados, podemos llamar a la función **radians** para convertirlo a radianes, y luego llamar a las funciones de seno y coseno, pasando el ángulo en radianes:

```py
from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978
```

Observa cómo estamos llamando a las funciones directamente, sin el nombre del módulo como prefijo. Esto es porque importamos las funciones con esta sintaxis alternativa.

Esto es útil, pero puede resultar en conflictos de nombres si ya tienes funciones o variables con el mismo nombre definidas en el script de Python. Así que eso es algo a tener en cuenta al elegir qué tipo de declaración de importación quieres usar.

Y finalmente, encontramos esta declaración de importación que termina con un asterisco. El asterisco le está diciendo a Python que quieres importar todo en ese módulo, pero quieres importarlo para que no necesites usar el nombre del módulo como prefijo:

```py
from module_name import *
```

Por ejemplo, si haces esto mientras importas el módulo **math**, podrás llamar a cualquier función definida en ese módulo sin especificar el nombre del módulo como prefijo. Aquí tienes algunos ejemplos:

```py
from math import *
print(sqrt(36))  # 6.0
print(pow(5, 2)) # 25.0
print(exp(1))    # 2.718281828459045
```

Sin embargo, esto generalmente se desaconseja porque puede provocar colisiones de espacio de nombres y dificultar saber de dónde provienen ciertos nombres.

Las declaraciones de importación funcionan exactamente igual para funciones, clases, constantes, variables y cualquier otro elemento definido en el módulo.

Aquí tienes un ejemplo de una constante del módulo **math**, el número **pi**:

```py
import math
print(math.pi) # Output: 3.1416
```

Y aquí tienes un ejemplo de una clase del módulo **datetime**. Creamos un objeto date que representa el 15 de julio de 1959. Luego, asignamos ese objeto **date** a una variable y accedemos al día, mes y año individualmente usando la notación de puntos:

```py
import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # 15
print(birthday.month)  # 7
print(birthday.year)   # 1959
```

Puedes encontrar más información sobre el contenido del módulo en la documentación oficial de Python para ese módulo.

Genial. Ahora que sabes más sobre módulos, también deberías conocer este idioma muy importante en los scripts de Python, porque están muy relacionados:

```py
if __name__ == '__main__': 
    # Code
```

**`__`name`__`** es una variable incorporada especial en Python.

Cuando un archivo Python se ejecuta directamente, Python asigna el valor de esta variable a la cadena **"`__`main`__`"**.

Pero si el archivo Python se importa como un módulo en otro script Python, el valor de la variable **`__`name`__`** se establece con el nombre de ese módulo (usualmente el nombre del archivo sin la extensión .py).

Por eso a menudo encontrarás esta condicional en scripts de Python. Contiene el código que quieres ejecutar solo si el script de Python se está ejecutando como el programa principal:

```py
if __name__ == '__main__': 
    # Code
```

Pero si el script se importa como un módulo, el código dentro de ese bloque no se ejecuta.

Esto es útil porque permite que los scripts de Python tengan dos propósitos. Pueden ejecutarse directamente para llevar a cabo su lógica principal, o pueden importarse en otro módulo sin ejecutar su lógica principal.

## Preguntas

1. ¿Cuál de las siguientes afirmaciones describe mejor la Biblioteca Estándar de Python?

- [X] Es una colección de módulos y paquetes preescritos incluidos con Python.
- [ ] Es una colección de bibliotecas de terceros que necesitan ser instaladas por separado.
- [ ] Es la sintaxis central del lenguaje Python.
- [ ] Consiste en bibliotecas externas escritas en otros lenguajes de programación.

2. ¿Cuál de las siguientes es la sintaxis correcta para importar todo el módulo **datetime** y darle un alias más corto como **dt**?

- [ ] import datetime
- [ ] from datetime import date as dt
- [X] import datetime as dt
- [ ] from datetime import dt

3. Si solo quieres usar la función **mean** del módulo **statistics** directamente en tu código sin anteponer **statistics**, ¿qué declaración de importación usarías?

- [ ] import statistics
- [X] from statistics import mean
- [ ] import mean from statistics
- [ ] from statistics import *
