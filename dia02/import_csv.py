# %%

import pandas as pd

# %%
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

#%%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

# %%
df_customers["Points"].describe()

# %%
# Quero filtrar os customers que possuem mais do que 1000 pontos
# Faço uma primeira condição, que me fornece um vetor booleano
condicao = df_customers["Points"] > 1000
df_customers[condicao]

# %%
# Quero descobrir a pessoa que mais tem pontos no dataset
condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]

# %%
# colocar a condição dentro do []
df_customers[df_customers["Points"] == df_customers["Points"].max()]

# %%
# obtém o nome da pessoa que tem mais pontos
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%
# Quem tem entre 1000 e 2000 pontos
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)

# %%
# Faz uma cópia do DataFrame que foi filtrado. Aumenta a memória
df_1000_2000 = df_customers[condicao].copy()

# %%
# Quando faço uma cópia eu consigo manipular! Não é a mesma referência
df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000

# %%
# Printa o DataFrame original
df_customers

# %%
# Selecionar duas colunas pelo nome delas. Precisa de [[]] para isso
df_customers[["UUID", "Name"]]

# %%
# Faz uma lista dos nomes das colunas
# Reordena as colunas em ordem alfabética
colunas = df_customers.columns.tolist()
# outro modo: list[df_customers.columns]
colunas.sort()
colunas

# %%
# reatribui o DataFrame pra ele mesmo com a nova ordenação das colunas
# substitui o DataFrame original
df_customers = df_customers[colunas]
df_customers

# %%
# Renomear colunas
df_customers = df_customers.rename(columns={"Name": "Nome",
                                            "Points": "Pontos"})

df_customers

# %%
# outro modo é usar o argumento inplace para substituir o
# DataFrame original com os novos nomes das colunas
df_customers.rename(columns={"UUID":"Id"}, inplace=True)
df_customers
# %%
