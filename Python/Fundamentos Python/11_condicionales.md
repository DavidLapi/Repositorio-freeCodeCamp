# Booleans y Condicionales

## ¿Cómo funcionan las declaraciones condicionales y los operadores lógicos?

Las declaraciones condicionales, o condicionales, te permiten controlar el flujo de tu programa basándote en si ciertas condiciones son verdaderas o falsas.

Pero, antes de entrar en todo eso, repasemos los bloques de construcción básicos de las declaraciones condicionales, comenzando con los operadores de comparación. Los operadores de comparación son operadores que te permiten comparar dos o más valores y devolver un valor booleano.

En una lección anterior, aprendiste que los booleanos son uno de los tipos de datos en Python, y solo pueden ser *True* o *False*.

Aquí hay una tabla con los operadores de comparación en Python:

| **Operator** |    **Name**    | **Description** |
|--------------|----------------|-----------------|
| ==           |      Igual     | Comprueba si dos valores son iguales  |
| !=           |    No Igual    | Comprueba si dos valores no son iguales  |
| >            |   Mayor que    | Comprueba si el valor de la izquierda es mayor que el de la derecha  |
| <            |   Menor que    | Comprueba si el valor de la izquierda es menor que el de la derecha  |
| >=           |   Mayor o igual que    | Comprueba si el valor de la izquierda es mayor o igual que el de la derecha  |
| <=           |   Menor o igual que    | Comprueba si el valor de la izquierda es menor o igual que el de la derecha  |

Aquí algunas de esas expresiones que evalúan a True o False:

```py
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
```

Estos operadores se pueden usar en condicionales para comparar valores y ejecutar cierto código basado en si el condicional evalúa a True o False.

En Python, el condicional más básico es la declaración *if*. Aquí está la sintaxis básica:

```py
if condition:
    pass # Código para ejecutar si la condición es True
```

- Las sentencias *if* comienzan con la palabra clave *if*.

- *condition* es una expresión que se evalúa como True o False, seguida de dos puntos (:).

- El cuerpo de la sentencia *if* constituye un bloque de código, que es un grupo de sentencias que pertenecen juntas. En Python, el nivel de indentación es lo que define un bloque de código.

En el ejemplo anterior, el cuerpo de la sentencia *if* contiene una sentencia *pass*. Cuando se ejecuta una sentencia *pass*, no sucede nada. Esta es una palabra clave especial que puede usarse como marcador de posición para código futuro y es útil cuando no se permiten bloques de código vacíos.

El código dentro del cuerpo de la sentencia *if* se ejecuta solo cuando la condición evalúa a True. Por ejemplo:

```py
age = 18

if age >= 18:
    print('Eres un adulto') # Salida: Eres un adulto
```

Observa la indentación antes de *print('Eres un adulto')*. Mientras que otros lenguajes de programación usan caracteres como llaves para definir bloques de código, y solo usan la indentación para mejorar la legibilidad, en Python, los bloques de código se determinan por la indentación.

El siguiente código generaría un *IndentationError*, que es la forma en que Python indica que se requiere indentación en un punto determinado del código:

```py
age = 18

if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3
```

Aunque puedes usar cualquier número de espacios (siempre que seas consistente) para determinar cada nivel de sangría, la guía de estilo de Python recomienda usar cuatro espacios.

Los bloques también se encuentran en bucles y funciones, que aprenderás en lecciones futuras.

Volviendo a nuestro ejemplo, si *age* es menor que *18*, no se imprime nada en el terminal:

```py
age = 12

if age >= 18:
    print('You are an adult') # Nada se muestra en la terminal
```

Pero, ¿qué pasa si también quieres imprimir algo si edad es menor que 18? Ahí es donde entra la cláusula *else*. La cláusula *else* se ejecuta cuando la condición *if* es falsa (False). Aquí está la sintaxis para una sentencia *if…else*:

```py
if condition:
   pass # Código a ejecutar si la condicion es True
else:
   pass # Código a ejecutar si la condicion es False
```

Por ejemplo:

```py
age = 12

if age >= 18:
    print('Eres un adulto')
else:
    print('No eres un adulto todavía') # Salida: No eres un adulto todavía
```

Ten en cuenta que no puedes colocar ninguna instrucción entre el bloque *if* y la cláusula *else*. El siguiente código generaría un *SyntaxError*:

```py
age = 12

if age >= 18:
    print('Eres un adulto')
print('Ya casi está!')
else: # SyntaxError: invalid syntax
    print('No eres un adulto todavía')
```

Puede haber situaciones en las que quieras tener en cuenta múltiples condiciones. Para hacer eso, Python te permite extender tu declaración si con la palabra clave *elif* (else if).

Aquí está la sintaxis:

```py
if condition1:
   pass # Código a ejecutar si condition1 es True
elif condition2:
   pass # Código a ejecutar si condition1 es False y condition2 es True
else:
   pass # Código a ejecutar si todas las conditions son False
```

Ejemplo:

```py
age = 12

if age >= 18:
    print('Eres un adulto')
elif age >= 13:
    print('Eres un adolescente')
else:
    print('Eres un niño') # Salida: Eres un niño
```

Ten en cuenta que puedes usar tantas declaraciones *elif* como quieras:

```py
age = 2

if age >= 65:
    print('Eres un señor civilizado')
elif age >= 30:
    print('Eres un adulto en su prime')
elif age >= 18:
    print('Eres un adulto joven')
elif age >= 13:
    print('Eres un adolescente')
elif age >= 3:
    print('Eres un niño joven')
else:
    print('Eres un bebé') # Salida: Eres un bebé
```

Ahora que entiendes cómo funcionan los operadores de comparación y las declaraciones condicionales en Python, puedes empezar a escribir programas que tomen decisiones basadas en la lógica y la entrada. Ya sea comparando valores o bifurcándose a través de múltiples condiciones, estas herramientas son la base para escribir código flexible y sensible.

## Preguntas

1. ¿Qué hacen los operadores de comparación?

- [ ] Realizar cálculos matemáticos con valores booleanos
- [ ] Convertir cadenas a valores booleanos
- [X] Comparar dos valores y devolver un valor booleano
- [ ] Crear bucles e iteraciones

2. ¿Cuál será el resultado del siguiente código?

```py
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') 
```

- [ ] *Usted es un adulto* se imprimirá en la consola
- [ ] *Usted es un adolescente* se imprimirá en consola
- [X] *Usted es un niño* se imprimirá en la consola
- [ ] Se imprimirá un error en la consola

3. ¿Qué valor tendrá la expresión *3 >= 4*?

- [ ] True
- [ ] SyntaxError
- [ ] None
- [X] False
