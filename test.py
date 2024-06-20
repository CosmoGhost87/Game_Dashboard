import pandas as pd
import numpy as np

df = pd.read_csv("final_dataset.csv")
group = df.groupby(by="developer").count().sort_values(by="index",ascending=False).head(30)
dfred = df.where(df["developer"].isin(group.index.to_numpy())).dropna(how='all')
print(dfred)