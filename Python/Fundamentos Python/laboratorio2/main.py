# funcion apply_discount
def apply_discount(price, discount):
    print(f"El precio es de ${price}")
    print(f"El descuento es de {discount}%")

    if (isinstance(price, (float, int)) == False):
        return "The price should be a number"
    elif (isinstance(discount, (int, float)) == False): 
        return "The discount should be a number"
    elif (price <= 0):
        return "The price should be greater than 0"
    elif (discount < 0 or discount > 100):
        return "The discount should be between 0 and 100"
    else:
        discountPrice = (price * discount)/100
        finalPrice = price - discountPrice
        return finalPrice

print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(30, 100))
print(apply_discount(74.5, 20.0))