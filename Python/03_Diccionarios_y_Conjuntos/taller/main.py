# Variable medical_records
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

# Variable helloWorld
helloWorld = "Hello World!"

# Variable medical_records2
medical_records2 = [
    {
        'patient_id': 'P1011',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1012',
        # 'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1013',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1014',
        'age': 56,
        'gender': 'Male',
        # 'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

# Funcion find_invalid_records
def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {}
    return constraints

# Funcion validate
def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    
    is_invalid = False

    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    # Bucle for
    for index, dictionary in enumerate(data):
        # Primer if en bucle for
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

        # Segundo if en bucle for
        if set(dictionary.keys()) != key_set:
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            is_invalid = True

    # If si es invalido
    if is_invalid == True:
        return False
    
    print("Valid format.")
    return True


# Pruebas
print("Validar medical_records:")
validate(medical_records)
print("\nValidar helloWorld:")
validate(helloWorld)
print("\nValidar medical_records2:")
validate(medical_records2)