# Uma função é um bloco de código que pode ser executado quando chamado
# Isso economiza a escrita de vários códigos e facilita seu trabalho
# Sintaxe de criação -> def <nome da função>();
#                           <bloco de código>

def saudacao():
    print("Olá")


saudacao()


# Você pode passar parâmetros para que sua função execute taréfas
# com dados que seja fornecidos pelo usuário

nome = input("Diga seu nome: ")


def despedida(nome_usuario):
    print(f"Tchau {nome_usuario}!")


despedida(nome)


# Você também pode retornar valores da sua função
# Assim, é como se ela funcionasse como uma variável

def soma(a, b):
    return a + b


num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))

resultado = soma(num_1, num_2)

print(f"A soma dos dois resultados é {resultado}")

# Você pode definir um valor padrão para caso não seja inserido um parâmetro


def saudacao_2(nome_usuario="pessoa"):
    print(f"Olá {nome_usuario}")


nome = input("Digite um nome: ")

saudacao_2(nome)
