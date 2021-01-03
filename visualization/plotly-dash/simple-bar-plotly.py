"""
plotly chart
"""

import plotly.graph_objs as go

fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('first_figure.html', auto_open=True)


