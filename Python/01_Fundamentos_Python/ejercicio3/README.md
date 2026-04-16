# Ejercicio 3: Construye un divisor de facturas

## Paso 1

En este taller, practicarás trabajar con números y operaciones matemáticas para construir un divisor de cuentas. Esta herramienta calculará cuánto debe cada persona después de sumar los costos de la comida y la propina.

Para comenzar, necesitas una forma de llevar un registro del monto total a medida que se agregan los costos. En Python, puedes usar una variable para almacenar un entero (un número entero) que cambia con el tiempo.

Por ejemplo, podrías escribir:

```py
my_number = 2
```

Crea una variable llamada *running_total* y asígnale el valor 0.

## Paso 2

A continuación, necesitas tener en cuenta el número de personas que comparten la cuenta. Guarda este valor en una variable, como hiciste en el paso anterior.

Crea una variable llamada *num_of_friends* y asígnale el valor de *4*. Esto se usará más adelante en el taller para calcular la división final.

## Paso 3

Cada curso tiene un costo. Necesitas almacenar estos montos en variables para usarlos después. Dado que estos montos incluyen centavos, usarás el tipo float, que se usa para representar números decimales. Aquí tienes un ejemplo de una variable con un valor float:

```py
change = 2.35
```

Crea cuatro variables: *appetizers* con valor *37.89*, *main_courses* con valor *57.34*, *desserts* con valor *39.39* y *drinks* con valor *64.21*.

## Paso 4

Ahora que has almacenado los costos individuales, puedes calcular el total. En Python, usas el operador de suma + para sumar valores.

El operador += suma un valor a una variable existente y la actualiza al mismo tiempo. Por ejemplo:

```py
total = 10
total += 2 + 2 + 1
print(total)  # total is now 15
```

Usa el operador += una vez para agregar *appetizers*, *main_courses*, *desserts* y *drinks* a *running_total*.

Finalmente, usa *print()* para mostrar la cadena *'Total bill so far:'* seguida de un espacio y el valor de *running_total*.

**Nota:** Puede que notes que la salida tiene más dígitos decimales de los esperados. Como aprendiste en una lección anterior, esto sucede porque los números se almacenan en binario, y muchos valores decimales no pueden representarse exactamente en este formato, lo que provoca errores de redondeo.

## Paso 5

El servicio fue excelente, así que el grupo decide dejar una propina del 25%. Para calcular un porcentaje en Python, puedes multiplicar el total por el equivalente decimal del porcentaje.

Por ejemplo, para encontrar el 10% de un valor, lo multiplicarías por *0.10* usando el operador *:

```py
tax = total * 0.10
```

Crea una variable llamada *tip* y asígnale el resultado de multiplicar *running_total* por *0.25*.

Finalmente, usa *print()* para mostrar la cadena *'Tip amount:'* seguida de un espacio y el valor de tu variable *tip*.

## Paso 6

Ahora que has calculado la propina, necesitas añadirla a tu *running_total* para encontrar el monto final de la cuenta.

En Python, puedes usar el operador de asignación aumentada *'+='* para sumar un valor a una variable y actualizar esa variable al mismo tiempo. Por ejemplo, *total += 5* es una forma abreviada de escribir *total = total + 5*.

Usa el operador *'+='* para sumar el valor de *tip* a tu *running_total*. Finalmente, usa *print()* para mostrar la cadena *'Total with tip:'* seguida de un espacio y el valor de *running_total*.

## Paso 7

Con la propina ya incluida, tienes el monto final para todo el grupo. Tienes que determinar cuánto debe cada persona dividiendo la cuenta total entre el número de amigos.

En Python, usas la barra diagonal */* para realizar divisiones. Por ejemplo:

```py
half = 10 / 2
```

Crea una variable llamada *final_bill* y asígnale el resultado de dividir *running_total* entre *num_of_friends*.

Finalmente, usa la función *print()* para mostrar la cadena *'Bill per person:'* seguida de un espacio y el valor de *final_bill*.

## Paso 8

La cuenta se divide, pero la división a menudo resulta en números decimales largos. Dado que el dinero generalmente se representa con dos decimales, debes redondear el resultado final.

Python proporciona una *round()* función incorporada para esto. Toma dos argumentos: el número que quieres redondear y la cantidad de decimales que quieres conservar. Aquí tienes un ejemplo:

```py
num = 4.815162342
round(num, 3) # 4.815
```

Usa la función *round()* para redondear *final_bill* a dos decimales y asigna el resultado a una nueva variable llamada *each_pays*.

Finalmente, usa *print()* para mostrar la cadena *'Each person pays:'* seguida de un espacio y tu variable *each_pays*.

Con eso, el taller de división de cuentas está completo.