# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=';')
df

# %%
# sort_values ordena do menor para o maior
# o argumento ascending = False me permite ordenar do maior para o menor

df = (df.sort_values( by=["Points", "Name"],
                      ascending=[False, True] )
        .rename(columns={"Name":"Nome", "Points":"Pontos"}))

df