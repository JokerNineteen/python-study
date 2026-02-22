# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import alphas

days = list(range(1, 31))
sales = [100, 120, 180, 200, 220, 240, 260, 280, 300, 320,
         340, 360, 380, 400, 420, 440, 460, 480, 500, 520,
         540, 560, 580, 600, 620, 640, 660, 680, 700, 720,]

# 创建图形对象
plt.figure(figsize=(10, 6))

# 绘制柱状图
plt.bar(days, sales, color='lightblue',alpha = 0.7, label='Daily Sales')

plt.plot(days, sales, color='blue', linestyle='-', marker='o', linewidth=2, label='Daily Sales')
plt.title('Daily Sales for a Month')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.show()
