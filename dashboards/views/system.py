import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

from dash.dependencies import Input, Output
from dashboards.maindash import app
from dashboards.data.collector import system_col
from dashboards.views.dropdowns import dropdowns


def system_view():
    return html.Div(
        children=[
            dropdowns(
                "dropdown-17", "dropdown-18", "Date", system_col.distinct("date.date")
            ),
            dropdowns(
                "dropdown-19", "dropdown-20", "User", system_col.distinct("user.user")
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
        {"label": k, "value": k}
        for k in system_col.distinct("date.date")
        if selected_date <= k
    ], selected_date


@app.callback(
    Output("dropdown-20", "options"),
    Output("dropdown-20", "value"),
    Input("dropdown-19", "value"),
)
def update_user_dropdown_options(selected_user):
    return [
        {"label": k, "value": k}
        for k in system_col.distinct("user.user")
        if selected_user <= k
    ], selected_user
