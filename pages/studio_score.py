from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("final_dataset.csv")
group = df.groupby(by="developer").count().sort_values(by="index",ascending=False).head(30)
dfred = df.where(df["developer"].isin(group.index.to_numpy())).dropna(how='all')
fig = go.Figure()
fig.add_trace(go.Histogram(x=dfred["developer"], y=dfred["cscore"], histfunc="avg", name='Critic score', marker_color = '#009e3c'))
fig.add_trace(go.Histogram(x=dfred["developer"], y=dfred["uscore"], histfunc="avg", name='User score', marker_color = '#004f9e'))
fig.update_layout(xaxis_title_text = 'Developer', yaxis_title_text = 'Score', template = "plotly_dark", width = 1470, autosize = False, title = "Средняя оценка игр по компаниям-разработчикам")
fig2 = go.Figure()
fig2.add_trace(go.Histogram(x=dfred["developer"], y=dfred["index"], name='Amount', marker_color = '#a60c0c'))
fig2.update_layout(xaxis_title_text = 'Developer', yaxis_title_text = 'Amount', template = "plotly_dark", width = 1470, autosize = False, title = "Количество выпущенных игр по компаниям-разработчикам")
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