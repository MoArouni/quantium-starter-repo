import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# 1. Load the formatted data
df = pd.read_csv("formatted_data.csv")

# 2. Sort data by date (Crucial for line charts so they don't look like scribbles!)
df = df.sort_values(by="Date")

# 3. Initialize the Dash app
app = Dash(__name__)

# 4. Create the line chart using Plotly Express
# This answers the "Line chart with axis labels" requirement
fig = px.line(
    df, 
    x="Date", 
    y="Sales", 
    title="Pink Morsel Sales Over Time",
    labels={"Sales": "Total Sales ($)", "Date": "Transaction Date"}
)

# 5. Define the layout
# This hits the "Header" and "Visualiser" requirements
app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales Visualizer',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 6. Run the app
if __name__ == '__main__':
    app.run(debug=True)