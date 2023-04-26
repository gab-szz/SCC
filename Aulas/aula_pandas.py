import pandas as pd

# Construtor do Series
# pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
lista_nomes = "Joyce Anna Pedro Altair Bonoro".split()
pd.Series(lista_nomes)

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}
print(pd.Series(dados)) # Cria um Series com dicionario

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

series_dados2 = pd.Series(lista_nomes, index=cpfs) #Cada cpf será indez de um nome, na mesma ordemss
print(series_dados2.loc['111.111.111-11'])

series_dados = pd.Series([10.2, -1, None, 15, 23.4])

print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas
print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object
print('Os valores são únicos?', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)
print('Existem valores nulos?', series_dados.hasnans) # Verifica se existem valores nulos
print('Quantos valores existem?', series_dados.count()) # Conta quantas valores existem (excluí os nulos)

print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica
print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica

print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series

# DataFrames
#   DataFrame com apenas nomes e index n-1
pddt = pd.DataFrame(lista_nomes, columns=['nome'])
print(pddt)

#   Dataframe com nomes e cpfs como inde
pddt = pd.DataFrame(lista_nomes, columns=['nome'], index=cpfs)
print(pddt)

#   Dataframe com vários dados
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]
dados = list(zip(lista_nomes, cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas
pddt = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])
print(pddt)

#   Construtor DataFrame com dicionário
dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

pddt = pd.DataFrame(dados)
print(pddt)

#   Seleção de colunas em um DataFrame
