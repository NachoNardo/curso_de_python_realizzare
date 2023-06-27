import sqlite3 # Importa o pacote que permite a manipulação do banco SQLite3

conexao = sqlite3.connect('curso_de_python.db') # Cria conexão de banco de dados com o caminho indicado
                                                # Se não houver um banco de dados, ele o cria

# É necessário criar um cursor para trabalhar com o banco através do código
cursor = conexao.cursor()

# Iremos criar uma tabela do banco de dados
# cursor.execute( '''
#     CREATE TABLE aluno (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nome TEXT,
#         nota REAL,
#         biografia BLOB
#     )
# ''')

# Inserir um registro na tabela
cursor.execute(" INSERT INTO aluno (nome, nota, biografia) VALUES ('Leonardo Holanda', 9.5, 'bla bla bla bla')")
cursor.execute(" INSERT INTO aluno (nome, nota, biografia) VALUES ('Maria Chiquinha', 10.0, 'bla bla bla bla')")
cursor.execute(" INSERT INTO aluno (nome, nota, biografia) VALUES ('Tonhão do Bar', 6.5, 'bla bla bla bla')")
cursor.execute(" INSERT INTO aluno (nome, nota, biografia) VALUES ('Zé das couves', 4.5, 'bla bla bla bla')")

#conexao.rollback() # Esse comando desfaz a última operação caso ela não tenha sido salva

conexao.commit() # Esse comando executa as operações e as salva de fato

# Busca um dado dentro da tabela

cursor.execute("SELECT * FROM aluno WHERE id = 1")

aluno = cursor.fetchone()

print(aluno)
print(aluno[0])
print(aluno[1])
print(aluno[2])
print(aluno[3])

# Como receber todos os resultados

cursor.execute("SELECT * FROM aluno WHERE id > 1")

alunos = cursor.fetchall()

print(alunos)

# Como receber um número limitado de resultados

cursor.execute("SELECT * FROM aluno WHERE id > 1")

alunos = cursor.fetchmany(2)

print(alunos)

# Atualizar os dados de um aluno

cursor.execute("UPDATE aluno SET nome = 'João' WHERE id = 1")

conexao.commit()

cursor.execute("SELECT * FROM aluno WHERE id = 1")

aluno = cursor.fetchone()

print(aluno)

# Vamos apagar um registro da tabela

cursor.execute("DELETE FROM aluno WHERE id = 1")

conexao.commit()

cursor.execute("SELECT * FROM aluno")

alunos = cursor.fetchall()

print(alunos)
