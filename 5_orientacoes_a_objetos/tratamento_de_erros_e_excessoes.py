# Erros e excessões em Python podem ser tratados através de um bloco try

try:
    print(1/0)
except Exception as e:
    print(str(e))

# O bloco finally sempre será executado quando um erro ou não ocorrer

try:
    print(1/0)
except:
    print("Ocorreu um erro")
finally:
    print("Essa linha sempre será executada")

# O bloco else será executado caso não ocorra nenhum erro

try:
    print(1/1)
except:
    print("Ocorreu um erro")
else:
    print("Não ocorreu um erro")
finally:
    print("Essa linha sempre será executada")
