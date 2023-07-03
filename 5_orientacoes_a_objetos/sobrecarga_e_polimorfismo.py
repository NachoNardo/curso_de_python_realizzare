# O Python não ceita sobrecarga de métodos, mas aceita o conceito de polimorfismo
# O conceito de polimorfismo é dar mais de uma forma para um mesmo método
# Exemplo:

class Animal:
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return "Au! Au!"

pet = Cachorro()

print(pet.som())

# Podemos também utilizar métodos com diferentes parâmetros

class Calculadora:
    def adicao(self, a, b):
        return a + b

calculadora = Calculadora()

print(calculadora.adicao(1,2))

class Calculadora_2(Calculadora):
    def adicao(self, a, b, c):
        return a + b + c

calculadora = Calculadora_2()

print(calculadora.adicao(1,2,3))

# print(calculadora.adicao(1,2)) # -> Neste caso você receberá um erro de que falta um parâmetro

class Calculadora_3(Calculadora):

    def adicao(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

# Você também pode utilizar a definição de parâmetro para criar uma nova variacao do método

calculadora = Calculadora_3()

print(calculadora.adicao(1, 2))
