# Projeto de análise de populacao
# Extração de dados com python

import pandas as pd

# Extraindo os dados da api do sidra
# dados de 2014 a 2021
url = "https://apisidra.ibge.gov.br/values/t/6579/n6/all/v/all/p/last%208"
df = pd.read_json(url)
# Selecionar colunas
df = df[["D3C", "D1C", "V"]]
#Excluir a primeira linha
df_1 = df.iloc[1:,0:]

# # dados de 2006 a 2013
url = "https://apisidra.ibge.gov.br/values/t/6579/n6/all/v/all/p/2006,2008,2009,2011,2012,2013"
df = pd.read_json(url)
# Selecionar colunas
df = df[["D3C", "D1C", "V"]]
#Excluir a primeira linha
df_2 = df.iloc[1:,0:]
# Agregar datasets df_1 e df_2
df_2 = df_2.append(df_1)

# dados de 2001 a 2005
url = "https://apisidra.ibge.gov.br/values/t/6579/n6/all/v/all/p/first%205"
df = pd.read_json(url)
# Selecionar colunas
df = df[["D3C", "D1C", "V"]]
#Excluir a primeira linha
df_3 = df.iloc[1:,0:]
# Agregar datasets df_2 e df_3
df = df_3.append(df_2,)

# carregar o dados para uma csv
# df.to_csv("dataset_populacao.csv")