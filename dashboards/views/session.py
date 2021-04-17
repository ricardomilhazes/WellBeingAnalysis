import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from dashboards.maindash import app
from dashboards.data.load_data import load_data

domain_names = [
    "Database Systems",
    "Natural Language Processing",
    "Artifical Intelligence",
    "All",
]
domain_names.sort()

subdomain_names = [
    "SQL",
    "Stemming",
    "Machine Learning",
    "All",
]
subdomain_names.sort()

dates = ["2019-08-08:22:22.11", "2021-02-17:14:07.37", "2019-04-24:05:02.53"]
dates.sort()

users = ["Alícia Jesus", "Helena Fonseca", "Melissa Costa", "All"]
users.sort()


def session_view():
    return html.Div(
        children=[
            html.Div(
                className="dropdown",
                children=[
                    html.Label(
                        children="Domain",
                    ),
                    html.Div(
                        className="first-dropdown",
                        children=dcc.Dropdown(
                            id="dropdown-9",
                            options=[{"label": k, "value": k} for k in domain_names],
                            value="All",
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-10"),
                    ),
                ],
            ),
            html.Div(
                className="dropdown",
                children=[
                    html.Label(
                        children="Subdomain",
                    ),
                    html.Div(
                        className="first-dropdown",
                        children=dcc.Dropdown(
                            id="dropdown-11",
                            options=[{"label": k, "value": k} for k in subdomain_names],
                            value="All",
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-12"),
                    ),
                ],
            ),
            html.Div(
                className="dropdown",
                children=[
                    html.Label(
                        children="Date",
                    ),
                    html.Div(
                        className="first-dropdown",
                        children=dcc.Dropdown(
                            id="dropdown-13",
                            options=[{"label": k, "value": k} for k in dates],
                            value=dates[0],
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-14"),
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
                            id="dropdown-15",
                            options=[{"label": k, "value": k} for k in users],
                            value="All",
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-16"),
                    ),
                ],
            ),
        ]
    )


@app.callback(Output("dropdown-10", "options"), [Input("dropdown-9", "value")])
def update_domain_dropdown_options(selected_domain):
    return [{"label": k, "value": k} for k in domain_names if selected_domain <= k]


@app.callback(Output("dropdown-10", "value"), [Input("dropdown-10", "options")])
def update_domain_dropdown_value(available_options):
    return available_options[0]["value"]


@app.callback(Output("dropdown-12", "options"), [Input("dropdown-11", "value")])
def update_subdomain_dropdown_options(selected_subdomain):
    return [
        {"label": k, "value": k} for k in subdomain_names if selected_subdomain <= k
    ]


@app.callback(Output("dropdown-12", "value"), [Input("dropdown-12", "options")])
def update_subdomain_dropdown_value(available_options):
    return available_options[0]["value"]


@app.callback(Output("dropdown-14", "options"), [Input("dropdown-13", "value")])
def update_date_dropdown_options(selected_date):
    return [{"label": k, "value": k} for k in dates if selected_date <= k]


@app.callback(Output("dropdown-14", "value"), [Input("dropdown-14", "options")])
def update_date_dropdown_value(available_options):
    return available_options[0]["value"]


@app.callback(Output("dropdown-16", "options"), [Input("dropdown-15", "value")])
def update_user_dropdown_options(selected_user):
    return [{"label": k, "value": k} for k in users if selected_user <= k]


@app.callback(Output("dropdown-16", "value"), [Input("dropdown-16", "options")])
def update_user_dropdown_value(available_options):
    return available_options[0]["value"]
