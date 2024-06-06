# %%

import pandas as pd

df = pd.read_parquet("../data/transactions_cart.parquet")
df
# %%

df.info(memory_usage='deep')
# %%
