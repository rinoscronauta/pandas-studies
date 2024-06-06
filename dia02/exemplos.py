# %%
import pandas as pd

notas = [4.5, 6, 7, 3.5]

# %%
# Quero que exiba as notas maiores do que 5
for i in notas:
    if i>5:
        print(i)

# %%
# usando as notas antigas, somo 1 em cada uma delas
notas_novas = []
for i in notas:
    notas_novas.append(i+1)

notas_novas



# %%
a = [1,2,3,4]
b = a
print(a)
print(b)

# %%
# Ambas são referências, o Python não criou um novo objeto
b.append(5)
print(a)
print(b)
# %%
