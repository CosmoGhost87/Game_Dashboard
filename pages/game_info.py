from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np

df = pd.read_csv("genre_dataset.csv")
games = np.sort(df["name"].unique())
layout = dbc.Container([
    html.Div([
        html.H1("Выберите игру:", style={'textAlign': 'center', 
                                         'width': 1470}),
        html.Div([
            dcc.Dropdown(
                id='game',
                options=[{'label': i, 'value': i} for i in games],
                value=games[0],
                clearable=False,
                className="dbc",
                style={'border': '1px solid'}
            )
        ])
    ]),
    html.Br(),
    dbc.Col([
        dbc.Row(id="developer", style={'font-size': 36}),
        dbc.Row(id="publisher", style={'font-size': 36}),
        dbc.Row(id="year", style={'font-size': 36}),
        dbc.Row(id="platform", style={'font-size': 36}),
        dbc.Row(id="genre", style={'font-size': 36}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id="cscore", config={'displayModeBar': False})
            ]),
            dbc.Col([
                dcc.Graph(id="uscore", config={'displayModeBar': False})
            ])
        ])
    ]),
])


@callback(
    [Output('developer', 'children'),
     Output('publisher', 'children'),
     Output('year', 'children'),
     Output('platform', 'children'),
     Output('genre', 'children'),     
     Output('cscore', 'figure'),
     Output('uscore', 'figure')
     ],
    Input('game', 'value')
)
def update_text(game):
    temp = df.loc[df["name"] == game]["developer"]
    temp = temp.sort_values(ascending=False).reset_index()
    temp = temp.loc[0]["developer"]
    developer = "Разработчик: " + temp
    temp = df.loc[df["name"] == game]["publisher"]
    temp = temp.sort_values(ascending=False).reset_index()
    temp = temp.loc[0]["publisher"]
    publisher = "Издатель: " + temp
    temp = df.loc[df["name"] == game]["date"]
    temp = temp.sort_values(ascending=False).reset_index()
    temp = temp.loc[0]["date"]
    year = "Год выпуска: " + str(temp)
    temp = df.loc[df["name"] == game]["platform"]
    temp = temp.sort_values(ascending=False).reset_index()
    temp = temp.loc[0]["platform"]
    platform = "Платформа: " + temp
    temp = df.loc[df["name"] == game]["genre"]
    temp = temp.sort_values(ascending=False).reset_index()
    temp = temp.loc[0]["genre"]
    genre = "Жанр: " + temp
    temp = df.loc[df["name"] == game]["cscore"]
    temp = temp.sort_values(ascending=False).reset_index()
    temp = temp.loc[0]["cscore"]
    cscoreValue = float(temp)
    temp = ((1-cscoreValue/10)*255, cscoreValue/10*255, 0)
    cscore = go.Figure(go.Indicator(mode="gauge+number", 
                                    gauge={'axis': {'range': [0, 10]}, 
                                           'bar': {'color': 'rgb'+str(temp)}}, 
                                    value=cscoreValue, title="Critic score"))
    cscore.update_layout(font_family="Play", 
                         template="plotly_dark", 
                         paper_bgcolor='rgba(0,0,0,0)')
    temp = df.loc[df["name"] == game]["uscore"]
    temp = temp.sort_values(ascending=False).reset_index()
    temp = temp.loc[0]["uscore"]
    uscoreValue = float(temp)
    temp = ((1-uscoreValue/10)*255, uscoreValue/10*255, 0)
    uscore = go.Figure(go.Indicator(mode="gauge+number", 
                                    gauge={'axis': {'range': [0, 10]}, 
                                           'bar': {'color': 'rgb' + str()}}, 
                                    value=uscoreValue, title="User score"))
    uscore.update_layout(font_family="Play", 
                         template="plotly_dark", 
                         paper_bgcolor='rgba(0,0,0,0)')
    return developer, publisher, year, platform, genre, cscore, uscore
