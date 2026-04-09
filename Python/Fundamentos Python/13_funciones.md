# Entendiendo Funciones y Ámbito

## ¿Cómo funcionan las funciones en Python?

Las funciones son piezas reutilizables de código que se ejecutan cuando las llamas. Muchos lenguajes de programación incluyen funciones integradas que facilitan comenzar. Python no es excepción, y ya hemos cubierto algunas funciones construidas como *print()* en anteriores lecciones.

Otra función integrada útil es *input()*, que te permite pedir la entrada del usuario:

```py
name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade
```

Por otro lado, *int()* convierte un número, booleano y una cadena numérica en un entero:

```py
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 
```

También puedes escribir tus propias funciones personalizadas. Para hacerlo, usa la palabra clave *def*, seguida del nombre que deseas darle a tu función, un par de paréntesis y dos puntos. Luego, en una nueva línea, escribe el código que tu función debería ejecutar. El código que ejecuta la función también se conoce como el cuerpo de la función.

Aquí está un ejemplo de una función personalizada llamada *hello* que imprime la cadena *'Hello World'* en el terminal:

```py
def hello():
    print('Hello World')
```

Para ejecutar la función, debes llamarla con su nombre seguido de un par de paréntesis:

```py
hello() # Hello World
```

Observa la indentación antes de *print('Hello World')*. Como recordarás de lecciones anteriores, Python depende de la indentación para determinar qué grupos de sentencias pertenecen juntos. Estos grupos de sentencias se llaman bloques de código.

Aquí hay otra función simple que imprime la suma de dos números en el terminal:

```py
def calculate_sum(a, b):
    print(a + b)
```

Puedes ver que nuestra función, *calculate_sum*, tiene *a* y *b* en sus paréntesis, separados por una coma. Esos se llaman parámetros. Piensa en los parámetros como variables de marcador de posición que actúan como "espacios" para los valores que pasas a las funciones cuando las llamas.

Para usar los parámetros, tienes que pasar "argumentos". Los argumentos son los valores que pasas a una función cuando la llamas.

Aquí está cómo llamar a la función *calculate_sum* para sumar juntos los números *3* y *1*:

```py
calculate_sum(3, 1) # 4
```

Si llamas a la función sin el número correcto de argumentos, obtendrás un TypeError:

```py
calculate_sum()

# TypeError: calculate_sum() missing 2 required positional arguments: 'a' 
```

Las funciones también usan una palabra clave especial *return* para salir de la función y devolver un valor. Si no usas explícitamente *return*, Python devolverá *None* por defecto.

Aquí tienes un ejemplo:

```py
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None
```

Puedes ver que la función *calculate_sum* imprime la suma de *a* y *b*, pero no devuelve nada explícitamente. Así que cuando asignamos su resultado a *my_sum*, el valor es en realidad *None*. Para solucionar eso, puedes usar la palabra clave *return* para enviar de vuelta el resultado:

```py
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4
```

Ahora, *calculate_sum* devuelve la suma de *a* y *b*, que se almacena en *my_sum*.

## Preguntas

1. ¿Cuál es el valor de retorno predeterminado de una función en Python?

- [ ] 0
- [X] None
- [ ] "" (cadena vacía)
- [ ] False

2. ¿Cuál es el término para una variable de marcador de posición en una función?

- [X] Parámetro
- [ ] Argumento
- [ ] Valor de retorno
- [ ] Decorador

3. ¿Qué palabra clave se usa para definir una función personalizada en Python?

- [ ] function
- [X] def
- [ ] func
- [ ] define