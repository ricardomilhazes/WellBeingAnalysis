import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from dashboards.maindash import app
from dashboards.data.load_data import get_dates, get_users

dates = get_dates("system")
dates.sort()

users = get_users("system")
users.sort()


def system_view():
    return html.Div(
        children=[
            html.Div(
                className="dropdown",
                children=[
                    html.Label(
                        children="Date",
                    ),
                    html.Div(
                        className="first-dropdown",
                        children=dcc.Dropdown(
                            id="dropdown-17",
                            options=[{"label": k, "value": k} for k in dates],
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-18"),
                    ),
                ],
            ),
            html.Div(
                className="dropdown",
                children=[
                    html.Label(
                        children="User",
                    ),
                    html.Div(
                        className="first-dropdown",
                        children=dcc.Dropdown(
                            id="dropdown-19",
                            options=[{"label": k, "value": k} for k in users],
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-20"),
                    ),
                ],
            ),
        ]
    )


@app.callback(
    Output("dropdown-18", "options"),
    Output("dropdown-18", "value"),
    Input("dropdown-17", "value"),
)
def update_date_dropdown_options(selected_date):
    return [
        {"label": k, "value": k} for k in dates if selected_date <= k
    ], selected_date


@app.callback(
    Output("dropdown-20", "options"),
    Output("dropdown-20", "value"),
    Input("dropdown-19", "value"),
)
def update_user_dropdown_options(selected_user):
    return [
        {"label": k, "value": k} for k in users if selected_user <= k
    ], selected_user
