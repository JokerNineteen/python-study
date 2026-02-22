# -*- coding: utf-8 -*-
from pyecharts.charts import Bar, Line
from pyecharts import options as opts

days = list(range(1, 31))
sales = [100, 120, 180, 200, 220, 240, 260, 280, 300, 320,
         340, 360, 380, 400, 420, 440, 460, 480, 500, 520,
         540, 560, 580, 600, 620, 640, 660, 680, 700, 720,]

bar = (
    Bar()
    .add_xaxis(days)
    .add_yaxis("Daily Sales", sales)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Daily Sales for a Month"),
        xaxis_opts=opts.AxisOpts(name="Day"),
        yaxis_opts=opts.AxisOpts(name="Sales"),
        legend_opts=opts.LegendOpts(legend_icon="circle"),
    )
)

line = (
    Line()
    .add_xaxis(days)
    .add_yaxis("Daily Sales", sales)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Daily Sales for a Month"),
        xaxis_opts=opts.AxisOpts(name="Day"),
        yaxis_opts=opts.AxisOpts(name="Sales"),
        legend_opts=opts.LegendOpts(legend_icon="circle"),
    )
)

bar.overlap(line)
bar.render("bar_chart.html")

# bar.render_notebook()