# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum()

# %%
# Quantos NAs tenho no meu Dataset inteiro, coluna a coluna
df.isna().sum()

# %%
df.isna().mean()

# %%
# Tratando NAs com a média da coluna - para análise de dados é bom
# Para machine learning não!
df.fillna({
        "idade": df["idade"].mean(),
        "renda":df["renda"].mean(),
        })

# %%
# O dropna remove as linhas que contém NA
# how indica COMO remover ('all' = todas, 'any' = ao menos uma)
# subset é para indicar quais colunas
df.dropna(subset=["idade", "renda"], how='any')

# %%
# thresh é quantos valores não-nulos tem que ter para não ser removido
df.dropna(axis=1, thresh=3)

# %%
