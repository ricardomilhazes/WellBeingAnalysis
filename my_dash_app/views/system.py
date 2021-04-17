import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from my_dash_app.maindash import app
from my_dash_app.data.load_data import load_data

dates = ["2019-08-08:22:22.11", "2021-02-17:14:07.37", "2019-04-24:05:02.53"]
dates.sort()

users = ["Alícia Jesus", "Helena Fonseca", "Melissa Costa", "All"]
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
                            value=dates[0],
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
                            value="All",
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


@app.callback(Output("dropdown-18", "options"), [Input("dropdown-17", "value")])
def update_date_dropdown_options(selected_date):
    return [{"label": k, "value": k} for k in dates if selected_date <= k]


@app.callback(Output("dropdown-18", "value"), [Input("dropdown-18", "options")])
def update_date_dropdown_value(available_options):
    return available_options[0]["value"]


@app.callback(Output("dropdown-20", "options"), [Input("dropdown-19", "value")])
def update_user_dropdown_options(selected_user):
    return [{"label": k, "value": k} for k in users if selected_user <= k]


@app.callback(Output("dropdown-20", "value"), [Input("dropdown-20", "options")])
def update_user_dropdown_value(available_options):
    return available_options[0]["value"]
