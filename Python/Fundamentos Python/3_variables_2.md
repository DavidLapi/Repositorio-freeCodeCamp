# Variables y tipos de datos, parte 2

## ¿Cómo funciona la función de impresión?

Cada lenguaje de programación tiene alguna forma de mostrar datos en el terminal con un método incorporado, función, propiedad o palabra clave. En Python, puedes usar la función *print* para imprimir datos en el terminal. Echemos un vistazo más de cerca a la función *print* para que puedas comenzar a usarla con confianza.

Una de las primeras cosas que haces cuando estás aprendiendo cualquier lenguaje de programación es escribir un programa simple de *¡Hola mundo!*. Puedes hacer eso muy fácilmente en Python con solo la función *print*.

Para hacer eso, solo necesitas poner el string **¡Hola mundo!** entre los paréntesis de apertura y cierre que usas para llamar a la función *print*:

```py
print('Hello world!') # Hello world!
```

Aprenderás más sobre cadenas y funciones en Python en lecciones futuras. Por ahora, solo considera las cadenas como una secuencia de caracteres rodeada por comillas simples (*'*) o dobles (*"*).

En el ejemplo **print('Hello world!')**, la cadena *'Hello world!'* es un **argumento** pasado a la función *print*. También puedes usar la función *print* para mostrar múltiples valores, o argumentos, a la vez separándolos con comas. Por ejemplo:

```py
print('My favorite colors are', 'blue', 'green', 'red')

# Output: My favorite colors are blue green red
```

Python agrega automáticamente un espacio entre cada elemento cuando los separas con comas. Esto es útil cuando quieres imprimir varias piezas de información juntas.

## Preguntas

1. ¿Por qué el siguiente código imprime todos los valores en la misma línea con espacios?

```py
print('My favorite colors are', 'blue', 'green', 'red')
```

[X] Porque separar valores con comas en *print()* añade espacios entre ellos.
[] Porque las cadenas se unen automáticamente sin ningún separador.
[] Porque cada llamada a print() agrega un espacio por defecto.
[] Porque Python convierte automáticamente todas las cadenas a mayúsculas en la salida.

2. ¿Cuál sería la salida del siguiente código?

```py
print('Hello', 'world!')
```

[X] Hello world!
[] Helloworld!
[] Hallo, world!
[] Hello\nworld!

3. ¿Cuál es el propósito de las comillas alrededor de *Hello world!* en el siguiente código?

```py
print('Hello world!')
```

[X] Definen una cadena que será impresa por la función *print()*.
[] Se usan para llamar a una función llamada *Hello world!*.
[] Son obligatorios solo si la cadena contiene espacios.
[] Le indican a Python que imprima una variable llamada *Hello world!*.