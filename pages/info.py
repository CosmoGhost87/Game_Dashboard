from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

layout = dbc.Container([
    html.H2("Данный дашброд показывает рейтинг и статистику по играм, которые были выпущены с 1995 по 2020 (оценки пользователей и критиков, количество выпущенных игр, издателей, игровые платформы)"),
    html.H3("В нем вы можете увидеть:"),
    html.P(["• Рейтинги игр по их оценкам;",html.Br(),
            "• Количество выпущенных игр по годам и жанрам;",html.Br(),
            "• Рейтинги студий по оценкам;",html.Br(),
            "• Сводку по каждой игре;",html.Br(),
            "• Диаграмма, показывающая на каких платформах больше всего игр."]),
    html.H3("Данные для данного дашборда были взяты из следующих датасетов:"),
    html.P(["• ",html.A("Metacritic all time games stats",href="https://www.kaggle.com/datasets/skateddu/metacritic-all-time-games-stats"),
            html.Br(),
            "• ", html.A("Metacritic video-games data",href="https://www.kaggle.com/datasets/brunovr/metacritic-videogames-data"),
            html.Br(),
            "• ", html.A("Video Game Sales Data",href="https://www.kaggle.com/datasets/holmjason2/videogamedata")]),
    html.H3("В дашборде были использованы следующие библиотеки:"),
    html.P([html.I("• dash"),html.Br(),
            html.I("• pandas"),html.Br(),
            html.I("• dash_bootstrap_components"),html.Br(),
            html.I("• numpy"),html.Br(),
            html.I("• plotly")]),
    html.H3("Авторами дашборда являются:"),
    html.P([html.I("Дерюгин Игорь"),html.Br(),
            html.I("Елохин Валерий"),html.Br()]),
    html.H3(["Скачать данный дашборд вы можете из нашего ", html.A("git", href="https://github.com/CosmoGhost87/Game_Dashboard")])
])