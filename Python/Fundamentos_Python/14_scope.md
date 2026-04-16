# Entendiendo Funciones y Ámbito

## ¿Qué es el ámbito (scope) en Python y cómo funciona?

En Python, el ámbito (scope) determina el punto en el que puedes acceder a una variable. Es lo que controla la vida útil de una variable y cómo se resuelve en diferentes partes del código.

Para determinar correctamente el ámbito, Python sigue la regla **LEGB**, que significa lo siguiente:

- **Ámbito local (L)**: Variables definidas en funciones o clases.

- **Ámbito envolvente (E)**: Variables definidas en funciones anidadas o de cierre.

- **Ámbito global (G)**: Variables definidas al nivel superior del módulo o archivo.

- **Ámbito incorporado (B)**: Nombres reservados en Python para funciones, módulos, palabras clave y objetos predefinidos.

Python utiliza la regla LEGB para resolver el ámbito de las variables en tu programa. Nos adentraremos en cada una de estas reglas para darte una mejor comprensión del proceso.

**Ámbito local** significa que una variable declarada dentro de una función o clase solo puede ser accedida dentro de esa función o clase.

Aquí tienes un ejemplo:

```py
def my_func():
    my_var = 10
    print(my_var)
```

En este caso, la función *my_func* tiene su propio ámbito al que no se puede acceder desde fuera de la función. Llamar a *my_func* dará como resultado *10*, pero imprimir *my_var* fuera de la función llevará a una *NameError*:

```py
def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

print(my_var) # NameError: name 'my_var' is not defined
```

**Ámbito envolvente** significa que una función anidada dentro de otra función puede acceder a las variables de la función en la que está anidada.

Por ejemplo:

```py
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!
```

En este ejemplo, la función interna, *inner_func*, puede acceder libremente a la variable *msg* definida en la función externa, *outer_func*. Sin embargo, nota que las funciones externas no pueden acceder a las variables definidas dentro de funciones anidadas:

```py
def outer_func():
    msg = 'Hello there!'
    print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()

outer_func() # NameError: name 'res' is not defined
```

Eso es porque *res* está en ámbito local a *inner_func*. También nota que *outer_func* intenta imprimir *res* antes de que se llame a *inner_func*.

Una solución es inicializar *res* como una cadena vacía en el ámbito envolvente, que está dentro de *outer_func*. Luego, dentro de *inner_func*, convierte *res* en una variable no-local con la palabra clave *nonlocal*:

```py
def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?
```

**Ámbito global** se refiere a variables que se declaran fuera de cualquier función o clase y se pueden acceder desde cualquier parte del programa. Aquí, *my_var* puede ser accedido desde cualquier parte, incluso dentro de una función en la que no está definido:

```py
my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100
```

Y si quieres hacer que una variable local definida dentro de una función sea accesible globalmente, puedes usar la palabra clave *global*:

```py
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10
```

También puedes usar la palabra clave *global* para modificar una variable global:

```py
my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20
```

Finalmente, ámbito incorporado se refiere a todas las funciones incorporadas, módulos y palabras clave de Python, y están disponibles en cualquier parte de tu programa:

```py
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
```

## Preguntas

1. ¿Cuál es la regla que sigue Python para determinar el ámbito de una variable?

- [ ] PILA: Estático, Temporal, Activo, Constante, Palabra clave
- [ ] ÁRBOL: Temporal, Reservado, Encerrar, Externo
- [X] LEGB: Local, Encerrar, Global, Incorporado
- [ ] ÁMBITO: Script, Constante, Externo, Python, Incrustado

2. ¿Qué hace la palabra clave nonlocal?

- [ ] Hace una variable global.
- [ ] Crea una nueva variable local.
- [ ] Previene la reasignación de variables.
- [X] Permite modificar una variable de una función de cierre

3. ¿Qué palabra clave puedes usar para modificar una variable global en Python?

- [X] global
- [ ] local
- [ ] static
- [ ] nonlocal