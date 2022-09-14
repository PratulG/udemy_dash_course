import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64


# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/PratulG/udemy_dash_course/master/07_interactive_components/wheels.csv")

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return "data:image/png;base64,{}".format(encoded.decode())

# Instanciate the app
app = dash.Dash()

# Delfine the layout
app.layout = html.Div(
  children = [
    dcc.RadioItems(
      id = "wheels",
      options = [{"label": str(i), "value": i} for i in df["wheels"].unique()],
      value = 1
    ),
    html.Div(
      id = "wheels-output"
    ),
    html.Hr(),
    dcc.RadioItems(
      id = "colors",
      options = [{"label": str(i), "value": i} for i in df["color"].unique()],
      value = "blue"
    ),
    html.Div(
      id = "colors-output"
    ),
    html.Hr(),
    html.Img(
      id = "display-image",
      src = "children",
      height = 300
    )
  ],
  style = dict(
    fontfamily = "helvatica",
    fontsize = 18
  )
)

# Build the callbacks
@app.callback(
  Output(component_id = "wheels-output", component_property = "children"),
  Input(component_id = "wheels", component_property = "value")
)
def callback_a(wheels):
    return f"You chose {wheels}"

@app.callback(
  Output(component_id = "colors-output", component_property = "children"),
  Input(component_id = "colors", component_property = "value")
)
def callback_b(colors):
    return f"You chose {colors}"

@app.callback(
  Output(component_id = "display-image", component_property = "src"),
  Input(component_id = "wheels", component_property = "value"),
  Input(component_id = "colors", component_property = "value")
)
def callback_image(wheels, color):
    path = "images/"
    encoded = encode_image(
    path + df[(df["wheels"] == wheels) & (df["color"] == color)]["image"].values[0]
  )
    return encoded


app.run_server(debug=True, use_reloader=False, port = 8050)  # Turn off reloader if inside Jupyter
