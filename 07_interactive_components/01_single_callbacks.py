from os import stat_result
import pandas as pd
import numpy as np
import plotly.express as px
import string
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.graph_objects as go # or plotly.express as px
from dash.dependencies import Input, Output

fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
from dash import html,dcc

app = dash.Dash()

# Define style

# Delfine the layout
app.layout = html.Div([
  dcc.Input(
    id = "input-id",
    value = "Initial text",
    type = "text"
  ),
  html.Div(
    id = "output-div"
  )
])

# Build the callbacks
@app.callback(
  Output(component_id = "output-div", component_property = "children"),
  Input(component_id = "input-id", component_property = "value")
)
def update_text(input_text):
    return f"You entered: {input_text}"


app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
