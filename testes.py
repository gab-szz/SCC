import sqlite3

conn = sqlite3.connect("BD_SCC.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM user")
resultado = cursor.fetchall()

# Exibindo os dados
print(resultado)