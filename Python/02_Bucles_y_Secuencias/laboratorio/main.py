# Funcion number_pattern
def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    else:
        lista = []
        for num in range(1, n+1):
            cadena = str(num)
            lista.append(cadena)
        string = " ".join(lista)
        return string

print(number_pattern(4))
print(number_pattern(12))