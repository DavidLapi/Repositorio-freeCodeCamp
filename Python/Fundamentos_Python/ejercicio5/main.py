# Funcion caesar
def caesar(text, shift, encrypt=True):

    # Condicion if si variable shift no es numero entero
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    # Condicion if si variable shift es menor que 1 o mayor que 25
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Variable alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Condicion if si variable encrypt no es verdadero
    if encrypt != True:
        shift = - shift

    # Variable shifted_alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Variable translation_table
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    # Variable encrypted_text
    # encrypted_text = text.translate(translation_table)
    # print(encrypted_text)

    # Devolver texto encriptado
    return text.translate(translation_table)

# Funcion de encriptación 
def encrypt(text, shift):
    return caesar(text, shift)

# Funcion de desencriptacion
def decrypt(text, shift):
    return caesar(text, shift, False)

# Variable shift
shift = 5

# Variable text
text = "hello world"

# Llamada a la funcion caesar
caesar(shift, text)

# Prueba 1
encrypted_text = caesar('freeCodeCamp', 3) # Output: iuhhCrghCdps
print(encrypted_text) # Output: None

# Prueba 2
encrypted_text = encrypt('freeCodeCamp', 3) # Output: iuhhCrghCdps

# Prueba 3
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(encrypted_text) # Output: Pbhentr vf sbhaq va hayvxryl cynprf.
print(decrypted_text) # Output: Courage is found in unlikely places.