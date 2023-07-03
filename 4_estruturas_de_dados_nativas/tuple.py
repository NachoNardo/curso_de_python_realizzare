# Uma tupla é uma coleção semelhante a uma lista, embora seja imutável
# Ela é definida no momento da sua criação e não pode ser alterada
# Seus itens podem ser de tipos variados e você pode acessar cada um
# Os itens podem ser repetidos
# Sua definição acontece ao criar uma coleção entre parênteses -> ()

tupla = (1, "Leonardo", 10.0)

print(tupla)

print(tupla[0])
print(tupla[1])
print(tupla[2])

# Você pode iterar uma tupla com o método for

for item in tupla:
    print(item)

# Você pode verificar a presença de um item usando if in

if "Leonardo" in tupla:
    print("Existe Leonardo na tupla")

# Você pode verificar o tamanho de uma tupla com o método len()

print(len(tupla))

# Você pode verificar quantas vezes um valor ocorre com o método count()

tupla = (1, 1, 2, 3)

print(tupla.count(1))
print(tupla.count(2))

# E pode verificar a posição de um item com o método index()

print(tupla.index(1))
print(tupla.index(2))
# print(tupla.index(4)) # -> traz um erro
