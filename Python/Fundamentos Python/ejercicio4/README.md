# Ejercicio 4: Construye un calculador para reservar entradas de cine

## Paso 1

En este taller, practicarás cómo usar booleanos y declaraciones condicionales en Python construyendo un calculador de reservas de entradas de cine.

Comienza declarando variables que almacenan información sobre el usuario y la función de la película.

Como aprendiste en lecciones anteriores, las variables se asignan usando el operador de asignación (=) de esta manera:

```py
# Assigns the value 10 to variable x
x = 10
```

Crea una variable llamada *base_price* para almacenar el precio base del boleto de cine y asigna su valor a *15*. Crea otra variable llamada *age* para almacenar la edad del usuario y asigna su valor a *21*.

## Paso 2

Ahora necesitas almacenar algunos valores de cadena sobre el boleto de la película. Puedes almacenar cadenas en Python de esta manera:

```py
name = 'Alice'
```

Crea una variable llamada *seat_type* para almacenar el tipo de asiento que el usuario ha seleccionado y asigna su valor a la cadena *Gold*. Crea otra variable llamada *show_time* para almacenar la hora de la función de la película y asigna su valor a la cadena *Evening*.

Recuerda rodear ambos valores con comillas simples o dobles.

## Paso 3

Como aprendiste en lecciones anteriores, en Python, una sentencia *if* puede usarse para ejecutar código dependiendo de si una condición es verdadera.

Una sentencia *if* consiste en la palabra clave *if*, seguida de una condición y dos puntos. El código que se ejecuta cuando la condición es verdadera, que debe estar indentado, se llama el cuerpo de la sentencia *if*.

```py
if condition:
    # Code to execute if condition is True
```

En este paso, verificarás si el usuario es elegible para reservar un boleto de cine según su edad.

Crea una sentencia *if* para verificar si *age* es mayor que *17*. Dentro del cuerpo de la sentencia *if*, imprime *'User is eligible to book a ticket.'* Esto imprimirá el mensaje solo cuando la edad del usuario sea mayor que *17*.

Recuerda indentar el cuerpo de la sentencia *if* y rodear el mensaje con comillas simples o dobles dentro de la llamada *print()*.

## Paso 4

Ahora verificarás si el usuario tiene permitido reservar un espectáculo nocturno según su edad.

Crea una estructura *if* para verificar si age es mayor o igual a *21*. Dentro del cuerpo de la estructura *if*, imprime *'User is eligible for Evening shows'*.

## Paso 5

En el paso anterior, verificaste una condición usando una sentencia *if*. La cláusula *else* se usa para manejar el caso cuando la condición es falsa. Aquí está la sintaxis de una sentencia *if...else*:

```py
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

Ahora, agrega una cláusula *else* a tu declaración *if* e imprime *'User is not eligible for Evening shows'* dentro del cuerpo de *else*. Esto se imprimirá solo cuando la condición en la declaración *if* sea falsa.

## Paso 6

Algunas informaciones solo pueden ser verdaderas o falsas. Como has aprendido en lecciones anteriores, esto puede representarse usando valores booleanos.

Crea una variable llamada *is_member* para indicar si el usuario es miembro y asigna su valor a *True*.

Debajo de la variable *is_member* crea otra variable llamada *is_weekend* para indicar si la función de la película es en un fin de semana y asigna su valor a *False*. No pongas el valor entre comillas.

## Paso 7

El usuario califica para un descuento de membresía si es miembro.

Crea una variable llamada *discount* y asigna su valor a *0*. Esto almacenará el descuento que el usuario obtiene en el boleto de cine.

## Paso 8

En Python, las condiciones *if* no tienen que comparar valores explícitamente con *True* o *False*. En cambio, se basan en la veracidad de los valores. Los valores verdaderos evalúan a *True* en un contexto booleano, como la condición de una sentencia *if*. Estos incluyen números distintos de cero, cadenas no vacías y el valor booleano True.

```py
if value:
   print('value is truthy')
```

Crea una sentencia *if* para verificar si *is_member* es verdadero. Dentro del cuerpo de la sentencia *if*, actualiza el valor de *discount* a *3* e imprime *User qualifies for membership discount* en el terminal.

## Paso 9

También debes manejar el caso cuando el usuario no califique para un descuento de membresía.

Agrega una cláusula *else* a tu declaración *if* e imprime *User does not qualify for membership discount* dentro del cuerpo de *else*.

Puedes imprimir un mensaje seguido de una variable así:

```py
print('Total:', total)
```

También quieres mostrar el valor actualizado de *discount*. Debajo de la sentencia *if...else*, usa la llamada *print()* para mostrar un mensaje que muestre *Discount:* seguido del valor actualizado de *discount*. Luego, verifica la salida en la terminal.

## Paso 10

En Python, el operador *and* se usa para verificar si múltiples condiciones son verdaderas. Aquí tienes cómo puedes usarlo para combinar dos condiciones en una sentencia if:

```py
if condition1 and condition2:
    # Code to execute if all conditions are True
