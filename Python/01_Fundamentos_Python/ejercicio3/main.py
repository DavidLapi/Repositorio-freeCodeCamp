
# Variable running_total (total de factura)
running_total = 0

# Variable num_of_friends (número de amigos)
num_of_friends = 4

# Variables appetizers, main_courses, desserts & drinks (aperitivos, menus principales, postres y bebidas)
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Calcular total de la factura
running_total += appetizers + main_courses + desserts + drinks
print(f"Total bill so far: {running_total}")
# Output: Total bill so far: 198.82999999999998

# Variable tip (propina)
tip = running_total * 0.25
print(f'Tip amount: {tip}')
# Output: Tip amount: 49.707499999999996

# Calculando total más la propina
running_total += tip
print(f'Total with tip: {running_total}')
# Output: Total with tip: 248.53749999999997

# Variable final_bill (Cuenta que pagan los amigos)
final_bill = running_total / num_of_friends
print(f'Bill per person: {final_bill}')
# Output: Bill per person: 62.13437499999999

# Variable each_pays (Cuenta que pagan los amigos redondeando la cifra a dos decimales)
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')
# Output: Each person pays: 62.13