from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("final_dataset.csv")
fig = go.Figure()
fig.add_trace(go.Histogram(x=df["date"], y=df["cscore"], histfunc="avg", name='Critic score', marker_color = '#009e3c'))
fig.add_trace(go.Histogram(x=df["date"], y=df["uscore"], histfunc="avg", name='User score', marker_color = '#004f9e'))
fig.update_layout(font_family="Play", xaxis_title_text = 'Year', yaxis_title_text = 'Score', paper_bgcolor='rgba(0,0,0,0)', template = "plotly_dark", width = 1470, autosize = False, title = "Средние оценки игр по годам")
fig2 = go.Figure()
fig2.add_trace(go.Histogram(x=df["genre"].sort_values(), y=df["cscore"], histfunc="avg", name='Critic score', marker_color = '#009e3c', ))
fig2.add_trace(go.Histogram(x=df["genre"].sort_values(), y=df["uscore"], histfunc="avg", name='User score', marker_color = '#004f9e'))
fig2.update_layout(font_family="Play", xaxis_title_text = 'Genre', yaxis_title_text = 'Score', paper_bgcolor='rgba(0,0,0,0)', template = "plotly_dark", width = 1470, autosize = False, title = "Средние оценки игр по жанрам")
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