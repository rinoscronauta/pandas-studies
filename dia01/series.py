# %%
import pandas as pd

# %%

idades = [30, 42, 90, 34]
idades

# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1) 
print(media, variancia)

# %%
# Transformação para séries Pandas
series_idades = pd.Series(idades)
series_idades

# %%
# Métodos da séries pandas
# Média
series_idades.mean()

# %%
# Variância
series_idades.var()

# %%
# Desvio padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# 3o Quartil
series_idades.quantile(0.75)

# %%
# Sumarização
series_idades.describe()

# %%
# Dimensão da série
series_idades.shape

# %%
# Navegando na lista - primeiro elemento
idades[0]

# %%
# Navegando na série
series_idades[3]

# %%
# Saber os index da série
series_idades.index

# %%
# Alterando index da série
series_idades.index = ['l', 'a', 'u', 'g']

# %%
# Navegando nos índices novos
series_idades['l']

# %%
# Mudando os index de novo
series_idades.index = [40, 10, 30, 20]

# %%
series_idades

# %%
# Ignora o index e usa a posição do elemento - elementos 2 e 3
series_idades.iloc[2:4]

# %%
# Ignora o index e usa a posição do elemento - elementos 0 e 1
series_idades.iloc[0:2]

# %%
# Usa os próprios índices - é similar ao series_idades[40]
series_idades.loc[40]

# %%
# Criar um atributo para a série
series_idades.name = 'idades'
series_idades

# %%
# Posso criar o atributo no momento em que eu crio a série
series_idades = pd.Series(idades, name="idades")
series_idades
# %%
