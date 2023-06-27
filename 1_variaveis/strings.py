# String são cadeias de caracteres, que em python são representadas pelo conteúdo entre aspas simples e duplas
# Exemplo

string_exemplo = 'Isto é uma string'
print(string_exemplo)

string_exemplo = "Isto também é uma string"
print(string_exemplo)

# Existem muitos métodos para manipular strings em Python, aqui estão alguns exemplos:

# Lower

var = 'EXempLO'
print(var.lower())

# print(var)
#
# var = var.lower()
# print(var)

# Upper

var = "ExempLo 2"
print(var.upper())

# split

print(var.split(" "))

# Join

var = ['Olá', "Python"]
texto = ' '.join(var)
print(texto)

# Strip

var = '    Olá Python    '
print(var.strip(' '))

# Replace

var = "Olá Leonardo"
print(var.replace('Leonardo', 'Python'))

# Find

var = 'Olá Python'
print(var.find('Python'))
