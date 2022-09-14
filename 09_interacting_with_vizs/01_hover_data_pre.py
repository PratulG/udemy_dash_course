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
import json


# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/PratulG/udemy_dash_course/master/07_interactive_components/wheels.csv")

# Instanciate the app
app = dash.Dash()

# Build the layout
app.layout = html.Div([
  html.Div(
    dcc.Graph(
      id = "wheels-plot",
      figure = {
        "data": [
          go.Scatter(
            x = df["color"],
            y = df["wheels"],
            dy = 1,
            mode = "markers",
            marker = dict(
              size = 15
            )
          )
        ],
        "layout": go.Layout(
          title = "Hover Data",
          hovermode = "closest" 
        )
      }
    ),
    style = dict(
      width = "30%",
      float = "left"
    )
  ),
  html.Div(
    html.Pre(
      id = "hover-data",
      style = dict(
        paddingtop = 35
      )
    ),
    style = dict(
      width = "30%"
    )
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "hover-data", component_property = "children"),
  Input(component_id = "wheels-plot", component_property = "hoverData")
)
def callback_image(hoverData):
    return json.dumps(hoverData, indent = 2)




app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
