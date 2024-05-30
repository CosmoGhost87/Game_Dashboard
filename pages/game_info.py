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
                options = [{'label': i, 'value': i} for i in games],
                value = games[0]
            )
        ])
    ]),
    html.Br(),
    html.Div([
        html.H1(id="developer"),
        html.H1(id="publisher"),
        html.H1(id="year"),
        html.H1(id="platform"),
        html.H1(id="genre"),
    ])
])
@callback(
    [Output('developer','children'),
     Output('publisher','children'),
     Output('year','children'),
     Output('platform','children'),
     Output('genre','children'),
     ],
    Input('game','value')
)
def update_text(game):
    developer = "Разработчик: " + df.loc[df["name"] == game]["developer"].sort_values(ascending=False).reset_index().loc[0]["developer"]
    publisher = "Издатель: " + df.loc[df["name"] == game]["publisher"].sort_values(ascending=False).reset_index().loc[0]["publisher"]
    year = "Год выпуска: " + str(df.loc[df["name"] == game]["date"].sort_values(ascending=False).reset_index().loc[0]["date"])
    platform = "Платформа: " + df.loc[df["name"] == game]["platform"].sort_values(ascending=False).reset_index().loc[0]["platform"]
    genre = "Жанр: " + df.loc[df["name"] == game]["genre"].sort_values(ascending=False).reset_index().loc[0]["genre"]
    return developer,publisher,year,platform,genre
