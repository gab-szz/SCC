import sqlite3

# Definição de variáveis
path = r"C:\Users\Gabriel Silvio\Documents\Projetos\Python\SCC - Remake\Aulas"

# Conectando ao banco de dados
conn = sqlite3.connect(path+r'\aulaDB.db')
# Um cursor é uma ponte entre o BD e o código:
cursor = conn.cursor()

# CRIANDO UMA TABELA
# ddl_create = """
# CREATE TABLE fornecedor (
#    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#    nome_fornecedor TEXT NOT NULL,
#    cnpj VARCHAR(18) NOT NULL,
#    cidade TEXT,
#    estado VARCHAR(2) NOT NULL,
#    cep VARCHAR(9) NOT NULL,
#   data_cadastro DATE NOT NULL
# );
# """
# cursor.execute(ddl_create)

# Criando objetos com os dados
cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
""")
teste = "testeeeee"
cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('{}', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
""".format(teste))

# Outra maneira de inserir dados

dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),
    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),
    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
]

cursor.executemany("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES (?, ?, ?, ?, ?, ?)""", dados)

# Finalmente grava as alterações na tabela:
conn.commit()

print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

# Puxando os dados para uma variável
cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
resultado[:2]

# Exibindo os dados
for linha in resultado:
    print(linha)

# Podemos capturar também os dados de uma chave específica
cursor.execute("SELECT * FROM fornecedor WHERE id_fornecedor = 5")
resultado = cursor.fetchall()
print(resultado)

# Modificando os dados de uma tabela
cursor.execute(
    "UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

# Deletando
cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

# Finalizando a conexão com o cursor e o BD
cursor.close()
conn.close()
