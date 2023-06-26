#Um programa em Python pode ler vários tipos de entradas de periféricos
#Entretanto, o padrão a ser utilizado é o teclado,
#E você só precisa utilizar o método input
#A sintaxe é: variavel = input('mensagem a ser impressa: ')
#O computador então irá ler o que o foi escrito no teclado
#E então irá salvar esta entrada com o tipo str na variável
#Exemplo:

variavel = input("Digite a sua idade: ")
print("Sua idade é: " + variavel + " anos.")

#Entretanto, você pode estar desejando receber um número inteiro ou fracionário
#Neste caso, usamos o casting, que é uma expressão entre parênteses que tenta
#Mudar o tipo da variável quando possível, e retorna um erro quando impossível

variavel = (int) (input("Digite um número inteiro: "))
variavel = variavel + 2
print("O número digitado acrescido de 2 é: " + (str) (variavel))

#Você pode fazer o cast de um tipo para qualquer outro
#Mas o único que trás mais dificuldades é o bool
#Qualquer valor como 0 ou vazio vira falso enquanto qualquer outra vira verdadeiro

v = []
print("" + str(bool(v)))

v = 1
print("" + str(bool(v)))
