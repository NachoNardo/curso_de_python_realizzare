# A Classe é como um model para a criação de objetos
# Nela você terá uma definição de atributos e métodos
# Assim, você pode garantir uma "fábrica" de dados estruturados
# Isto garante um verdadeiro avanço na organização de sistemas
# Sintaxe -> class <nome da classe>:
#               <bloco de código da classe>
# Por convenção uma classe inicia com uma letra maiúscula
# Para gerar um objeto basta você criar uma variável recebendo o nome da classe mais ()

class Carro:
    nome = "fusca"
    ano = 1970
    km = 1000000

veiculo = Carro()

print(veiculo)

# Para acessar os atributos de uma classe, basta chamar o objeto
# E inserir um ponto, mais o nome da variável

print(veiculo.nome)
print(veiculo.km)
print(veiculo.ano)

# Para criar um método, basta usar a criação de uma função
# dentro do bloco de código da classe

class Aluno:
    nome = "Leonardo"
    idade = 32

    def perguntar(self, pergunta):
        print("Professor! " + pergunta + "?")

aluno = Aluno()

aluno.perguntar(input("Insira uma pergunta: "))

# Você pode criar um método construtor para definir os atributos de uma classe em sua criação

class Membro:
    def __init__(self, nome, idade, id):
        self.nome = nome
        self.idade = idade
        self.id = id

membro = Membro("Leonardo", 32, 1)

print(membro.id)
print(membro.idade)
print(1)

# Alguns atributos e métodos podem ser privados
# Assim, eles começam seus nomes com __
# Se eles são privados, só podem ser acessados por dentro da classe

membro.idade = 1000

print(membro.idade)

class Membro:
    def __init__(self, nome, idade, id):
        if (nome != "" and type(nome) != None):
            self.__nome = nome
        else:
            raise AttributeError("Nome não pode ser vazio ou nulo")
        if (idade > 0):
            self.__idade = idade
        else:
            raise AttributeError("Idade não pode ser menor ou igual a zero")
        if (id > 0):
            self.__id = id
        else:
            raise AttributeError("Id não pode ser menor ou igual a zero")

    def set_nome(self, nome):
        if (nome == "" or type(nome) == None):
            self.__nome = nome
        else:
            raise AttributeError("Nome não pode ser vazio ou nulo")

    def get_nome(self):
        return self.__nome

    def set_idade(self, idade):
        if (idade > 0):
              self.__idade = idade
        else:
            raise AttributeError("Idade não pode ser menor ou igual a zero")

    def get_idade(self):
        return self.__idade

    def set_id(self, id):
        if (id > 0):
            self.__id = id
        else:
            raise AttributeError("Id não pode ser menor ou igual a zero")

    def get_id(self):
        return self.__id

membro = Membro("Leonardo", 32, 1)

print(membro.get_id())

membro.set_id(2)

print(membro.get_id())
