import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MaxNLocator
# 设置 Matplotlib 支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False   # 正确显示负号

# 数据
levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
yields = [16.67, 18.06, 19.45, 20.84, 22.23, 23.62, 25.01, 26.40, 50.00, 52.50, 55.00, 57.50, 80.00, 83.33, 86.67, 90.00, 93.33, 96.67,100.00]


# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(levels, yields, marker='o', color='orange', label='相对收益')

# 添加数据标签
for i, txt in enumerate(yields):
    plt.annotate(f'{txt}%', (levels[i], yields[i]), textcoords="offset points", xytext=(0,10), ha='center')

# 图表标题和标签
plt.title('通用突破材料掉落收益', fontsize=16)
plt.xlabel('掉落等级', fontsize=12)
plt.ylabel('相对收益 (%)', fontsize=12)

# 设置横轴和纵轴的刻度为整数
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

# 显示网格和图例
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 显示图表
plt.show()