# Variable precio entrada cine
base_price = 15

# Variable edad
age = 21

# Variable tipo asiento
seat_type = "Gold"

# Variable hora película
show_time = "Evening"

# Condicional if si age es mayor que 17
if age > 17:
    print("User is eligible to book a ticket")

# Condicional if si age es mayor o igual a 21 
if age >= 21:
    print("User is eligible for Evening shows")
else:
    print('User is not eligible for Evening shows')

# Variable es miembro
is_member = False

# Variable fin de semana
is_weekend = False

# Variable descuento
discount = 0

# Condicional if si es miembro tiene descuento; y si no es miembro, no tiene descuento
if is_member and age>=21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

# Imprime descuento
print('Discount:', discount)

# Variable cargos adicionales
extra_charges = 0

# Condicional if si es fin de semana verdadero o si es por la tarde
if is_weekend or show_time=='Evening':
    extra_charges = 2
    print("Extra charges will be applied")
else:
    print('No extra charges will be applied')

# Imprime cargos adicionales
print("Extra charges:", extra_charges)

# Condicion if si la edad de la persona es mayor o igual a 18 o 21, y que la hora no sea Evening O que sea miembro del cine
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print("Ticket booking condition satisfied")
    # Variable cargos servicio
    service_charges = 0
    # Sentencia if anidada si el tipo de asiento es Premium, Gold o normal
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    # Variable precio final calculando precio base sumando los cargos adicionales y restando el descuento
    final_price = base_price + extra_charges + service_charges - discount
    print('Final price of ticket:', final_price)
else:
    print("Ticket booking failed due to restrictions")

