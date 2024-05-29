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
fig = go.Figure()
fig.add_trace(go.Pie(labels=dfpie.index, values=dfpie["index"], marker={'colors':px.colors.qualitative.Dark24}))
fig.update_layout(template = "plotly_dark",autosize = False, width = 1470, height = 1000)
fig2 = go.Figure()
fig2.add_trace(go.Heatmap(x=dfheat["genre"], y=dfheat["platform"], z=dfheat["index"]))
fig2.update_layout(template = "plotly_dark", width = 1470, height = 1000, autosize = False)
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
    ])
])