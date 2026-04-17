def greet():
    pass
    
print(greet()) # None

developer = 'Jessica is developer'

print(developer.upper()) # JESSICA

separate_dev = developer.split()
print(separate_dev)

joined_dev = ' '.join(separate_dev)
print(joined_dev)

print(4 ** 2)

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('JavaScript')