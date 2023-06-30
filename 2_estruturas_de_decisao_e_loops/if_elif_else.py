# If é uma operação condicional, onde se a condição for verdadeira,
# o programa passa a executar o bloco de código que acontece em seguida
# Sintaxe -> if <condição>:
#               <bloco de código>
# Em Python, blocos de código são separados por uma iniciação com um tab

if True:
    print("Condição verdadeira, irá escrever esta linha")

if False:
    print("Condição falsa, não irá escrever esta linha")

##################################################################################

# Podemos utilizar comparações e operadores lógicos para gerar as condicionais

x = 10

if x < 20:
    print("x é menor do que 20")

if x > 2:
    print("x é maior do que 2")

if x < 5:
    print("x é menor do que 5")

if x < 30 and x > 7:
    print("x é maior que 7 e menor que 30")

if x > 2 or x < 5:
    print("x é maior que 2 ou menor que 5")

if x == 10:
    print("x é igual a 10")

if x != 20:
    print("x é diferente de 20")

if x <= 30:
    print("x é menor ou igual a 30")

if x >= 3:
    print("x é maior ou igual a 3")

######################################################################################
# A palavra else é utilizada quando você quer executar um bloco de código
# caso as condições anteriores não tenham sido atendidas
# entretanto, ele mesmo não terá uma uma condição por si só
# Sintaxe -> else:
#               <bloco de código>

nome = input("Digite seu nome: ")

if nome == "leonardo":
    print("Seu nome é Leonardo")
else:
    print(f"Seu nome não é Leonardo, seu nome é {nome}")

###########################################################################################
# Por último temos o elif, que executa um bloco de código caso sua condição seja verdadeira
# e as anteriores não forem.
# Sintaxe -> elif <condição>:
#               <bloco de código>

numero = int(input("Digite um número: "))

if numero > 5:
    print("O número é maior do que 5")
elif numero > 2:
    print("O número é maior do que 2")
else:
    print("O número é menor do que 2")
