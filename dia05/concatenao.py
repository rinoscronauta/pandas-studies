# %%
import pandas as pd
import os

# função que recebe um caminho e retorna um dataframe modificado
def import_etl(path:str):
    
    # limpa o caminho do arquivo
    name = path.split("/")[-1].split(".")[0]

    df = (pd.read_csv(path, sep=';')
    #renomeia a coluna pra ter o nome da tabela
            .rename(columns={"valor":name})
    # define como índice 3 colunas que se repetem em todas as tabelas
            .set_index(["cod","nome","período"]))
    
    return df

# %%

path = "../data/ipea/"
files = os.listdir(path)

dfs = []
for i in files:
    dfs.append(import_etl(path+i))

# reseta os índices
df_bia = pd.concat(dfs, axis=1).reset_index()

# salva o csv com a tabelona concatenada
# df_bia.to_csv("../data/bia_consolidado.csv", sep=";", index=False)

# %%

df_bia
# %%
