import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample data for dashboard
df = px.data.iris()

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sample Dashboard"),
    html.Label("Select X axis:"),
    dcc.Dropdown(
        id="xaxis-column",
        options=[{"label": col, "value": col} for col in df.columns if df[col].dtype != object],
        value="sepal_width"
    ),
    html.Label("Select Y axis:"),
    dcc.Dropdown(
        id="yaxis-column",
        options=[{"label": col, "value": col} for col in df.columns if df[col].dtype != object],
        value="sepal_length"
    ),
    dcc.Graph(id='indicator-graphic')
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'))
def update_graph(xaxis_column_name, yaxis_column_name):
    fig = px.scatter(
        df, x=xaxis_column_name, y=yaxis_column_name,
        color="species",
        title=f'{yaxis_column_name} vs {xaxis_column_name}'
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)