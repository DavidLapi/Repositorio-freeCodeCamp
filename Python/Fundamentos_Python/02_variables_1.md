# Variables y tipos de datos, parte 1

## ¿Cómo declaras variables y cuáles son las convenciones de nomenclatura para nombrar variables?

En Python, las variables son como una caja etiquetada para almacenar y referenciar datos de diferentes tipos. Para declarar variables en Python, asignas un valor a un identificador con el operador de asignación (=). No necesitas usar palabras clave especiales como *let* o *const* en JavaScript, o *char* en C#.

En Python, simplemente escribes el nombre de la variable a la izquierda, seguido del operador de asignación, y el valor que deseas asignar a la variable a la derecha. Aquí hay un ejemplo de cómo declarar las variables *nombre* y *edad*:

```py
nombre = "David"
edad = 23
```

En el ejemplo anterior, la variable *nombre* contiene el valor 'David'. Este valor es una cadena, que es una serie de caracteres usados para representar texto. Las cadenas se escriben con comillas simples o dobles, por ejemplo 'Hello' o "Hello". En lecciones futuras, aprenderás más sobre cómo trabajar con cadenas en Python.

Al nombrar variables en Python, hay algunas reglas importantes que debes tener en cuenta:

- Los nombres de las variables sólo pueden comenzar con una letra o un guión bajo (_), no un número.

- Los nombres de las variables sólo pueden contener caracteres alfanuméricos (a-z, A-Z, 0-9) y guiones bajos (_).

- Los nombres de las variables son sensibles a mayúsculas — *edad*, *Edad*, y *EDAD* se consideran únicos.

- Los nombres de las variables no pueden ser una de las palabras reservadas de Python como *if*, *class*, o *def*.

Si rompes alguna de esas reglas, tu programa de Python lanzará un **SyntaxError**:

```py
5variable_name = 5
^
SyntaxError: invalid syntax
```

Ahora repasemos algunas convenciones comunes de nomenclatura para variables en Python.

Primero, los nombres de las variables deben estar en minúsculas, con palabras separadas por un guión bajo. Esto se llama *snake case*:

```py
my_variable_name = "David freeCode"
```

A continuación, debes usar nombres descriptivos para las variables. Por ejemplo, si deseas guardar la edad de un usuario como variable, *edad_usuario* es mejor que *edad* o una abreviatura como *eu*:

```py
user_age = 30
```

De esta manera, puedes comunicar fácilmente el propósito de una variable a otros miembros del equipo (o a tu futuro yo) en una gran base de código.

Otra convención es evitar usar nombres de variables de una sola letra. Esto es muy común en Python, pero se debe evitar porque los nombres de variables de una sola letra no comunican propósito o significado:

```py
x = 56 # What do you mean by x?
```

Esto es diferente si estás en un bucle o algo similar, ya que los nombres de variables como *i*, *j*, *k+, etc., son comunes y aceptables.

Además, el símbolo de libra (#) y el texto que sigue en el ejemplo anterior se llama comentario. Ya podrías estar familiarizado con los comentarios, así que revisémoslos rápidamente y expliquemos cómo funcionan.

En Python, los comentarios empiezan con un símbolo de libra (#), y el lenguaje ignora todo lo que siga después del símbolo *#* en esa línea:

```py
# Esta es mi línea
```

Los comentarios de varias líneas se pueden crear usando comentarios de una sola línea consecutivos:

```py
# Estas son
# mis mejores
# líneas.
```

Puedes usar comentarios para explicar tu código, dejar recordatorios para ti mismo, o aclarar por qué existe una línea. Los comentarios son especialmente útiles cuando estás aprendiendo o trabajando en equipos.

Sin embargo, no debes usar comentarios para explicar lo que significan tus nombres de variables. En su lugar, los nombres que elijas para tus variables deben ser descriptivos y comunicar para qué son, y seguir las otras reglas de nomenclatura mencionadas anteriormente para evitar errores de sintaxis.

## Preguntas

1. ¿Cuál de las siguientes es la forma correcta de declarar una variable en Python?

- [ ] let age = 25
- [ ] const age = 25
- [ ] var age = 25
- [X] age = 25

2. ¿Cuál de estas no es una regla para nombrar variables?

- [ ] Los nombres de las variables deben comenzar con una letra o un guión bajo.
- [X] Los nombres de las variables no son sensibles a mayúsculas.
- [ ] Los nombres de las variables no pueden usar las palabras clave reservadas de Python.
- [ ] Los nombres de variables pueden contener letras, números y guiones bajos.

3. ¿Por qué deberías evitar usar nombres de variables de una sola letra?

- [X] No comunican el propósito de la variable.
- [ ] Python no permite nombres de variables de una sola letra.
- [ ] Aumentan el riesgo de errores de sintaxis.
- [ ] Usan más memoria que los nombres de variables más largos.

--------------------------------------------------------------------------------

Función de impresión --> [**Click aquí**](./funcion_impresion.md)