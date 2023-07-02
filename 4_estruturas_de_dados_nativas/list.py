# Uma lista em Python é uma estrutura de dados organizada com vários itens em ordem
# Ela é criada ao se atribuir um ou mais valores entre colchetes
# Os valores devem ser separados por vírgulas
# Exemplo

lista = [1, 2, 3, 4, 5]

# Uma lista pode conter mais de um tipo de dado

lista = [1, "a", 1.2, True]

# Você pode acessar os itens de uma lista utilizando o nome da mesma e o índice entre colchetes
# O índice é um número inteiro que inicia a sua contagem com 0
# Exemplo

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4]) #-> ao tentar acessar um índice que não existe você recebe um IndexError

# Você pode descobrir o tamanho de uma lista utilizando a função len()
# Lembrando que aqui a contagem começa com o 1

print(len(lista))

# Para percorrer todos os itens de uma lista, o melhor jeito é utilizar o método for

for item in lista:
    print(item)

# Para adicionar um novo item à lista em uma posição específica você pode utilizar o método insert

lista.insert(0, "5")

print(len(lista))
print(lista)

# Para adicionar um novo item ao final da lista você pode utilizar o método append

lista.append(3)

print(len(lista))
print(lista)

# Você pode remover um item da lista informando seu valor para o método remove

lista.remove("a")

print(len(lista))
print(lista)

# Você pode remover um item da lista em determinado índice com o método pop
# Se você não informar um índice, o último item será eliminado

lista.pop(1)

print(len(lista))
print(lista)

# Você pode verificar se um item está na lista através de um if com a palavra in

if '5' in lista:
    print("5 está na lista")

# Você pode ordenar uma lista automaticamente com o método sort

lista = [5, 4, 3, 1, 2]

lista.sort()

print(lista)

# Você pode inverter a ordem de uma lista com o método reverse

lista.reverse()

print(lista)
