import plotly.graph_objs as go
import plotly.express as px


def create_graph(average_rating):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=average_rating,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": "Average Rating"},
            gauge={"axis": {"range": [1, 5]}},
        )
    )

    return fig
