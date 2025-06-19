# Genshin Impact Mechanic Analysis Project

[![GitHub Repository](https://img.shields.io/badge/Repository-Genshin_Mechanics_Analysis-blue?logo=github)](https://github.com/Redem-cat/genshin-mechanics-analysis)     [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![版本](https://img.shields.io/badge/Version-1.0.0-green)]() [![Python](https://img.shields.io/badge/Python-3.8+-blue)]() [![MATLAB](https://img.shields.io/badge/MATLAB-R2020a+-orange)]()
本项目包含对《原神》游戏系统的量化分析与模拟，包括角色培养、抽卡概率、敌人属性等内容。


## 项目结构

```
├── data/ # 原始数据文件
│ └── 圣遗物强化概率.xlsx # 圣遗物强化概率数据
├── docs/ # 项目文档和分析报告
│ ├── 原神抽卡概率计算.docx
│ ├── 原神量化研究.docx
│ └── 崩坏星穹铁道养成系统拆解.xlsx
├── source code/ # 源代码
│ ├── matlab/ # MATLAB 代码
│ │ ├── Monte_Carlo.m # 蒙特卡洛模拟
│ │ ├── element_mastery.m # 元素精通计算
│ │ └── five_star_pdf.m # 五星角色概率分析
│ └── python/ # Python 代码
│ ├── adventure_exp.py # 冒险等级经验计算
│ ├── character_exp_fitting.py # 角色经验拟合
│ ├── character_level_exp.py # 角色等级经验
│ ├── enemy_hp_fitting.py # 敌人血量拟合
│ ├── fitting.py # 数据拟合工具
│ ├── material_drop_rates.py # 材料掉落率分析
│ └── relic_enhancement_sim.py # 圣遗物强化模拟器（核心代码）
├── requirement.txt # Python 依赖库
└── readme.md # 本项目说明
```
---

## 开发信息

- **核心代码：** `source code/python/relic_enhancement_sim.py`（圣遗物强化模拟器）  
- **辅助代码：** 其他代码用于数据拟合与辅助分析



## 使用说明

### Python 环境配置

```bash
pip install -r requirement.txt
```

### 运行代码
运行圣遗物强化模拟器（核心代码）
```bash
python "source code/python/relic_enhancement_sim.py"
```
运行蒙特卡洛模拟
```matlab
run('source code/matlab/Monte_Carlo.m');
```

### 注意事项
Python 中文显示问题
为防止中文乱码，在 Python 脚本中添加以下代码：

```python
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']         # Windows 系统
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac 系统
plt.rcParams['axes.unicode_minus'] = False           # 正确显示负号
```
## 📜 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。
