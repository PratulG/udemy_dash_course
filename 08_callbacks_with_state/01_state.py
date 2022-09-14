import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64


# Instanciate the app
app = dash.Dash()

# Delfine the layout
app.layout = html.Div([
  dcc.Input(
    id = "number-in",
    value = 1,
    style = dict(
      fontsize = 24
    )
  ),
  html.Button(
    id = "submit-btn",
    n_clicks = 0,
    children = "Click me!!",
    style = dict(
      fontsize = 24
    )
  ),
  html.H1(
    id = "number-out"
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "number-out", component_property = "children"),
  Input(component_id = "submit-btn", component_property = "n_clicks"),
  State(component_id = "number-in", component_property = "value")
)
def multiply(n_clicks, number):
    return f"{number} was typed in and btn was clicked {n_clicks} times"

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
