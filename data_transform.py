import pandas as pd
import numpy as np


df1 = pd.read_csv("game_sales_data.csv",sep=',',encoding="unicode_escape")
df2 = pd.read_csv("games-data.csv",sep=',',encoding="unicode_escape")
df3 = pd.read_csv("metacritic_games.csv",sep=',',encoding="unicode_escape")
df1 = df1.iloc[:, [False,True,True,True,True,True,True,False,True]]
df2 = df2.iloc[:, [True,True,True,True,True,True,True,False,False,False]]
df3 = df3.iloc[:, [True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True]]
df1 = df1.rename(columns={'Name':'name','Platform':'platform','Publisher':'publisher','Developer':'developer','Critic_Score':'cscore','User_Score':'uscore','Year':'date'})
df2 = df2.rename(columns={'r-date':'date','score':'cscore','user score':'uscore'})
df3 = df3.rename(columns={'genre(s)':'genre','release_date':'date','metascore':'cscore','user_score':'uscore'})
df1 = df1.dropna(subset=['cscore','uscore'])
df1["publisher"] = df1['publisher'].str.replace(" ","")
df1["developer"] = df1['developer'].str.replace(" ","")
df2["date"] = df2['date'].str[-4:].astype(int)
df3["date"] = df3["date"].str[-4:].astype(int)
df3["publisher"] = df3['publisher'].str.replace(" ","")
df3["developer"] = df3['developer'].str.replace(" ","")
dftemp = df2["genre"].str.split(",",expand=True)
df2["genre"] = dftemp[0]
df2["cscore"] = df2["cscore"]/10
df3["cscore"] = df3["cscore"]/10

df1["platform"] = df1["platform"].str.replace("PSP","PlayStationPortable")
df2["platform"] = df2["platform"].str.replace("PSP","PlayStationPortable")
df1["platform"] = df1["platform"].str.replace("PSV","PlayStationVita")
df1["platform"] = df1["platform"].str.replace("PSN","PlayStationNetwork")
df1["platform"] = df1["platform"].str.replace("PS","PlayStation")
df1["platform"] = df1["platform"].str.replace("GBA","GameBoyAdvance")
df1["platform"] = df1["platform"].str.replace("GB","GameBoy")
df1["platform"] = df1["platform"].str.replace("GC","GameCube")
df1["platform"] = df1["platform"].str.replace("N64","Nintendo64")
df1["platform"] = df1["platform"].str.replace("NS","NintendoSwitch")
df1["platform"] = df1["platform"].str.replace("GEN","SegaGenesis")
df1["platform"] = df1["platform"].str.replace("SNES","SuperNintendoEntertainmentSystem")
df1["platform"] = df1["platform"].str.replace("NES","NintendoEntertainmentSystem")
df1["platform"] = df1["platform"].str.replace("GBA","GameBoyAdvance")
df1["platform"] = df1["platform"].str.replace("X360","Xbox360")
df1["platform"] = df1["platform"].str.replace("XB","Xbox")
df1["platform"] = df1["platform"].str.replace("XOne","XboxOne")

df3["platform"] = df3["platform"].str.replace("PSP","PlayStationPortable")
df3["platform"] = df3["platform"].str.replace("PS","PlayStation")
df3["platform"] = df3["platform"].str.replace("N64","Nintendo64")
df3["platform"] = df3["platform"].str.replace("GC","GameCube")
df3["platform"] = df3["platform"].str.replace("GBA","GameBoyAdvance")
df3["platform"] = df3["platform"].str.replace("DC","SegaDreamcast")
df3["platform"] = df3["platform"].str.replace("VITA","PlayStationVita")
df3["platform"] = df3["platform"].str.replace("Switch","NintendoSwitch")
df3["platform"] = df3["platform"].str.replace("XONE","XboxOne")
df3["platform"] = df3["platform"].str.replace("XBOX","Xbox")
df3["platform"] = df3["platform"].str.replace("X360","Xbox360")
df3["platform"] = df3["platform"].str.replace("WII","Wii")
df3["platform"] = df3["platform"].str.replace("WIIU","WiiU")
df = pd.concat([df1,df2,df3])
df = df.dropna(subset=['genre'])
#df.to_csv("final_dataset.csv")
print(df3)