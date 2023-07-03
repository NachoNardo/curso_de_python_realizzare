# Um set em Python é um conjunto de itens únicos
# Para se criar um set é possível simplesmente adicionar valores entre chaves {}
# Ou então utilizar a função set()
# Se algum dos elementos for repetido, ele será inserido uma só vez no set
# Exemplos:

conjunto = {1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10}
print(conjunto)

print(set(['a', 'b', 'c']))

# Para ler todos os valores de um set em um script é possível utilizar o laço for

for item in conjunto:
    print(item)

# Você pode adicionar um valor no set com a função add()

conjunto.add(11)

print(conjunto)

# Você pode remover um item do conjunto passando seu valor para o método remove()
# Se o item não existir ocorrerá um erro

conjunto.remove(1)

print(conjunto)

# Você pode remover um item do conjunto passando seu valor para o método discard()

conjunto.discard(99)

print(conjunto)

# Podemos utilizar operações de conjuntos com os sets
# Exemplo: união

conjunto2 = {'a', 'b', 'c', 'd', 'e'}

print(conjunto | conjunto2)

# Ou

print(conjunto.union(conjunto2))

# Interseção

conjunto2 = {1, 2, 3, 4, 35, 99}

print(conjunto & conjunto2)

print(conjunto.intersection(conjunto2))

# Diferença

print(conjunto - conjunto2)

print(conjunto.difference(conjunto2))

# Diferença simétrica

print(conjunto ^ conjunto2)

print(conjunto.symmetric_difference(conjunto2))
