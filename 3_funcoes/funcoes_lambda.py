# Uma função lambda é uma função com qualquer número de argumentos
# Mas ela só pode ter uma linha de execução
# Ela tem seu valor normalmente atribuído a uma variável
# Sintaxe lambda argumentos: expressão

add = lambda x, y: x + y
print(add(2,2))

# As funções lambdas são comumente utilizadas com o méstodos filter(), map() e sorted()

lista = ["pera", "uva", "banana"]
print(lista)

ordem = lambda fruta: len(fruta)

resultado = sorted(lista, key=ordem)

print(resultado)
