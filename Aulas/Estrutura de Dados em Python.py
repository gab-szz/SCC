# Unidade 2 - Seção 1

# Objetos do tipo sequência: texto, listas e tuplas
# Objetos do tipo set (conjunto).
# Objetos do tipo mapping (dicionário).
# Objetos do tipo array NumPy.

from tkinter import *

#   OBJETOS DO TIPO SEQUÊNCIA
# Os objetos do tipo sequência são estruturas de dados capazes de armazenar mais de um valor.
# Essas estruturas de dados representam sequências finitas indexadas por números não negativos.
# O primeiro elemento de uma sequência ocupa o índice 0; o segundo, 1; o último elemento,
# a posição n - 1, em que n é capacidade de armazenamento da sequência.
# As estruturas de dados desse grupo possuem algumas operações em comum.

# Sequência de Caracteres

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
print(texto.upper())
print(texto.replace("i", 'XX'))

# Split serve para cortar o texto
# Caso seja passado um parâmetro, então o corte será feito no parâmetro especificado.
palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")

#   LISTAS
# Modos de declarar uma lista:
# lista1 = []
# lista2 = ['a', 'b', 'c']
# lista3 = [x for x in iterable]
# list()

# também poderia ter sido criada usando aspas duplas
vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')

# Outro codigo com mesmo resultado:

#   LIST COMPREHENSION
# também chamada de listcomp, é uma forma pythônica de criar uma lista com base
# em um objeto iterável. Esse tipo de técnica é utilizada quando, dada uma sequência,
# deseja-se criar uma nova sequência, porém com as informações originais transformadas
# ou filtradas por um critério. Para entender essa técnica, vamos supor que tenhamos
# uma lista de palavras e desejamos padronizá-las para minúsculo. Observe o código a seguir.

linguagens = ["Python", "Java", "JavaScript",
              "C", "C#", "C++", "Swift", "Go", "Kotlin"]
linguagens2 = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split(
)  # Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)
