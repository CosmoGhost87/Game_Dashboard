from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("released_games_dataset.csv")
dftemp = df.groupby(by="genre").count().sort_values(by="index", ascending=False)
headdf = dftemp.head(5)
taildf = dftemp.tail(len(dftemp)-5)
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.groupby(by="date").count().index, y=df.groupby(by="date").count()["index"], name='Amount', marker_color = '#a60c0c', mode="lines+markers"))
fig.update_layout(xaxis_title_text = 'Year', yaxis_title_text = 'Amount', template = "plotly_dark", width = 1470, autosize = False)
fig2 = go.Figure()
fig2.add_trace(go.Histogram(x=taildf.sort_index().index, y=taildf.sort_index()["index"], histfunc="max", name='Amount', marker_color = '#a60c0c'))
fig2.update_layout(xaxis_title_text = 'Genre', yaxis_title_text = 'Amount', template = "plotly_dark", width = 1470, autosize = False)
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig, config={'displayModeBar':False})
        ])
    ]),
    html.Br(),
    html.H1("ТОП-5 жанров, в которых было выпущено больше всего игр", style={'textAlign':'center', 'width':1470}),
    dbc.Row([
        dbc.Col([                
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("ТОП-1")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardBody(
                            html.P(headdf.iloc[0,0]),
                            style={'font-size':24},
                        )]),
                ])
            ], color = "primary", outline=True, style={'textAlign': 'center'})]),
        dbc.Col([                
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("ТОП-2")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardBody(
                            html.P(headdf.iloc[1,0]),
                            style={'font-size':24},
                        )]),
                ])
            ], color = "primary", outline=True, style={'textAlign': 'center'})]),
        dbc.Col([                
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("ТОП-3")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardBody(
                            html.P(headdf.iloc[2,0]),
                            style={'font-size':24},
                        )]),
                ])
            ], color = "primary", outline=True, style={'textAlign': 'center'})]),
        dbc.Col([                
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("ТОП-4")]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardBody(
                            html.P(headdf.iloc[3,0]),
                            style={'font-size':24},
                        )]),
                ])
            ], color = "primary", outline=True, style={'textAlign': 'center'})]),
        dbc.Col([                
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("ТОП-5")]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardBody(
                            html.P(headdf.iloc[4,0]),
                            style={'font-size':24},
                        )]),
                ])
            ], color = "primary", outline=True, style={'textAlign': 'center'})])
    ],className="g-0", style={'width':1470}),
    html.Br(),
    html.H2("Остальные жанры представлены на графике", style={'textAlign':'center', 'width':1470}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig2, config={'displayModeBar':False})
        ])
    ])
])