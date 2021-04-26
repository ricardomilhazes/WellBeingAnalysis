import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from dashboards.maindash import app
from dashboards.data.collector import session_col
from dashboards.views.dropdowns import dropdowns


def session_view():
    return html.Div(
        children=[
            dropdowns(
                "dropdown-9",
                "dropdown-10",
                "Domain",
                session_col.distinct("question.domain"),
            ),
            dropdowns(
                "dropdown-11",
                "dropdown-12",
                "Subomain",
                session_col.distinct("question.subdomain"),
            ),
            dropdowns(
                "dropdown-13", "dropdown-14", "Date", session_col.distinct("date.date")
            ),
            dropdowns(
                "dropdown-15", "dropdown-16", "User", session_col.distinct("user")
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
        {"label": k, "value": k}
        for k in session_col.distinct("question.domain")
        if selected_domain <= k
    ], selected_domain


@app.callback(
    Output("dropdown-12", "options"),
    Output("dropdown-12", "value"),
    Input("dropdown-11", "value"),
)
def update_subdomain_dropdown_options(selected_subdomain):
    return [
        {"label": k, "value": k}
        for k in session_col.distinct("question.subdomain")
        if selected_subdomain <= k
    ], selected_subdomain


@app.callback(
    Output("dropdown-14", "options"),
    Output("dropdown-14", "value"),
    Input("dropdown-13", "value"),
)
def update_date_dropdown_options(selected_date):
    return [
        {"label": k, "value": k}
        for k in session_col.distinct("date.date")
        if selected_date <= k
    ], selected_date


@app.callback(
    Output("dropdown-16", "options"),
    Output("dropdown-16", "value"),
    Input("dropdown-15", "value"),
)
def update_user_dropdown_options(selected_user):
    return [
        {"label": k, "value": k}
        for k in session_col.distinct("user")
        if selected_user <= k
    ], selected_user
