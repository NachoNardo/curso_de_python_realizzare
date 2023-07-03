# Uma classe pode herdar atributos e métodos de outras classes
# Neste caso basta criar uma classe nova que recebe uma classe "pai" na sua definição

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        pass

# O método super() irá chamar o construtor da classe pai

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        return "Au! Au!"

bicho = Cachorro("Pingo")

print(bicho.som())

print(bicho.nome)

# Você pode criar uma herança múltipla de uma classe passando mais de uma classe como argumento

class Adestrado:
    def adestrado(self):
        return 'sim'

class Pet(Cachorro, Adestrado):
    def __init__(self, nome):
        super().__init__(nome)

    def to_string(self):
        return "Nome: " + self.nome, "Som: " + self.adestrado(), "Som: " + self.som()

pet = Pet("Pingo")

print(pet.adestrado())
print(pet.nome)
print(pet.som())

print(pet.to_string())
