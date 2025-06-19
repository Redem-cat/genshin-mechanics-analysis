import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.font_manager import FontProperties

# 原始数据
x_data = np.array([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
y_data = np.array([17.165, 22.645, 34.143, 53.748, 80.584, 108.409, 136.292, 169.106, 207.382,
                   256.063, 323.601, 398.600, 492.884, 624.443, 765.640, 914.229, 1077.443, 1253.835, 1446.853])

# 定义拟合函数
# 1. 二次函数
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# 2. 指数函数
def exponential_func(x, a, b):
    return a * np.exp(b * x)

# 3. 幂函数
def power_func(x, a, b):
    return a * x**b

# 拟合二次函数
popt_quad, _ = curve_fit(quadratic_func, x_data, y_data)
print("二次函数拟合参数 (a, b, c):", popt_quad)

# 拟合指数函数
popt_exp, _ = curve_fit(exponential_func, x_data, y_data, p0=(1, 0.1))
print("指数函数拟合参数 (a, b):", popt_exp)

# 拟合幂函数
popt_power, _ = curve_fit(power_func, x_data, y_data, p0=(1, 1))
print("幂函数拟合参数 (a, b):", popt_power)

# 计算拟合值
y_quad = quadratic_func(x_data, *popt_quad)
y_exp = exponential_func(x_data, *popt_exp)
y_power = power_func(x_data, *popt_power)

# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  # 使用黑体字体

# 可视化结果
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="原始数据", color="blue")
plt.plot(x_data, y_quad, label="二次函数拟合", color="red", linestyle="--")
plt.plot(x_data, y_exp, label="指数函数拟合", color="green", linestyle="-.")
plt.plot(x_data, y_power, label="幂函数拟合", color="purple", linestyle=":")
plt.xlabel("X", fontproperties=font)
plt.ylabel("Y", fontproperties=font)
plt.title("数据拟合结果", fontproperties=font)
plt.legend(prop=font)  # 设置图例字体
plt.grid(True)
plt.show()