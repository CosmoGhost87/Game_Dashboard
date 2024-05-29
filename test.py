import pandas as pd

dfheat = pd.read_csv("released_games_dataset.csv").groupby(by=["platform","genre"], as_index=False).count()
left = pd.Series(dfheat["platform"].unique())
left.name = "platform"
right = pd.Series(dfheat["genre"].unique())
right.name = "genre"
temp = pd.merge(left,right,how="cross")
dfheat = pd.merge(dfheat,temp,how="right").fillna(0)
print(dfheat)