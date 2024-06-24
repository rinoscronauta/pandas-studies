# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
# tipos das colunas do DataFrame
df.dtypes

# %%
# Convertendo de número para string - não sobrescrevi
df["Points"].astype(str)

# %%
# Multiplica Points por 2, criando uma coluna nova
df["Points_dobble"] = df["Points"] * 2
df

# %%
df[["Points", "Points_dobble"]].astype(float)

# %%
# Não é possível converter string para número inteiro
df[["UUID", "Name"]].astype(int)

# %%
# Coluna nova com uma lista
df["Lista"] = [[ 1,2 ] for i in df.index ]
df

# %%
# O tipo da lista é objeto
df.dtypes

# %%
