import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output
from dashboards.maindash import app
from dashboards.data.collector import question_col
from dashboards.utils.graph import create_graph
from dashboards.utils.stats import question_stats
from dashboards.views.dropdowns import dropdowns
from dashboards.views.panel import panel

max_rating, min_rating, average_rating, size = question_stats(question_col.find())

fig = create_graph(average_rating)


def question_view():
    return html.Div(
        children=[
            dropdowns(
                "dropdown-1",
                "dropdown-2",
                "Domain",
                question_col.distinct("question.domain"),
            ),
            dropdowns(
                "dropdown-3",
                "dropdown-4",
                "Subdomain",
                question_col.distinct("question.subdomain"),
            ),
            dropdowns(
                "dropdown-5", "dropdown-6", "Date", question_col.distinct("date.date")
            ),
            dropdowns(
                "dropdown-7", "dropdown-8", "User", question_col.distinct("user")
            ),
            panel(
                size,
                max_rating,
                min_rating,
                fig,
                "entries",
                "max-elem",
                "min-elem",
                "updated-graph",
            ),
        ]
    )


@app.callback(
    Output("dropdown-2", "options"),
    Input("dropdown-1", "value"),
)
def update_domain_dropdown_options(selected_domain):
    return [
        {"label": k, "value": k}
        for k in question_col.distinct("question.domain")
        if selected_domain <= k
    ]


@app.callback(
    Output("dropdown-4", "options"),
    Input("dropdown-3", "value"),
)
def update_subdomain_dropdown_options(selected_subdomain):
    return [
        {"label": k, "value": k}
        for k in question_col.distinct("question.subdomain")
        if selected_subdomain <= k
    ]


@app.callback(
    Output("dropdown-6", "options"),
    Input("dropdown-5", "value"),
)
def update_date_dropdown_options(selected_date):
    return [
        {"label": k, "value": k}
        for k in question_col.distinct("date.date")
        if selected_date <= k
    ]


@app.callback(
    Output("dropdown-8", "options"),
    Input("dropdown-7", "value"),
)
def update_user_dropdown_options(selected_user):
    return [
        {"label": k, "value": k}
        for k in question_col.distinct("user")
        if selected_user <= k
    ]


@app.callback(
    Output("entries", "children"),
    Output("max-elem", "children"),
    Output("min-elem", "children"),
    Output("updated-graph", "figure"),
    Input("dropdown-1", "value"),
    Input("dropdown-2", "value"),
    Input("dropdown-3", "value"),
    Input("dropdown-4", "value"),
    Input("dropdown-5", "value"),
    Input("dropdown-6", "value"),
    Input("dropdown-7", "value"),
    Input("dropdown-8", "value"),
)
def update_figure(
    first_domain,
    second_domain,
    first_subdomain,
    second_subdomain,
    first_date,
    second_date,
    first_user,
    second_user,
):
    cursor = question_col.find(
        {
            "question.domain": {"$gte": first_domain, "$lte": second_domain},
            "question.subdomain": {
                "$gte": first_subdomain,
                "$lte": second_subdomain,
            },
            "date.date": {"$gte": first_date, "$lte": second_date},
            "user": {"$gte": first_user, "$lte": second_user},
        }
    )

    if cursor.count() <= 0:
        fig = create_graph(0.00)
        size = 0
        max_rating = "No value"
        min_rating = "No value"

        return size, max_rating, min_rating, fig

    max_rating, min_rating, average_rating, size = question_stats(cursor)
    fig = create_graph(average_rating)

    return size, max_rating, min_rating, fig