```

El descuento por membresía solo debe aplicarse a los miembros si su *age* es mayor o igual a 21.

Actualiza la condición de la línea *if is_member:* usando el operador *and* para combinar la condición existente con otra condición que verifica si *age* es mayor o igual a 21.

## Paso 11

Ahora cambia el valor de la variable *is_member* a *False* ya que el usuario no es miembro.

Después de eso, verás que el valor de *discount* ahora permanece en 0, porque ambas condiciones deben cumplirse para que se aplique el descuento.

## Paso 12

Ahora crea una variable llamada *extra_charges* y asígnale el valor 0. Esto representará cargos adicionales para aplicar al boleto de cine los fines de semana.

Luego, crea una estructura *if* para verificar si *is_weekend* es verdadero. Dentro del cuerpo de la estructura if, actualiza el valor de *extra_charges* a 2 e imprime *Extra charges will be applied* en la terminal.

## Paso 13

Ahora, agrega una cláusula *else* a tu sentencia *if* e imprime *No extra charges will be applied* dentro del cuerpo de *else*. Esto imprimirá el mensaje solo cuando la condición de cargos extra sea falsa.

Luego, debajo de la cláusula *else*, usa la llamada *print()* para mostrar un mensaje que muestre *Extra charges:* seguido del valor actualizado de *extra_charges* y verifica la salida en el terminal.

## Paso 14

En Python, el operador *or* se usa para verificar si al menos una de dos condiciones es verdadera. Así es como puedes usarlo en una sentencia *if*:

```py
if condition1 or condition2:
    # Code to execute if any condition is True
```

También deben aplicarse cargos adicionales si el espectáculo es por la noche. Actualiza la condición de la línea *if is_weekend:* usando el operador *or* para combinar la condición existente con una segunda condición que verifique si *show_time* es igual a la cadena *Evening*.

## Paso 15

Ahora verificarás si el usuario cumple con las condiciones para reservar un boleto de cine. Los usuarios con edad *21* o más siempre pueden reservar boletos sin ninguna restricción.

Crea una estructura *if* para verificar si *age* es mayor o igual a *21*. Dentro del cuerpo de la estructura *if*, imprime *Ticket booking condition satisfied* en el terminal.

Luego, agrega una cláusula *else* a tu declaración *if* e imprime *Ticket booking failed due to restrictions* dentro del cuerpo de *else*.

## Paso 16

Los usuarios entre 18 y 21 pueden reservar entradas, pero solo cuando el *show_time* no sea *Evening*.

Actualiza la condición de la línea *if age >= 21:*. Usa el operador *and* para construir una expresión que verifique si *age* es mayor o igual a *18* y *show_time* no es *Evening*. Luego usa el operador *or* para combinar esa expresión con la condición existente. No crees nuevas variables.

## Paso 17

Hay una excepción más a las reglas de reserva. Los usuarios entre 18 y 21 pueden reservar funciones nocturnas si son miembros.

Cuando se usan múltiples operadores lógicos en una sentencia *if*, las condiciones unidas con *and* se evalúan antes que las condiciones unidas con *or*. Los paréntesis () se usan en Python para agrupar condiciones y controlar el orden en que se evalúan.

```py
if condition1 and (condition2 or condition3):
    # Code to execute if conditions evaluate to True
else:
    # Code to execute if conditions evaluate to False
```

Actualiza la condición de la línea *if age >= 21 or age >= 18 and show_time != 'Evening':* para agregar otra condición usando el operador *or* para verificar si *is_member* es verdadero. Usa paréntesis () para agrupar las condiciones *show_time != 'Evening'* e *is_member* juntas como se muestra en el ejemplo anterior.

## Paso 18

En Python, una sentencia *if* también puede colocarse dentro del cuerpo de otra sentencia *if*. Esto se llama una **sentencia if anidada**.

Una estructura *if* anidada te permite verificar una condición adicional solo después de que la primera condición ya se haya cumplido. La estructura *if* interna se ejecutará solo si la condición del *if* externo es verdadera.

```py
if condition1:
    # Code to execute if condition1 is True
    if condition2:
        # Code to execute if both conditions are True
```

Ahora calcularás los cargos por servicio según el tipo de asiento que el usuario haya seleccionado.

Dentro del cuerpo de la última sentencia *if*, debajo de la línea *print('Ticket booking condition satisfied')*, crea una variable llamada *service_charges* y asígnale el valor *0*. Asegúrate de indentar tu código con cuatro espacios para mantenerlo dentro del cuerpo externo de la sentencia *if*.

Luego, crea una estructura *if* anidada para verificar si *seat_type* es igual a *Premium*. Dentro del cuerpo de la estructura *if* anidada, actualiza el valor de *service_charges* a *5*.

## Paso 19

Todavía dentro del cuerpo de la declaración externa *if*, agrega una cláusula *else* a la declaración anidada *if seat_type == 'Premium':* y actualiza el valor de *service_charges* a *1* dentro del cuerpo del *else*. Asegúrate de mantener el *else* indentado con cuatro espacios para permanecer dentro del cuerpo de la declaración externa *if*.

## Paso 20

La sentencia *if...elif...else* se usa para verificar múltiples condiciones en orden.

```py
if condition1:
   # Code to execute if condition1 is True
elif condition2:
   # Code to execute if condition1 is False and condition2 is True
else:
   # Code to execute if all conditions are False
```

Todavía dentro del cuerpo de la declaración externa *if*, agrega una cláusula *elif* entre las líneas *if seat_type == 'Premium':* y *else:* y verifica si *seat_type* es igual a *Gold*. Dentro del cuerpo de la cláusula *elif*, actualiza el valor de *service_charges* a *3*.

Debajo de la estructura anidada *if...elif...else*, usa la llamada *print()* para mostrar un mensaje que indique *Service charges:* seguido del valor actualizado de *service_charges*. Luego, verifica la salida en el terminal.

## Paso 21

En este paso final, calcularás el precio final del boleto de cine usando los valores calculados en los pasos anteriores.

El precio final del boleto se calcula sumando los cargos adicionales y los cargos por servicio al precio base, y luego restando el descuento.

Dentro del cuerpo de la última sentencia *if*, debajo de la línea *print('Service charges:', service_charges)*, calcula el precio final del boleto y guárdalo en una variable llamada *final_price*.

Finalmente, imprime un mensaje que muestre *Final price of ticket:* seguido del valor de *final_price*.