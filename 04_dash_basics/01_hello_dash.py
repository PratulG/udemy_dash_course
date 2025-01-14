import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
# Define de layout
app.layout = html.Div([
  html.H1("Hello Dash!")
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
