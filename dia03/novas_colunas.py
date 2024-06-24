# %%

import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=";")

# %%

df["Points_double"] = df["Points"] * 2
df

# %%

df["Points_ratio"] = df["Points_double"] / df["Points"]
df

# %%

df["Constante"] = None
df

# %%
# detecta NA, NaN e None
df.isna()

# %%

df["Points_log"] = np.log(df["Points"])
df

# %%

df.dtypes

# %%
np.log(df[["Points","Points_double","Points_ratio"]])

# %%
# Todos os nomes em letra maiúscula
nomes_alta = []
for i in df['Name']:
    nomes_alta.append(i.upper())

df["Nome_Alta"] = nomes_alta
df

# %%
# É uma maneira melhor e mais elegante de fazer o código acima
df["Name"].str.upper()

# %%
# Definir função get_first, que pega o Nome, coloca em letra maiúscula e
# separa os elementos de "_", e exibe o primeiro elemento.
def get_first(nome:str):
    nome = nome.upper()
    return nome.split("_")[0]


# %%
# Executando a função acima em todas as linhas da coluna Name
# criando uma coluna nova chamada Name_First
df["Name_First"] = df["Name"].apply( get_first )
df

# %%
# Definindo a mesma função como uma função lambda
df["Name"].apply( lambda x: x.upper().split("_")[0] )

# %%
# Define a função que indica a faixa de pontos de cada usuário
# Cria uma coluna nova com essas faixas de pontos

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"
    
df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df

# %%
# Pegar os 3 últimos caracteres das strings das colunas UUID
df["UUID"].apply(lambda x: x[-3:])

# %%
df


# %%

data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1,30,10,45],
    "valor":[100,2000, 15, 500],
    "frequencia":[2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)

def rfv(row):
    
    nota = 0
    
    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0
    
    return nota

# %%
df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm

# %%

df_crm.iloc[0]

# %%
