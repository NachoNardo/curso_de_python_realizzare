#Variáveis devem começar sempre com letras, de preferência com letras minúsculas
#Em programação é comum considerar varíaveis que começam com letras maiúsculas como Classes
#E todas as letras maiúsculas significam uma constante

variavel = 10 #O que acontece aqui é que a variável está recebendo o valor 10, do tipo int
              #A atribuição acontece da direita para a esquerda

variavel = 'string' #Agora esta variável tem um valor do tipo str que é a palavra string

#Variáveis não podem ter espaços entre as palavras se elas tiverem um nome composto
#Ao invés disso, utilize o char '_' para indicar a separação
#Elas podem conter um número, desde que não seja inicial
#Elas não podem conter caracteres acentuados ou pontuação e caracteres especiais
#Exemplos:

#1melhor = 10
#pio$r = 5
#exceção = 7
#variável = 1

#########################################################################################

#Tipos de variáveis
#Variáveis possuem diferentes tipos, e eles podem ser verificados pela função type(<varipável>)
#Exemplos:

variavel = 10
print(type(variavel)) #int

variavel = 'string'
print(type(variavel)) #str

variavel = False
print(type(variavel)) #bool

variavel = 10.5
print(type(variavel)) #float

variavel = None
print(type(variavel)) #None

############################################################################################
