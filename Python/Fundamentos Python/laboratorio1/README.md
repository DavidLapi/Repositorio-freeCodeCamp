# Construye un Planificador de Clima para Viajes

Para este laboratorio, usarás sentencias condicionales para determinar si es posible desplazarte según el clima, la distancia a recorrer y la disponibilidad de un vehículo.

**Objetivo:** Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

## Historias de usuario

1. Debes crear las siguientes variables:

- *distance_mi* (un número que representa la distancia a recorrer en millas)

- *is_raining* (un booleano que representa si el usuario está experimentando clima lluvioso actualmente)

- *has_bike* (un booleano que representa si el usuario tiene una bicicleta)

- *has_car* (un booleano que representa si el usuario tiene un coche)

- *has_ride_share_app* (un booleano que representa si el usuario tiene una app que le permite solicitar un viaje)

2. Debes usar sentencias condicionales para determinar si es posible el desplazamiento basado en los valores de estas variables.

3. Debes usar las sentencias *if*, *elif* y *else* para evaluar las categorías de distancia en orden ascendente.

4. Si *distance_mi* es un valor falso:

- Deberías imprimir *False*.

5. Si la distancia es **menor o igual a 1 milla**:

- Debes imprimir True solo si **no está lloviendo**.

- De lo contrario, deberías imprimir *False*.

6. Si la distancia es **mayor que 1 milla y menor o igual a 6 millas**:

- Debes imprimir *True* solo si la persona tiene una bicicleta y no está lloviendo.

- De lo contrario, deberías imprimir *False*.

7. Si la distancia es **mayor a 6 millas**:

- Debes imprimir *True* si la persona tiene un coche o tiene una aplicación de viaje compartido.

- De lo contrario, deberías imprimir *False*.