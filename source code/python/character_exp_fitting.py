import numpy as np
from scipy.optimize import curve_fit

# 等级数据
levels = np.arange(1, 91)

# 总和数据
total_sum = [
    0, 1000, 2325, 4025, 6175, 8800, 11950, 15675, 20025, 25025,
    30725, 37175, 44400, 52450, 61375, 71200, 81950, 93675, 106400, 120175,
    135050, 151850, 169850, 189100, 209650, 231525, 254775, 279425, 305525, 333100,
    362200, 392850, 425100, 458975, 494525, 531775, 570750, 611500, 654075, 698500,
    744800, 795425, 848125, 902900, 959800, 1018875, 1080150, 1143675, 1209475, 1277600,
    1348075, 1424575, 1503625, 1585275, 1669550, 1756500, 1846150, 1938550, 2033725, 2131725,
    2232600, 2341550, 2453600, 2568775, 2687100, 2808625, 2933400, 3061475, 3192875, 3327650,
    3465825, 3614525, 3766900, 3922975, 4082800, 4246400, 4413825, 4585125, 4760350, 4939525,
    5155750, 5398775, 5671875, 5974975, 6311775, 6684725, 7097150, 7554575, 8062200, 8624850
]

# 定义拟合函数
def linear_func(x, a, b):
    """线性函数：y = a * x + b"""
    return a * x + b

def quadratic_func(x, a, b, c):
    """二次函数：y = a * x^2 + b * x + c"""
    return a * x**2 + b * x + c

def exponential_func(x, a, b, c):
    """指数函数：y = a * exp(b * x) + c"""
    return a * np.exp(b * x) + c

def power_func(x, a, b, c):
    """幂函数：y = a * x^b + c"""
    return a * np.power(x, b) + c

def cubic_func(x, a, b, c, d):
    """三次函数：y = a * x^3 + b * x^2 + c * x + d"""
    return a * x**3 + b * x**2 + c * x + d

# 计算均方误差 (MSE)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# 计算决定系数 (R²)
def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

# 对 total_sum 进行拟合
data = total_sum
x_data = levels

# 尝试多种函数
functions = {
    "线性函数": linear_func,
    "二次函数": quadratic_func,
    "指数函数": exponential_func,
    "幂函数": power_func,
    "三次函数": cubic_func
}

best_fit = None
best_mse = float('inf')
best_r2 = -float('inf')
best_func_name = ""
best_params = None

for func_name, func in functions.items():
    try:
        params, _ = curve_fit(func, x_data, data, maxfev=10000)  # 增加 maxfev 以避免拟合失败
        y_pred = func(x_data, *params)
        current_mse = mse(data, y_pred)
        current_r2 = r_squared(data, y_pred)

        print(f"{func_name} 拟合结果:")
        print(f"  参数: {params}")
        print(f"  MSE: {current_mse}")
        print(f"  R²: {current_r2}")
        print()

        if current_mse < best_mse:
            best_mse = current_mse
            best_r2 = current_r2
            best_func_name = func_name
            best_params = params
            best_fit = func
    except Exception as e:
        print(f"{func_name} 拟合失败: {e}")

# 输出最佳拟合结果
print("\n最佳拟合结果:")
print(f"  函数: {best_func_name}")
print(f"  参数: {best_params}")
print(f"  MSE: {best_mse}")
print(f"  R²: {best_r2}")

# 最佳拟合函数表达式
if best_func_name == "线性函数":
    print(f"  表达式: y = {best_params[0]} * x + {best_params[1]}")
elif best_func_name == "二次函数":
    print(f"  表达式: y = {best_params[0]} * x^2 + {best_params[1]} * x + {best_params[2]}")
elif best_func_name == "指数函数":
    print(f"  表达式: y = {best_params[0]} * exp({best_params[1]} * x) + {best_params[2]}")
elif best_func_name == "幂函数":
    print(f"  表达式: y = {best_params[0]} * x^{best_params[1]} + {best_params[2]}")
elif best_func_name == "三次函数":
    print(f"  表达式: y = {best_params[0]} * x^3 + {best_params[1]} * x^2 + {best_params[2]} * x + {best_params[3]}")