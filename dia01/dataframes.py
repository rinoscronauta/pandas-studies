# %%
import pandas as pd
# %%
# Dicionário
data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade": [31, 32, 31, 2]
}

#%%
# Idade da primeira pessoa
data["idade"][0]

# %%
# DataFrame - um conjunto de séries
df = pd.DataFrame(data)
df
#%%
# df["idade"] é uma série, e para garantir que quero o primeiro elemento
df["idade"].iloc[0]

# %%
# primeira posição da série 'sobrenome'
df['sobrenome'].iloc[0]

# %%
# uma série com todo o conteúdo da primeira linha do DataFrame
df.iloc[0]

# %%
# O nome da série 'idade' é o índice
df['idade']

# %%
# Trocando os índices do DataFrame
df.index=[3,2,1,0]
df
# %%
# Pego a idade do índice 0 - novo. Para o primeiro índice preciso usar .iloc[0]
df["idade"][0]

# %%
# Index do DataFrame
df.index

# %%
# Colunas do DataFrame
df.columns

# %%
# Um método que mostra as informações do DataFrame
# o agumento é para mostrar o quanto de memória o DataFrame está usando
df.info(memory_usage='deep')

# %%
# um atributo que mostra as colunas e o tipo de objeto delas
df.dtypes

# %%
# Adicionando uma coluna nova ao DataFrame
df['peso'] = [80, 53, 65, 14]

# %%
# O método describe fornece as estatísticas das colunas numéricas
sumario = df.describe()
sumario

# %%
sumario['peso']['mean']

# %%
# Mostra as n primeiras linhas - o padrão é 5
df.head(2)

# %%
# Mostra as n últimas linhas - o padrão é 5
df.tail(2)