import plotly.graph_objects as go
from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Minimal Dash Dashboard", className="mt-4 mb-4")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='sample-graph')
        ], md=6),
        dbc.Col([
            dcc.Graph(id='sample-scatter')
        ], md=6)
    ]),
    dbc.Row([
        dbc.Col([
            html.P("This is a minimal Dash dashboard example ready for Docker deployment.", className="mt-4")
        ])
    ])
], fluid=True)

# Callback to update graphs
@app.callback(
    Output('sample-graph', 'figure'),
    Output('sample-scatter', 'figure'),
    Input('sample-graph', 'id')
)
def update_graphs(_):
    # Sample bar chart
    fig1 = go.Figure(data=[
        go.Bar(x=['A', 'B', 'C', 'D'], y=[4, 7, 2, 9], name='Series 1')
    ])
    fig1.update_layout(title='Sample Bar Chart', hovermode='x unified')
    
    # Sample scatter plot
    fig2 = go.Figure(data=[
        go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 4, 6, 3, 7], mode='markers+lines', name='Data')
    ])
    fig2.update_layout(title='Sample Scatter Plot', hovermode='closest')
    
    return fig1, fig2

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=False)
