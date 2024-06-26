from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("released_games_dataset.csv")
dftemp = df.groupby(by="genre").count().sort_values(by="index", ascending=False)
headdf = dftemp.head(5)
taildf = dftemp.tail(len(dftemp)-5)
taildf1 = taildf.head(50)
taildf2 = taildf.tail(115)
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.groupby(by="date").count().index, y=df.groupby(by="date").count()["index"], name='Amount', marker_color = '#a60c0c', mode="lines+markers"))
fig.update_layout(font_family="Play", xaxis_title_text = 'Year', yaxis_title_text = 'Amount', template = "plotly_dark", width = 1470, autosize = False, paper_bgcolor='rgba(0,0,0,0)', title = "Количество выпущенных игр по годам")
fig2 = go.Figure()
fig2.add_trace(go.Histogram(x=taildf1.sort_values(by="index", ascending=False).index, y=taildf1.sort_values(by="index", ascending=False)["index"], histfunc="max", name='Amount', marker_color = '#a60c0c'))
fig2.update_layout(font_family="Play", xaxis_title_text = 'Genre', yaxis_title_text = 'Amount', template = "plotly_dark", width = 1470, autosize = False, paper_bgcolor='rgba(0,0,0,0)', title = "Количество выпущенных игр по жанрам (первая половина)")
fig3 = go.Figure()
fig3.add_trace(go.Histogram(x=taildf2.sort_values(by="index", ascending=False).index, y=taildf2.sort_values(by="index", ascending=False)["index"], histfunc="max", name='Amount', marker_color = '#a60c0c'))
fig3.update_layout(font_family="Play", xaxis_title_text = 'Genre', yaxis_title_text = 'Amount', template = "plotly_dark", width = 1470, autosize = False, paper_bgcolor='rgba(0,0,0,0)', title = "Количество выпущенных игр по жанрам (вторая половина)")
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
                    dbc.CardHeader(headdf.index[0])
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
                    dbc.CardHeader(headdf.index[1])
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
                    dbc.CardHeader(headdf.index[2])
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
                    dbc.CardHeader(headdf.index[3])]),
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
                    dbc.CardHeader(headdf.index[4])]),
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
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig3, config={'displayModeBar':False})
        ])
    ])
])