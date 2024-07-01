# %%
import pandas as pd
import numpy as np

df = pd.read_excel("../data/transacao_cartao.xlsx")
df

# %%
# se necessário, mudar o formato da Data
df['dtTransaction'] = pd.to_datetime(df['dtTransaction'],
                                     format='%d/%m/%Y')

df
# %%
# fornece as parcelas e os valores delas
def fatia_parcelas(row):
    return [row["Valor"]/ row["Parcelas"] for i in range(row["Parcelas"])]

df['ValorParcela'] = df.apply(fatia_parcelas, axis=1)

df

# %%
# transformar cada elemento da lista em uma coluna
df_fatura = df.explode("ValorParcela")
df_fatura

# %%
# descarta as colunas Valor e Parcelas
df_fatura = df_fatura.drop(['Valor','Parcelas'],
                           axis=1)

df_fatura

# %%
# Coluna nova indicando quantos meses soma à data da transação
df_fatura["Months_add"] = (df_fatura.groupby("idTransaction")["dtTransaction"]
                                    .rank('first')
                                    .astype(int))

df_fatura
# %%
# Coluna nova com a data da fatura que será cobrada a parcela
def add_months(row):
    new_date = row["dtTransaction"] + np.timedelta64(row['Months_add']*30, 'D')
    dt_str = new_date.strftime("%Y-%m")
    return dt_str

df_fatura["DtFatura"] = df_fatura.apply(add_months, axis=1)
df_fatura
# %%
# soma o valor da parcela a ser paga naquele mês
df_fatura_mes = (df_fatura.groupby(['idCliente', 'DtFatura'])["ValorParcela"]
                          .sum()
                          .reset_index())
df_fatura_mes

# %%
# muda a visualização da tabela
df_fatura_mes_pivot_table = (df_fatura_mes.pivot_table(columns="DtFatura",
                                          index="idCliente",
                                          values="ValorParcela")
                              .fillna(0)
                              .reset_index()
                              )
df_fatura_mes_pivot_table

# %%
# Salva em Excel
df_fatura_mes_pivot_table.to_excel("Fatura_detalhada.xlsx")
# %%
