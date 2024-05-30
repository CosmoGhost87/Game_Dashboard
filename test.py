import pandas as pd
import numpy as np

df = pd.read_csv("genre_dataset.csv")
games = np.sort(df["name"].unique())
print(games)