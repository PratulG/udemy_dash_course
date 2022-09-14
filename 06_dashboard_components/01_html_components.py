import pandas as pd
import numpy as np
import plotly.express as px
import string
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
from dash import html,dcc

app = dash.Dash()

# Define style

# Define the layout
app.layout = html.Div(
  children = [
    "This is a div",
    html.Div(
      children = [
        "This is an inner div"
      ],
      style = dict(
        color = "red",
        border = "2px solid red"
      )
    ),
    html.Div(
      children = [
        "Another inner div!"
      ],
      style = dict(
        color = "blue",
        border = "2px solid blue"
      )
    )
  ],
  style = dict(
    color = "green",
    border = "2px solid green"
  )
)

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
