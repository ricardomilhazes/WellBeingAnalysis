import dash_core_components as dcc
import dash_html_components as html

def panel(size, max_rating, min_rating, fig, entries, max_elem, min_elem, updated_graph):
    return html.Div(
        className="panel",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.H3(className="title", children="Statistics"),
                ],
            ),
            html.Div(
                className="panel-body",
                children=[
                    html.Div(
                        className="categories",
                        children=[
                            html.Div(
                                className="category",
                                children=[
                                    html.Span("Number of asnwers"),
                                    html.Span(
                                        id=entries,
                                        children=size
                                    ),
                                ],
                            ),
                            html.Div(
                                className="category",
                                children=[
                                    html.Span("Highest evaluation"),
                                    html.Span(
                                        id=max_elem,
                                        children=max_rating
                                    ),
                                ],
                            ),
                            html.Div(
                                className="category",
                                children=[
                                    html.Span("Lowest Evaluation"),
                                    html.Span(
                                        id=min_elem,
                                        children=min_rating
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        className="chart",
                        children=[dcc.Graph(id=updated_graph, figure=fig)],
                    ),
                ],
            ),
        ],
    )