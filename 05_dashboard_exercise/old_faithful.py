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

# Load the data
df = pd.read_csv("OldFaithful.csv")

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
  dcc.Graph(
    id = "old_faithful",
    figure = {
      "data": [
        go.Scatter(
          x = df["X"],
          y = df["Y"],
          mode = "markers"
        )
      ],
      "layout": go.Layout(
        title = "Old Faithful Eruptions",
        xaxis = {
          "title": "Duration (in minutes)"
        },
        yaxis = {
          "title": "Interval (in minutes)"
        },
        hovermode = "closest"
      )
    }
  )
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
