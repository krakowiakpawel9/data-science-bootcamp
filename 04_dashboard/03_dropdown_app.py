import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Dropdown(
        id='drop-1',
        options=[
            {'label': 'Polska', 'value': 'PL'},
            {'label': 'Niemcy', 'value': 'GER'}
        ],
        value='PL'
    ),

    dcc.Graph(
        id='graph-1'
    )
])

@app.callback(
    Output('graph-1', 'figure'),
    [Input('drop-1', 'value')]
)
def update_graph(value):
    print(value)
    data_dict = {
        'PL': [3, 2, 5, 4, 7, 2, 4],
        'GER': [4, 1, 3, 4, 2, 4, 1]
    }
    return {'data': [
        {'y': data_dict[value],
         'type': 'scatter',
         'fill': 'tozeroy'}
    ]}


if __name__ == '__main__':
    app.run_server(debug=True)