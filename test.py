import pandas as pd
import numpy as np

df = pd.read_csv("released_games_dataset.csv")
dftemp = df.groupby(by="genre").count().sort_values(by="index", ascending=False)
headdf = dftemp.head(5)
print(headdf.index[0])