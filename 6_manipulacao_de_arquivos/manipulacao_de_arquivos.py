# Abrir um arquivo

file = open("arquivo.txt", "r")

texto = file.read()

print(texto)

file.close()

# É normal manipular arquivos de texto dividindo-os com linhas
# O método split com o caractere especial de pular linha '\n'
# Fará uma lista com cada uma das linhas

print(texto.split('\n'))

# Mas você pode ler o arquivo em linhas mais facilmente com o método readlines()

file = open("arquivo.txt", "r")

texto = file.readlines()

for linha in texto:
    print(linha)

file.close()

# Para escrever um arquivo iremos abrí-lo utilizando o parâmetro w
# Com o parâmetro w iremos abrir um arquivo ou criá-lo se ele não existe

file = open("escrita.txt", "w")

texto = ["Escrever primeira linha\n", "Escrever segunda linha\n", "Escrever terceira linha\n"]

file.writelines(texto)

file.close()

# O modo w e w+ permitem a escrita do texto, mas apagam o conteúdo original
file = open("escrita.txt", "w")

file.write("texto\n")

file.close()

# O modo a e a+ permitem a escrita e adicionam o texto no final do arquivo original
file = open("escrita.txt", "a+")

file.write("adição ao final\n")

file.close()
