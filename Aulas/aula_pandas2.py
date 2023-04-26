import pandas as pd


dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]

}


#   Extraindo informações de um dataframe

dados_dois = pd.DataFrame(dados)

print('\nInformações do DataFrame:\n')
print(dados_dois.info()) # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', dados_dois.shape) # Retorna uma tupla com o número de linhas e colunas
#print('\nTipo de dados:\n', dados_dois.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

#print('\nQual o menor valor de cada coluna?\n', dados_dois.min()) # Extrai o menor de cada coluna 
#print('\nQual o maior valor?\n', dados_dois.max()) # Extrai o valor máximo e cada coluna 
#print('\nQual a média aritmética?\n', dados_dois.mean()) # Extrai a média aritmética de cada coluna numérica
#print('\nQual o desvio padrão?\n', dados_dois.std()) # Extrai o desvio padrão de cada coluna numérica
#print('\nQual a mediana?\n', dados_dois.median()) # Extrai a mediana de cada coluna numérica

#print('\nResumo:\n', dados_dois.describe()) # Exibe um resumo

dados_dois.head() # Exibe os 5 primeiros registros do DataFrame