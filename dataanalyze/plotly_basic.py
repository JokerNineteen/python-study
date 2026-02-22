# -*- coding: utf-8 -*-
import plotly.graph_objects as go

days = list(range(1, 31))
sales = [100, 120, 180, 200, 220, 240, 260, 280, 300, 320,
         340, 360, 380, 400, 420, 440, 460, 480, 500, 520,
         540, 560, 580, 600, 620, 640, 660, 680, 700, 720,]

bar = go.Bar(
    x=days,
    y=sales,
    name='Daily Sales',
    marker=dict(color='rgb(55, 83, 109)'),
    opacity=0.7
    )

line = go.Scatter(
    x=days,
    y=sales,
    name='Daily Sales',
    line=dict(color='rgb(26, 118, 255)', width=2),
    )

fig = go.Figure(data=[bar, line])

fig.update_layout(
    title='Daily Sales for a Month',
    xaxis_title='Day',
    yaxis_title='Sales',
    legend_title='Legend',
    )

fig.show()