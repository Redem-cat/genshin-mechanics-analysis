import matplotlib.pyplot as plt

# 冒险等级数据
adventure_levels = list(range(1, 61))

# 所需总和数据
total_needed = [
    0, 375, 875, 1500, 2225, 3075, 4025, 5100, 6300, 7600,
    9025, 10550, 12200, 13975, 15850, 17850, 20225, 22725, 25350, 28125,
    30950, 34375, 38100, 42100, 46400, 50975, 55850, 61000, 66450, 72175,
    78200, 84500, 91100, 98000, 105175, 112650, 120400, 128450, 136775, 145400,
    155950, 167475, 179950, 193400, 207800, 223150, 239475, 256750, 275000, 294200,
    320600, 349400, 380600, 414200, 450200, 682550, 941500, 1227250, 1540075, 1880200
]

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(adventure_levels, total_needed, marker='o')

# 添加标题和标签
plt.title('Adventure Level Upgrade Chart')
plt.xlabel('Adventure Level')
plt.ylabel('Total Needed')

# 显示网格
plt.grid(True)

# 显示图表
plt.show()