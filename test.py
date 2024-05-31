import pandas as pd
import numpy as np

df = pd.read_csv("genre_dataset.csv")
df["genre"] = df["genre"].str.split(",")
temp = []
for i in range (0, len(df)):
    temp.append(set(df.loc[i,"genre"]))
df["genre"] = temp
print(df)