# Um loop for é feito para automatizar a iteração de um elemento iterável
# Ele não possui condição, mas pede um elemento iterável e usa um índice
# Ele termina naturalmente quando o iterador tem todos os itens lidos
# Sintaxe -> for <índice> in <iterador>:
#               <bloco de código>

lista = ["leonardo", "tamara", "maria", "gabriel"]

for x in lista:
    print(f"Aluno(a) {x} presente")

# Você pode interromper um loop com a palavra break

for x in lista:
    print(x)
    if x == "tamara":
        break

# Você pode pular uma iteração com a palavra continue

for x in lista:
    if x == "gabriel":
        continue
    print(x)

# Você pode utilizar a palavra else para executar um bloco de código
# quando a iteração acabar

for x in lista:
    print(x)
else:
    print("Todos os alunos foram listados")
    
