# Dicionários são estruturas de dados que operam com a lógica de chave->valor
# Ou seja, você salva algum dado tendo um valor chave para acessá-lo ao invés de um índice
# Você não tem um salvamento de forma ordenada, mas o encontra pela sua chave
# Esta estrutura é criada entre chaves , mas com cada item sendo uma combinação
# As chaves são obrigatoriamente únicas, enquanto os itens podem ser repetidos
# Seu acesso é extremamente mais rápido do que outras opções
# A sintaxe é <nome> {<chave>:<valor>,<chave2>:<valor2>...<chaven>:<valorn>}

dicionario = {"Leo":"Leonardo", "Tata":"Tamara", "Biel":"Gabriel", "Ma":"Maria"}

# Para acessar um item do dicionário, basta utilizar a mesma notação de item da lista, mas passando a chave

print(dicionario["Leo"])

# Você pode iterar todas as chaves do dicionário utilizando o laço for

for chave in dicionario:
    print(chave)

# Você pode iterar todos os valores combinando o laço for com o método values()

print(dicionario.values())

for valor in dicionario.values():
    print(valor)

# Você pode iterar ambos com o laço for e o método items()

print(dicionario.items())

for chave, valor in dicionario.items():
    print(chave + ":" + valor)

# Você pode adicionar um novo item no dicionário
# Sintaxe -> <dicionario>[<chave>] = <valor>

dicionario["Tutu"] = "Arthur"

print(dicionario)

# Para deletar um item do dicionário você usa o operador del

del dicionario["Biel"]
print(dicionario)

# Você pode verificar se existe uma chave no dicionário com if in

if "Tata" in dicionario:
    print(dicionario["Tata"])
