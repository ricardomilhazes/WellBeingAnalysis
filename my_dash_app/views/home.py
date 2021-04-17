import dash
import dash_html_components as html
import dash_core_components as dcc

from my_dash_app.maindash import app
from my_dash_app.views.question import question_view
from my_dash_app.views.session import session_view
from my_dash_app.views.system import system_view
from dash.dependencies import Input, Output


def home_view():
    return html.Div(
        [
            dcc.Tabs(
                id="inquiries",
                value="question",
                children=[
                    dcc.Tab(label="Question", value="question"),
                    dcc.Tab(label="Session", value="session"),
                    dcc.Tab(label="System", value="system"),
                ],
            ),
            html.Div(id="inquiries-content"),
        ]
    )


@app.callback(Output("inquiries-content", "children"), Input("inquiries", "value"))
def tab_content(tab):
    if tab == "question":
        return question_view()
    elif tab == "session":
        return session_view()
    elif tab == "system":
        return system_view()
