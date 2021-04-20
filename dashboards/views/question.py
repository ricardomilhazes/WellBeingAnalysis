import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from dashboards.maindash import app
from dashboards.data.load_data import get_domains, get_subdomains, get_dates, get_users

domain_names = get_domains("question")
domain_names.sort()

subdomain_names = get_subdomains("question")
subdomain_names.sort()

dates = get_dates("question")
dates.sort()

users = get_users("question")
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


@app.callback(
    Output("dropdown-2", "options"),
    Output("dropdown-2", "value"),
    Input("dropdown-1", "value"),
)
def update_domain_dropdown_options(selected_domain):
    return [
        {"label": k, "value": k} for k in domain_names if selected_domain <= k
    ], selected_domain


@app.callback(
    Output("dropdown-4", "options"),
    Output("dropdown-4", "value"),
    Input("dropdown-3", "value"),
)
def update_subdomain_dropdown_options(selected_subdomain):
    return [
        {"label": k, "value": k} for k in subdomain_names if selected_subdomain <= k
    ], selected_subdomain


@app.callback(
    Output("dropdown-6", "options"),
    Output("dropdown-6", "value"),
    Input("dropdown-5", "value"),
)
def update_date_dropdown_options(selected_date):
    return [
        {"label": k, "value": k} for k in dates if selected_date <= k
    ], selected_date


@app.callback(
    Output("dropdown-8", "options"),
    Output("dropdown-8", "value"),
    Input("dropdown-7", "value"),
)
def update_user_dropdown_options(selected_user):
    return [
        {"label": k, "value": k} for k in users if selected_user <= k
    ], selected_user
