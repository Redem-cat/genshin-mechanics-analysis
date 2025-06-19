Genshin Impact Mechanic Analysis Project
本项目包含对《原神》游戏系统的量化分析和模拟，包括角色培养、抽卡概率、敌人属性等分析。

项目结构
text
.
├── data/ # 原始数据文件
│   └── 圣遗物强化概率.xlsx # 圣遗物强化概率数据
├── docs/ # 项目文档和分析报告
│   ├── 原神抽卡概率计算.docx # 抽卡概率研究
│   ├── 原神量化研究.docx # 游戏数值量化研究
│   └── 崩坏星穹铁道养成系统拆解.xlsx # 崩坏星穹铁道系统拆解
├── source code/ # 源代码
│   ├── matlab/ # MATLAB代码
│   │   ├── Monte_Carlo.m # 蒙特卡洛模拟
│   │   ├── element_mastery.m # 元素精通计算
│   │   └── five_star_pdf.m # 五星角色概率分析
│   └── python/ # Python代码
│       ├── adventure_exp.py # 冒险等级经验计算
│       ├── character_exp_fitting.py # 角色经验拟合
│       ├── character_level_exp.py # 角色等级经验
│       ├── enemy_hp_fitting.py # 敌人血量拟合
│       ├── fitting.py # 数据拟合工具
│       ├── material_drop_rates.py # 材料掉落率分析
│       └── relic_enhancement_sim.py # 遗器强化模拟器(核心代码)
├── requirement.txt # Python依赖库
└── readme.md # 本项目说明
开发信息
核心代码: source code/python/relic_enhancement_sim.py (遗器强化模拟器)

辅助代码: 其他代码主要用于数据拟合和辅助分析

使用说明
Python环境配置:

bash
pip install -r requirement.txt
运行遗器强化模拟器(核心代码):

bash
python source code/python/relic_enhancement_sim.py
MATLAB代码:

matlab
% 示例:运行蒙特卡洛模拟
run('source code/matlab/Monte_Carlo.m');
Python中文显示问题:
在Python脚本中添加以下代码以正确显示中文:

python
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac系统
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号