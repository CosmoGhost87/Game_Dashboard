import pandas as pd

dfheat = pd.read_csv("released_games_dataset.csv").groupby(by=["platform","genre"], as_index=False).count()
left = pd.Series(dfheat["platform"].unique())
left.name = "platform"
right = pd.Series(dfheat["genre"].unique())
right.name = "genre"
temp = pd.merge(left,right,how="cross")
dfheat = pd.merge(dfheat,temp,how="right").fillna(0)
dfheat1 = dfheat.sort_values(by="index",ascending=False).head(30).sort_index()
left1 = pd.Series(dfheat1["platform"].unique())
left1.name = "platform"
right1 = pd.Series(dfheat1["genre"].unique())
right1.name = "genre"
temp1 = pd.merge(left1,right1,how="cross")
dfheat1 = pd.merge(dfheat1,temp1,how="right").fillna(0)
dfheat2 = dfheat.sort_values(by="index",ascending=False).head(len(dfheat)-30).sort_index()
left2 = pd.Series(dfheat2["platform"].unique())
left2.name = "platform"
right2 = pd.Series(dfheat2["genre"].unique())
right2.name = "genre"
temp2 = pd.merge(left2,right2,how="cross")
dfheat2 = pd.merge(dfheat2,temp2,how="right").fillna(0)
print(dfheat2)