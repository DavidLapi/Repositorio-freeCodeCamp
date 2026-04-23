# Funcion number_pattern
def number_pattern(n):
    if not isinstance(n, int):
        return f"Argument {n} must be an integer value."
    elif n < 1:
        return f"Argument {n} must be an integer greater than 0."
    else:
        lista = []
        for num in range(1, n+1):
            texto = str(num)
            lista.append(texto)
        string = " ".join(lista)
        return string

print(number_pattern("Cachopo"))
print(number_pattern(-2))
print(number_pattern(4))
print(number_pattern(12))
