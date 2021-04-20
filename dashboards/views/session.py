import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from dashboards.maindash import app
from dashboards.data.load_data import get_domains, get_subdomains, get_dates, get_users

domain_names = get_domains("session")
domain_names.sort()

subdomain_names = get_subdomains("session")
subdomain_names.sort()

dates = get_dates("session")
dates.sort()

users = get_users("session")
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


@app.callback(
    Output("dropdown-10", "options"),
    Output("dropdown-10", "value"),
    Input("dropdown-9", "value"),
)
def update_domain_dropdown_options(selected_domain):
    return [
        {"label": k, "value": k} for k in domain_names if selected_domain <= k
    ], selected_domain


@app.callback(
    Output("dropdown-12", "options"),
    Output("dropdown-12", "value"),
    Input("dropdown-11", "value"),
)
def update_subdomain_dropdown_options(selected_subdomain):
    return [
        {"label": k, "value": k} for k in subdomain_names if selected_subdomain <= k
    ], selected_subdomain


@app.callback(
    Output("dropdown-14", "options"),
    Output("dropdown-14", "value"),
    Input("dropdown-13", "value"),
)
def update_date_dropdown_options(selected_date):
    return [
        {"label": k, "value": k} for k in dates if selected_date <= k
    ], selected_date


@app.callback(
    Output("dropdown-16", "options"),
    Output("dropdown-16", "value"),
    Input("dropdown-15", "value"),
)
def update_user_dropdown_options(selected_user):
    return [
        {"label": k, "value": k} for k in users if selected_user <= k
    ], selected_user
