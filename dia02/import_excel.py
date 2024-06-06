# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# dimensões do nosso DataFrame. Quantas linhas e quantas colunas?
df.shape

# %%
# 5 primeiras linhas
df.head()

# %%
# 5 últimas colunas
df.tail()

# %%
# faz uma lista com a ordem que eu quero das colunas
# substitui o DataFrame original
colunas = ['UUID',
           "Points",
           'IdCustomer',
           "DtTransaction"]

df = df[colunas]
df

# %%
# Informação sobre o DataFrame, incluindo quanto de memória está ocupando
df.info(memory_usage='deep')
# %%
