
# Variables first_name & last_name
first_name = 'John'
last_name = 'Doe'

# Variable full_name
full_name = first_name + ' ' + last_name

# Variable address
address = '123 Main Street'
address += ', Apartment 4B'

# Variable employee_age
employee_age = 28

# Variable employee_info
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

# Variables experience_years & experience_info
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# Variables position & salary
position = 'Data Analyst'
salary = 75000

# Variable employee_card
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# Variable employee_code
employee_code = 'DEV-2026-JD-001'

# Variable department
department = employee_code[0:3]
print(department)

# Variables year_code & initials
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)

# Variable last_three
last_three = employee_code[-3:]
print(last_three)
