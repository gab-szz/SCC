import sqlite3

#Chamando variavel de outro arquivo
#print(tela_principal.varrr)

conn = sqlite3.connect('BD_code.db')
cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                cpf INTEGER(11) PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40),
                estado_civil CHAR(20));
               """)

cursor.execute("""
                CREATE TABLE IF NOT EXISTS fornecedores (
                cpf INTEGER(11) PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40),
                estado_civil CHAR(20));
               """)
conn.commit()
print("Banco de dados criado")
cursor.close()