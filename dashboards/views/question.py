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


def question_view():
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
                            id="dropdown-1",
                            options=[{"label": k, "value": k} for k in domain_names],
                            value="All",
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-2"),
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
                            id="dropdown-3",
                            options=[{"label": k, "value": k} for k in subdomain_names],
                            value="All",
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-4"),
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
                            id="dropdown-5",
                            options=[{"label": k, "value": k} for k in dates],
                            value=dates[0],
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-6"),
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
                            id="dropdown-7",
                            options=[{"label": k, "value": k} for k in users],
                            value="All",
                        ),
                    ),
                    html.Div(className="center-text", children=html.P("to")),
                    html.Div(
                        className="second-dropdown",
                        children=dcc.Dropdown(id="dropdown-8"),
                    ),
                ],
            ),
        ]
    )


@app.callback(Output("dropdown-2", "options"), [Input("dropdown-1", "value")])
def update_domain_dropdown_options(selected_domain):
    return [{"label": k, "value": k} for k in domain_names if selected_domain <= k]


@app.callback(Output("dropdown-2", "value"), [Input("dropdown-2", "options")])
def update_domain_dropdown_value(available_options):
    return available_options[0]["value"]


@app.callback(Output("dropdown-4", "options"), [Input("dropdown-3", "value")])
def update_subdomain_dropdown_options(selected_subdomain):
    return [
        {"label": k, "value": k} for k in subdomain_names if selected_subdomain <= k
    ]


@app.callback(Output("dropdown-4", "value"), [Input("dropdown-4", "options")])
def update_subdomain_dropdown_value(available_options):
    return available_options[0]["value"]


@app.callback(Output("dropdown-6", "options"), [Input("dropdown-5", "value")])
def update_date_dropdown_options(selected_date):
    return [{"label": k, "value": k} for k in dates if selected_date <= k]


@app.callback(Output("dropdown-6", "value"), [Input("dropdown-6", "options")])
def update_date_dropdown_value(available_options):
    return available_options[0]["value"]


@app.callback(Output("dropdown-8", "options"), [Input("dropdown-7", "value")])
def update_user_dropdown_options(selected_user):
    return [{"label": k, "value": k} for k in users if selected_user <= k]


@app.callback(Output("dropdown-8", "value"), [Input("dropdown-8", "options")])
def update_user_dropdown_value(available_options):
    return available_options[0]["value"]
