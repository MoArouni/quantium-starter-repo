import pandas
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# 1. Setup & Data
DATA_PATH = "./formatted_data.csv"
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="Date") # Match your CSV column name capital 'D'

dash_app = Dash(__name__)

# 2. Components
header = html.H1("Pink Morsel Visualizer", id="header")

visualization = dcc.Graph(id="visualization")

region_picker = dcc.RadioItems(
    options=["north", "east", "south", "west", "all"],
    value="all",
    id="region_picker",
    inline=True
)

# 3. Layout
dash_app.layout = html.Div([
    header,
    region_picker,
    visualization
], style={"textAlign": "center"})

# 4. Callback
@dash_app.callback(
    Output("visualization", "figure"),
    Input("region_picker", "value")
)
def update_graph(region):
    if region == "all":
        df = data
    else:
        df = data[data["Region"].str.lower() == region] # Matching case
    
    fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales")
    return fig

if __name__ == '__main__':
    dash_app.run_server(debug=True)