from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np

df = pd.read_csv("genre_dataset.csv")
games = np.sort(df["name"].unique())
layout = dbc.Container([
    html.Div([
        html.H1("Выберите игру:", style={'textAlign':'center', 'width':1470}),
        html.Div([
            dcc.Dropdown(
                id = 'game',
                options = [{'label':i, 'value': i} for i in games],
                value = games[0],
                clearable=False,
                className="dbc",
                style={'border':'1px solid'}
            )
        ])
    ]),
    html.Br(),
    dbc.Col([
        dbc.Row(id="developer", style={'font-size':36}),
        dbc.Row(id="publisher", style={'font-size':36}),
        dbc.Row(id="year", style={'font-size':36}),
        dbc.Row(id="platform", style={'font-size':36}),
        dbc.Row(id="genre", style={'font-size':36}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id="cscore", config={'displayModeBar':False})
            ]),
            dbc.Col([
                dcc.Graph(id="uscore", config={'displayModeBar':False})
            ])
        ])
    ]),

])
@callback(
    [Output('developer','children'),
     Output('publisher','children'),
     Output('year','children'),
     Output('platform','children'),
     Output('genre','children'),     
     Output('cscore','figure'),
     Output('uscore','figure')
     ],
    Input('game','value')
)
def update_text(game):
    developer = "Разработчик: " + df.loc[df["name"] == game]["developer"].sort_values(ascending=False).reset_index().loc[0]["developer"]
    publisher = "Издатель: " + df.loc[df["name"] == game]["publisher"].sort_values(ascending=False).reset_index().loc[0]["publisher"]
    year = "Год выпуска: " + str(df.loc[df["name"] == game]["date"].sort_values(ascending=False).reset_index().loc[0]["date"])
    platform = "Платформа: " + df.loc[df["name"] == game]["platform"].sort_values(ascending=False).reset_index().loc[0]["platform"]
    genre = "Жанр: " + df.loc[df["name"] == game]["genre"].sort_values(ascending=False).reset_index().loc[0]["genre"]
    cscoreValue = float(df.loc[df["name"] == game]["cscore"].sort_values(ascending=False).reset_index().loc[0]["cscore"])
    cscore = go.Figure(go.Indicator(mode="gauge+number", gauge={'axis':{'range':[0,10]},'bar':{'color':'rgb' + str(((1-cscoreValue/10)*255,cscoreValue/10*255,0))}}, value=cscoreValue))
    cscore.update_layout(template = "plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    uscoreValue = float(df.loc[df["name"] == game]["uscore"].sort_values(ascending=False).reset_index().loc[0]["uscore"])
    uscore = go.Figure(go.Indicator(mode="gauge+number", gauge={'axis':{'range':[0,10]},'bar':{'color':'rgb' + str(((1-uscoreValue/10)*255,uscoreValue/10*255,0))}}, value=uscoreValue))
    uscore.update_layout(template = "plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    return developer,publisher,year,platform,genre,cscore,uscore
