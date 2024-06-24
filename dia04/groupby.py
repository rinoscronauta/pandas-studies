# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# Filtrei um usuário e somei todos seus pontos
condicao = df["IdCustomer"]=="5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user['Points'].sum()

# %%
# Jeito empírico de fazer o código acima para todos os usuários
pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df["IdCustomer"]==i
    pontos[i] = df[condicao]["Points"].sum()

pontos

# %%
# Agrupa por IdCustomer e soma os pontos e apresenta como um DataFrame
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()

# %%
# Agrupa por IdCustomer
# Usa o método agg para passar um dicionário
# Renomeia as colunas
# Reseta os índices
(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())

# %%
import datetime

data1 = df["DtTransaction"][0]
print(data1)
now = datetime.datetime.now()
print(now)

(now - data1).days

# %%

(datetime.datetime.now() - df["DtTransaction"][0]).days

# %%
# Defini uma função 
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days


(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": ['max', recencia]
          })
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())
# %%
