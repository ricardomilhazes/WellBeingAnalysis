import dash_core_components as dcc
import dash_html_components as html


def dropdowns(first_dropdown, second_dropdown, dimension, dimension_attributes):
    return html.Div(
        className="dropdown",
        children=[
            html.Label(
                children=dimension,
            ),
            html.Div(
                className="first-dropdown",
                children=dcc.Dropdown(
                    id=first_dropdown,
                    options=[{"label": k, "value": k} for k in dimension_attributes],
                    value=dimension_attributes[0],
                ),
            ),
            html.Div(className="center-text", children=html.P("to")),
            html.Div(
                className="second-dropdown",
                children=dcc.Dropdown(
                    id=second_dropdown, value=dimension_attributes[-1]
                ),
            ),
        ],
    )
