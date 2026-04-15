import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# 1. Load and Sort Data
df = pd.read_csv("formatted_data.csv")
df = df.sort_values(by="Date")

# 2. Initialize the Dash app
app = Dash(__name__)

# 3. Define the Layout (The "Look")
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'fontFamily': 'sans-serif', 'padding': '20px'}, children=[
    
    # Header Styling
    html.H1(
        children='Pink Morsel Sales Visualizer',
        style={
            'textAlign': 'center', 
            'color': '#2c3e50', 
            'marginBottom': '30px',
            'borderBottom': '2px solid #2c3e50',
            'paddingBottom': '10px'
        }
    ),

    # Radio Button Container
    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',  # Default selection
            inline=True,   # Puts buttons in a row
            inputStyle={"margin-left": "15px", "margin-right": "5px"}
        ),
    ]),

    # Graph Container
    html.Div(style={'backgroundColor': 'white', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'}, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

# 4. The Callback (The "Logic")
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-filter', 'value')]
)
def update_graph(region):
    # Filter data based on choice
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == region]

    # Create the updated figure
    fig = px.line(
        filtered_df, 
        x="Date", 
        y="Sales", 
        title=f"Pink Morsel Sales: {region.capitalize()} Region",
        template="plotly_white" # Makes the chart look cleaner
    )

    # Customize the chart look
    fig.update_layout(
        transition_duration=500, # Smooth animation when switching regions
        font_color="#2c3e50",
        title_font_size=20
    )

    return fig

# 5. Run the app
if __name__ == '__main__':
    app.run(debug=True)