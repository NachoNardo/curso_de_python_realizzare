# Um loop while executa um bloco de código enquanto a sua condição for verdadeira
# Sintaxe -> while <condição>:
#               <bloco de código>

contador = 0

while contador < 10:
    print(contador)
    contador += 1

# A palavra break é utilizada para encerrar o loop quando ela é chamada

i = 0

while contador < 100:
    print(i)
    if i == 5:
        break
    i += 1

# A palavra continue pula para a próxima execução do loop

i = 0

while i <= 20:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i += 1
