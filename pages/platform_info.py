from dash import html, dcc
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

dfpie = pd.read_csv("final_dataset.csv").groupby(by="platform").count()
dfheat = pd.read_csv("released_games_dataset.csv").groupby(by=["platform","genre"], as_index=False).count()
left = pd.Series(dfheat["platform"].unique())
left.name = "platform"
right = pd.Series(dfheat["genre"].unique())
right.name = "genre"
temp = pd.merge(left,right,how="cross")
dfheat = pd.merge(dfheat,temp,how="right").fillna(0)
dfheat1 = dfheat.sort_values(by="index",ascending=False).head(100).sort_index()
left1 = pd.Series(dfheat1["platform"].unique())
left1.name = "platform"
right1 = pd.Series(dfheat1["genre"].unique())
right1.name = "genre"
temp1 = pd.merge(left1,right1,how="cross")
dfheat1 = pd.merge(dfheat1,temp1,how="right").fillna(0)
dfheat2 = dfheat.sort_values(by="index",ascending=False).head(400).tail(300).sort_index()
left2 = pd.Series(dfheat2["platform"].unique())
left2.name = "platform"
right2 = pd.Series(dfheat2["genre"].unique())
right2.name = "genre"
temp2 = pd.merge(left2,right2,how="cross")
dfheat2 = pd.merge(dfheat2,temp2,how="right").fillna(0)
dfheat3 = dfheat.sort_values(by="index",ascending=False).tail(len(dfheat)-400).sort_index()
left3 = pd.Series(dfheat3["platform"].unique())
left3.name = "platform"
right3 = pd.Series(dfheat3["genre"].unique())
right3.name = "genre"
temp3 = pd.merge(left3,right3,how="cross")
dfheat3 = pd.merge(dfheat3,temp3,how="right").fillna(0)
fig = go.Figure()
fig.add_trace(go.Pie(labels=dfpie.index, values=dfpie["index"], marker={'colors':px.colors.qualitative.Dark24}))
fig.update_layout(template = "plotly_dark", paper_bgcolor='rgba(0,0,0,0)',autosize = False, width = 1470, height = 1000, title = "Количество выпущенных игр по платформам")
fig2 = go.Figure()
fig2.add_trace(go.Heatmap(x=dfheat1["genre"], y=dfheat1["platform"], z=dfheat1["index"]))
fig2.update_layout(template = "plotly_dark", paper_bgcolor='rgba(0,0,0,0)', width = 1470, height = 1000, autosize = False, title = "Количество выпущенных игр по жанрам и платформам (первая треть)")
fig3 = go.Figure()
fig3.add_trace(go.Heatmap(x=dfheat2["genre"], y=dfheat2["platform"], z=dfheat2["index"]))
fig3.update_layout(template = "plotly_dark", paper_bgcolor='rgba(0,0,0,0)', width = 1470, height = 1000, autosize = False, title = "Количество выпущенных игр по жанрам и платформам (вторая треть)")
fig4 = go.Figure()
fig4.add_trace(go.Heatmap(x=dfheat3["genre"], y=dfheat3["platform"], z=dfheat3["index"]))
fig4.update_layout(template = "plotly_dark", paper_bgcolor='rgba(0,0,0,0)', width = 1470, height = 1000, autosize = False, title = "Количество выпущенных игр по жанрам и платформам (третья треть)")
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig, config={'displayModeBar':False})
        ])
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig2, config={'displayModeBar':False})
        ])
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig3, config={'displayModeBar':False})
        ])
    ]),
        html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig4, config={'displayModeBar':False})
        ])
    ])
])