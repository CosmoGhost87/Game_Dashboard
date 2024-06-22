from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
from pages import games_score,released_game_info,studio_score,game_info,platform_info,info

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
own_css = "C:\\Users\\Cosmo\\Game_Dashboard\\assets\\styles.css"
app = Dash(__name__,external_stylesheets=[dbc.themes.VAPOR, dbc_css, own_css])
app.title = 'Game Dashboard'
app._favicon = "favicon.png"
app.config.suppress_callback_exceptions = True
default_layout = html.Div([html.H1('Стартовая страница дашборда по играм',
                                   style={'textAlign':'center'}),
                            html.H3("Выберите страницу слева для просмотра",
                                    style={'textAlign':'center'}),
                            html.Img(src=app.get_asset_url("dataset-cover.png"),
                                     height=810,
                                     width=1440,
                                     style={'display':'block',
                                            'margin-left':'7rem',
                                            'margin-right':'auto'})])
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#1657a2",
}

CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
sidebar = html.Div(
    [
        html.H2("Дашборд по играм"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Рейтинги игр", href="/games_score", active="exact"),
                dbc.NavLink("Сводка по выпущенным играм", href="/released_game_info", active="exact"),
                dbc.NavLink("Рейтинги студий", href="/studio_score", active="exact"),
                dbc.NavLink("Сводка по игре", href="/game_info", active="exact"),
                dbc.NavLink("Информация по платформам", href="/platform_info", active="exact"),
                dbc.NavLink("Информация о дашборде", href="/info", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def render_page_content(pathname):
    if pathname =="/info":
        return info.layout
    elif pathname == "/games_score":
        return games_score.layout
    elif pathname == "/released_game_info":
        return released_game_info.layout
    elif pathname == "/studio_score":
        return studio_score.layout
    elif pathname == "/game_info":
        return game_info.layout
    elif pathname == "/platform_info":
        return platform_info.layout
    elif pathname == "/":
        return default_layout
    return html.Div([html.H1('Такой страницы не существует',style={'textAlign':'center'}),html.H3("Пожалуйста, не пишите адрес ссылки сами. Используйте меню слева",style={'textAlign':'center'}),html.Img(src=app.get_asset_url("404.png"), style={'display':'block','margin-left':'auto','margin-right':'auto'})])

if __name__ == "__main__":
    app.run_server(debug=True)