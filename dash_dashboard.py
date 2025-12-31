"""
SpaceX Falcon 9 Capstone Project
Plotly Dash Dashboard (Template)
This file is for educational and demonstration purposes.
"""

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load dataset (placeholder)
# Replace with actual dataset path when running the project
df = pd.DataFrame({
    "Launch_Site": ["CCAFS", "KSC", "VAFB"],
    "Success": [20, 15, 10],
    "Failure": [5, 3, 2]
})

# Create Dash app
app = dash.Dash(__name__)

# Simple bar chart (example)
fig = px.bar(
    df,
    x="Launch_Site",
    y=["Success", "Failure"],
    title="Launch Success by Site"
)

# Layout
app.layout = html.Div(children=[
    html.H1("SpaceX Falcon 9 Launch Dashboard"),

    html.P(
        "This dashboard provides an interactive overview of launch outcomes "
        "across different SpaceX launch sites."
    ),

    dcc.Graph(figure=fig)
])

# Run server
if __name__ == "__main__":
    app.run_server(debug=True)
