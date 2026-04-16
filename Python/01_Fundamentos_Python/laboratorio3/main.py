full_dot = '●'
empty_dot = '○'

def create_character(nombre, STR, INT, CAR):

    if not isinstance(nombre, str):
        return "The character name should be a string"
    elif not nombre:
        return "The character should have a name"
    elif len(nombre) > 10:
        return "The character name is too long"
    elif " " in nombre:
        return "The character name should not contain spaces"
    else:
        if (not isinstance(STR, int)) or (not isinstance(INT, int)) or (not isinstance(CAR, int)):
            return "All stats should be integers"
        elif (STR < 1) or (INT < 1) or (CAR < 1):
            return "All stats should be no less than 1"
        elif (STR > 4) or (INT > 4) or (CAR > 4):
            return "All stats should be no more than 4"
        elif (STR+INT+CAR) != 7:
            return "The character should start with 7 points"
        else:
            return f'{nombre}\nSTR {STR*full_dot}{(10-STR)*empty_dot}\nINT {INT*full_dot}{(10-INT)*empty_dot}\nCHA {CAR*full_dot}{(10-CAR)*empty_dot}'

print(create_character("abduscan", 1, 4, 2))