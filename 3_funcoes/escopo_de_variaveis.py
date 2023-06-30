# Escopo de variáveis basicamente significa o alcance e domínio
# Que uma variável tem dentro de um código
# Existe o escopo global e o escopo local

var = "global" # Esta variável tem escopo global dentro do código,
               # pode ser referida em qualquer local

print(var)

def var_global():
    print(var)

var_global()

# Uma variável local irá atuar somente em um bloco de código
# ou em blocos de códigos derivados

def var_local():
    x = 1
    print(x)

var_local()

# print(x) # -> Trará um erro

# Quando a variável tiver um nome igual, ela ela irá respeitar seu escopo

varg = "Global"

def global_local():
    varg = 1
    print(varg)

global_local()

print(varg)

# Eu posso usar a palavra global para dizer que estou trabalhando com a variável global

def global_global():
    global varg
    varg = "Local"
    print(varg)

global_global()

print(varg)
