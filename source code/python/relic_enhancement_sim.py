#本脚本文件重在展现计算与推导过程，其结果正确性以游戏本身为准
#本脚本文件只针对五星遗器，默认为均衡六。
#每天获取的开拓力数量为240，每个遗器副本消耗40体出金（即五星遗器），每次刷取出金期望2.100个。意味着每天可以刷12.6个五星遗器
#游戏中遗器的主词条获取概率：头部：生命值：100.00%
# 手部：攻击力：100.00%
# 躯干：生命%：20.00% 攻击%：20.00% 防御%：20.00% 暴击率：10.00% 暴击伤害：10.00% 治疗加成：10.00% 效果命中：10.00%
# 脚部：生命%：30.00% 攻击%：30.00 防御%：30.00% 速度：10.00%
# 位面球：生命%：12.33% 攻击%：12.33% 防御%：12.33% 属性伤：63.00%（火、冰、风、雷、物理、量子和虚数七种属性概率均分）
# 连结绳：生命%：26.67% 攻击%：26.67% 防御%：26.67% 击破特攻：15.00% 回能效率：5.00%
#其对应的成长数值成线性,即基础值+level*成长值，具体数值如下：
# 数据名称	属性	0级	15级	递增值
# HPDelta	生命值	112.9	705.6	39.51
# AttackDelta	攻击力	56.45	352.8	19.76
# DefenceDelta	防御力	-	-	-
# HPAddedRatio	生命值百分比	0.0691	0.432	0.0242
# AttackAddedRatio	攻击力百分比	0.0691	0.432	0.0242
# DefenceAddedRatio	防御力百分比	0.0864	0.54	0.0302
# CriticalChanceBase	暴击率	0.0518	0.324	0.0181
# CriticalDamageBase	暴击伤害	0.1037	0.648	0.0363
# BreakDamageAddedRatioBase	击破特攻	0.1037	0.648	0.0363
# StatusProbabilityBase	效果命中	0.0691	0.432	0.0242
# StatusResistanceBase	效果抵抗	-	-	-（意为防御力和效果抵抗主词条的遗器不存在）
# #（需要注意，防御力和防御力%是不一样的属性！）
# SpeedDelta	速度	4.03	25.03	1.4
# SPRatioBase	能量恢复速率	0.0311	0.1944	0.0109
# AddedRatio	属性伤害加成	0.0622	0.3888	0.0218
# HealRatioBase	治疗量提高	0.0553	0.3456	0.0194
# #崩铁副词条的抽取方式为“带权不放回抽取”，即服从超几何分布。副词条种类及其对应的抽取权重如下：
# 生命：125 # 攻击：125 # 防御：125 # 生命%：125 # 攻击%：125 # 防御%：125
# 效果命中：100 # 效果抵抗：100 # 击破特攻：100 # 暴击率：75 # 暴击伤害：75 # 速度：50
# 正常得到的五星遗器中，初始三词条与初始四词条的数量为 4:1，当副词条数量达到4便会进入到副词条升级的逻辑
# 在副词条数量小于4的时候，抽取副词条便会按照这些权重分配，这意味着初始三词条遗器有 4 次强化机会，初始四有 5 次强化机会
# 副词条在等级3、6、9、12、15级才会强化提升
# 4个副词条升级的概率是相等的，每次升级带来的加成会分为三档，三个挡位的数值之比为大致0.8：0.9：1.0
# 实际不同档位的强化数值如下：
# 速度：# 一档：2.0 二档：2.3 三档：2.6
# 生命# 一档：34 # 二档：38 # 三档：42
# 攻击：# 一档：17 # 二档：19 # 三档：21
# 防御：# 一档：17 # 二档：19 # 三档：21
# 生命%：# 一档：3.46% # 二档：3.89% # 三档：4.32%
# 攻击%：# 一档：3.46% # 二档：3.89% # 三档：4.32%
# 防御# 一档：4.32% # 二档：4.86% # 三档：5.40%
# 暴击率：# 一档：2.59% # 二档：2.92% # 三档：3.24%
# 暴击伤害# 一档：5.18% # 二档：5.83% # 三档：6.48%
# 效果命中：# 一档：3.46% # 二档：3.89% # 三档：4.32%
# 效果抵抗： # 一档：3.46% # 二档：3.89% # 三档：4.32%
# 击破特攻：# 一档：5.18% # 二档：5.83% # 三档：6.48%
# 需要注意的是最终遗器显示的属性需要直接舍弃掉百分位使用十分位
# 遗器强化到不同挡位所所需要的经验 +15 76000 +12 37000 +9 17500 +6 7500
# 可以看出从12级升级到15级的经验是巨量的
# 只考虑侵蚀隧洞和模拟宇宙获取的遗器，它们都有两种套装作为产物，两套套装的获取概率相等，各为50%。
# 侵蚀隧洞获取的外圈遗器有四个部位，出现概率均等，各为 25%；
# 模拟宇宙获取的内圈遗器有两个部位，出现概率均等，各为 50%。
# 实现：输入特定的0级遗器属性，预测出对它强化得到不同结果的概率，计算出刷取出该遗器相同部位和主词条的所需开拓力；
# 未来还可以考虑基于此文件实现输入特定的总遗器要求，计算出需要刷取出该标准的一套遗器需要费的开拓力。



import random
import copy
from itertools import permutations

# 基础配置
STAMINA_PER_RUN = 40
RELIC_PER_RUN = 2.1
BASE_HP = 2400
BASE_ATK = 1200
BASE_DEF = 900

# 副词条权重和强化数值
SUBSTAT_WEIGHTS = {
    'hp': 125, 'atk': 125, 'def': 125,
    'hp%': 125, 'atk%': 125, 'def%': 125,
    'effect_hit': 100, 'effect_res': 100, 'break_effect': 100,
    'crit_rate': 75, 'crit_dmg': 75, 'speed': 50
}

UPGRADE_VALUES = {
    'speed': [2.0, 2.3, 2.6],
    'hp': [34, 38, 42],
    'atk': [17, 19, 21],
    'def': [17, 19, 21],
    'hp%': [3.46, 3.89, 4.32],
    'atk%': [3.46, 3.89, 4.32],
    'def%': [4.32, 4.86, 5.40],
    'crit_rate': [2.59, 2.92, 3.24],
    'crit_dmg': [5.18, 5.83, 6.48],
    'effect_hit': [3.46, 3.89, 4.32],
    'effect_res': [3.46, 3.89, 4.32],
    'break_effect': [5.18, 5.83, 6.48]
}  #每次升级带来的加成会分为三档，三个挡位的数值之比为大致0.8：0.9：1.0

# 主词条成长数据（基础值, 每级成长）
MAIN_STAT_DATA = {
    'hp': (112.896, 39.5136),
    'atk': (56.4479, 19.7568),
    'hp%': (0.0691199, 0.024192),
    'atk%': (0.0691199, 0.024192),
    'def%': (0.086399, 0.03024),
    'crit_rate': (0.0518399, 0.018144),
    'crit_dmg': (0.1036799, 0.036288),
    'heal': (0.0552959, 0.019354),
    'effect_hit': (0.0691199, 0.024192),
    'speed': (4.03199, 1.4),
    'energy_regen': (0.0311039, 0.010886),
    'elemental_dmg': (0.0622079, 0.021773)
}

# 主词条概率分布（按部位）
MAIN_STAT_PROBS = {
    'head': {'hp': 1.0},
    'hands': {'atk': 1.0},
    'body': {
        'hp%': 0.2, 'atk%': 0.2, 'def%': 0.2,
        'crit_rate': 0.1, 'crit_dmg': 0.1,
        'heal': 0.1, 'effect_hit': 0.1
    },
    'feet': {
        'hp%': 0.3, 'atk%': 0.3, 'def%': 0.3,
        'speed': 0.1
    },
    'sphere': {
        'hp%': 12.33 / 100,
        'atk%': 12.33 / 100,
        'def%': 12.33 / 100,
        'elemental_dmg_1': 9 / 100,  # 火
        'elemental_dmg_2': 9 / 100,  # 冰
        'elemental_dmg_3': 9 / 100,  # 风
        'elemental_dmg_4': 9 / 100,  # 雷
        'elemental_dmg_5': 9 / 100,  # 物理
        'elemental_dmg_6': 9 / 100,  # 量子
        'elemental_dmg_7': 9 / 100  # 虚数
    },
    'rope': {
        'hp%': 26.67 / 100, 'atk%': 26.67 / 100, 'def%': 26.67 / 100,
        'break_effect': 15 / 100, 'energy_regen': 5 / 100
    }
}


class Relic:  # 一个遗器对象
    def __init__(self, set_type, slot, main_stat, substats, initial_slots, level=0):
        self.set_type = set_type  # '外圈'/'内圈'
        self.slot = slot  # 部位
        self.main_stat = main_stat
        self.substats = substats
        self.initial_slots = initial_slots
        self.level = level
        self.main_stat_value = self._calculate_main_stat()

    def _calculate_main_stat(self):
        """处理元素伤害类型的完整标识"""
        # 保留完整的元素伤害类型（如 elemental_dmg_7）
        if self.main_stat.startswith('elemental_dmg_'):
            base_stat = 'elemental_dmg'  # 统一使用基类型
        else:
            base_stat = self.main_stat

        if base_stat in MAIN_STAT_DATA:
            base, growth = MAIN_STAT_DATA[base_stat]
            return base + self.level * growth
        return 0.0

    def get_main_stat_actual(self):
        """获取主词条实际增益值，即将百分比乘基础值"""
        raw_value = self.main_stat_value

        if self.main_stat in ['hp', 'atk', 'def', 'speed', 'energy_regen', 'effect_hit', 'heal']:
            return raw_value
        elif self.main_stat.endswith('%'):
            if self.main_stat == 'hp%':
                return BASE_HP * raw_value
            elif self.main_stat == 'atk%':
                return BASE_ATK * raw_value
            elif self.main_stat == 'def%':
                return BASE_DEF * raw_value
        elif self.main_stat.startswith('elemental_dmg_'):
            return raw_value  # 元素伤害直接返回百分比
        return raw_value

# # 通过修改此处可以实现对副词条组合概率的计算
# def calculate_substat_prob(target_substats):
#     """计算指定副词条组合的出现概率"""
#     if len(target_substats) not in [3, 4]:
#         return 0.0
#
#     total = 0.0
#     for perm in permutations(target_substats):
#         prob = 1.0
#         remaining_weights = SUBSTAT_WEIGHTS.copy()
#         total_weight = sum(remaining_weights.values())
#
#         for stat in perm:
#             if stat not in remaining_weights:
#                 prob = 0.0
#                 break
#             prob *= remaining_weights[stat] / total_weight
#             total_weight -= remaining_weights[stat]
#             del remaining_weights[stat]
#
#         total += prob
#     return total


def get_main_stat_prob(slot, main_stat):
    """获取主词条出现概率"""
    probs = MAIN_STAT_PROBS.get(slot, {})

    # 处理元素伤害类型
    if slot == 'sphere' and main_stat.startswith('elemental_dmg_'):
        return probs.get(main_stat, 0)

    return probs.get(main_stat, 0)


def calculate_relic_probability(relic):
    """计算单个遗器的综合出现概率"""
    # 部位概率
    if relic.set_type == '外圈':
        slot_prob = 0.25 if relic.slot in ['head', 'hands', 'body', 'feet'] else 0
    else:
        slot_prob = 0.5 if relic.slot in ['sphere', 'rope'] else 0

    set_prob = 0.5 # 内外圈概率，这里假定刷内圈和外圈的概率是相等的，都是0.5

    main_stat_prob = get_main_stat_prob(relic.slot, relic.main_stat)  # 主词条概率

    # # 副词条概率
    # substat_prob = calculate_substat_prob(list(relic.substats.keys()))

    # 初始词条数概率
    # initial_slot_prob = 0.2 if relic.initial_slots == 4 else 0.8

    return slot_prob * main_stat_prob*set_prob

    # return slot_prob * main_stat_prob * substat_prob * initial_slot_prob


def calculate_stamina(relic):
    """计算所需开拓力"""
    prob = calculate_relic_probability(relic)
    return (1 / prob) * (STAMINA_PER_RUN / RELIC_PER_RUN) if prob != 0 else float('inf')


def simulate_upgrade(relic, target_level, simulations=10000):
    """修正后的强化逻辑，根据目标等级进行强化，考虑副词条强化条件和补充逻辑"""
    results = []
    for _ in range(simulations):
        simulated = copy.deepcopy(relic)
        current_level = simulated.level
        if current_level >= target_level:
            results.append(simulated)
            continue

        # 计算实际可以强化的次数（基于目标等级和当前等级）
        # 副词条强化发生在等级3、6、9、12、15
        # 强化次数为 floor((target_level - 1) / 3) - floor((current_level - 1) / 3)
        current_upgrades = (current_level - 1) // 3
        target_upgrades = (target_level - 1) // 3
        required_upgrades = max(0, target_upgrades - current_upgrades)

        # 处理初始3词条补充到4词条
        # 只有在目标等级 >=3 时才进行补充
        if simulated.initial_slots == 3 and target_level >=3:
            # 排除主词条属性和已有副词条
            main_stat_base = simulated.main_stat.split('_')[0] if simulated.main_stat.startswith(
                'elemental_dmg_') else simulated.main_stat
            available = [
                k for k in SUBSTAT_WEIGHTS
                if k not in simulated.substats and k != main_stat_base
            ]
            # 按权重随机选择新词条
            if available:
                chosen = random.choices(
                    available,
                    weights=[SUBSTAT_WEIGHTS[k] for k in available]
                )[0]
                simulated.substats[chosen] = random.choice(UPGRADE_VALUES[chosen])
            upgrades_remaining = 4  # 补充词条后剩余4次强化
        elif simulated.initial_slots ==3 and target_level <3:
            upgrades_remaining=0
        else:
            upgrades_remaining =5

        actual_upgrades = min(required_upgrades, upgrades_remaining)

        # 执行强化
        for _ in range(actual_upgrades):
            substats = list(simulated.substats.keys())
            if not substats:
                break
            chosen_sub = random.choice(substats)  # 均等概率选择
            if chosen_sub not in UPGRADE_VALUES:
                continue
            upgrade = random.choice(UPGRADE_VALUES[chosen_sub])
            simulated.substats[chosen_sub] = round(simulated.substats[chosen_sub] + upgrade, 2)

        # 更新等级和主词条值
        simulated.level = target_level
        simulated.main_stat_value = simulated._calculate_main_stat()

        # 处理显示数值到一位小数
        for k in simulated.substats:
            simulated.substats[k] = int(simulated.substats[k] * 10) / 10

        results.append(simulated)

    # 统计结果
    stats = {}
    # 遍历所有模拟结果，收集所有可能的副词条
    all_substats = set()
    for result in results:
        all_substats.update(result.substats.keys())

    # 为每个副词条计算最小值、最大值和平均值
    for substat in all_substats:
        values = [r.substats[substat] for r in results if substat in r.substats]
        if values:
            stats[substat] = {
                'min': min(values),
                'max': max(values),
                'avg': sum(values) / len(values)
            }
    return stats


def get_user_input():
    """获取用户输入的遗器属性"""
    print("请输入遗器的属性：")
    set_type = input("套装类型（外圈/内圈）：")
    slot = input("部位（head/hands/body/feet/sphere/rope）：")

    # 根据部位提示主词条选项
    main_stat_options = MAIN_STAT_PROBS.get(slot, {})
    print("该部位可能出现的主词条有：")
    for option in main_stat_options:
        print(f"- {option}")

    main_stat = input("主词条：")
    substats = {}
    initial_slots = int(input("初始词条数（3或4）："))

    # 提示副词条选项
    print("可用的副词条有：")
    for substat in UPGRADE_VALUES:
        print(f"- {substat}")

    # 根据初始词条数提示输入副词条
    if initial_slots == 3:
        print("请输入3个副词条及其数值（格式：词条1:数值1,词条2:数值2,词条3:数值3）：")
        substat_input = input()
        for pair in substat_input.split(','):
            key, value = pair.split(':')
            substats[key.strip()] = float(value.strip())
    else:
        print("请输入4个副词条及其数值（格式：词条1:数值1,词条2:数值2,词条3:数值3,词条4:数值4）：")
        substat_input = input()
        for pair in substat_input.split(','):
            key, value = pair.split(':')
            substats[key.strip()] = float(value.strip())

    # 获取用户想要强化到的等级
    target_level = int(input("想要强化到的等级（0-15）："))
    if target_level < 0 or target_level > 15:
        print("等级输入无效，设置为默认值15")
        target_level = 15

    return Relic(set_type, slot, main_stat, substats, initial_slots, level=0), target_level


# 交互部分主程序
# 交互部分主程序
if __name__ == "__main__":
    # 获取用户输入的遗器和目标等级
    relic, target_level = get_user_input()

    # 计算概率和体力
    prob = calculate_relic_probability(relic)
    stamina = calculate_stamina(relic)
    days = stamina / 240  # 每天240体力

    # 模拟强化结果
    sim_results_stats = simulate_upgrade(relic, target_level, 10000)

    # 找到模拟结果中的一个遗器用于显示最终数值
    # 由于 sim_results 是一个字典，存储的是副词条的统计信息，而不是强化后的遗器对象
    # 我们需要在 simulate_upgrade 函数中返回强化后的遗器对象列表
    # 因此，需要修改 simulate_upgrade 函数

    def simulate_upgrade(relic, target_level, simulations=10000):
        """修正后的强化逻辑，根据目标等级进行强化，考虑副词条强化条件和补充逻辑"""
        results = []
        relics_after_upgrade = []  # 用于存储强化后的遗器对象
        for _ in range(simulations):
            simulated = copy.deepcopy(relic)
            current_level = simulated.level
            if current_level >= target_level:
                relics_after_upgrade.append(simulated)
                continue

            # 计算实际可以强化的次数（基于目标等级和当前等级）
            # 副词条强化发生在等级3、6、9、12、15
            # 强化次数为 floor((target_level - 1) / 3) - floor((current_level - 1) / 3)
            current_upgrades = (current_level - 1) // 3
            target_upgrades = (target_level - 1) // 3
            required_upgrades = max(0, target_upgrades - current_upgrades)

            # 处理初始3词条补充到4词条
            # 只有在目标等级 >=3 时才进行补充
            if simulated.initial_slots == 3 and target_level >= 3:
                # 排除主词条属性和已有副词条
                main_stat_base = simulated.main_stat.split('_')[0] if simulated.main_stat.startswith(
                    'elemental_dmg_') else simulated.main_stat
                available = [
                    k for k in SUBSTAT_WEIGHTS
                    if k not in simulated.substats and k != main_stat_base
                ]
                # 按权重随机选择新词条
                if available:
                    chosen = random.choices(
                        available,
                        weights=[SUBSTAT_WEIGHTS[k] for k in available]
                    )[0]
                    simulated.substats[chosen] = random.choice(UPGRADE_VALUES[chosen])
                upgrades_remaining = 4  # 补充词条后剩余4次强化
            elif simulated.initial_slots == 3 and target_level < 3:
                upgrades_remaining = 0
            else:
                upgrades_remaining = 5

            actual_upgrades = min(required_upgrades, upgrades_remaining)

            # 执行强化
            for _ in range(actual_upgrades):
                substats = list(simulated.substats.keys())
                if not substats:
                    break
                chosen_sub = random.choice(substats)  # 均等概率选择
                if chosen_sub not in UPGRADE_VALUES:
                    continue
                upgrade = random.choice(UPGRADE_VALUES[chosen_sub])
                simulated.substats[chosen_sub] = round(simulated.substats[chosen_sub] + upgrade, 2)

            # 更新等级和主词条值
            simulated.level = target_level
            simulated.main_stat_value = simulated._calculate_main_stat()

            # 处理显示数值
            for k in simulated.substats:
                simulated.substats[k] = int(simulated.substats[k] * 10) / 10

            relics_after_upgrade.append(simulated)

        # 统计结果
        stats = {}
        # 遍历所有模拟结果，收集所有可能的副词条
        all_substats = set()
        for result in relics_after_upgrade:
            all_substats.update(result.substats.keys())

        # 为每个副词条计算最小值、最大值和平均值
        for substat in all_substats:
            values = [r.substats[substat] for r in relics_after_upgrade if substat in r.substats]
            if values:
                stats[substat] = {
                    'min': min(values),
                    'max': max(values),
                    'avg': sum(values) / len(values)
                }
        return stats, relics_after_upgrade

    # 模拟强化结果
    sim_results_stats, relics_after_upgrade = simulate_upgrade(relic, target_level, 10000)

    # 找到模拟结果中的一个遗器用于显示最终数值
    final_relic = relics_after_upgrade[0] if relics_after_upgrade else relic

    print("\n=== 计算结果 ===")
    print(f"刷出和该遗器相同主词条和部位遗器概率: {prob:.8f}")
    print(f"预计开拓力: {stamina:.2f}")
    print(f"预计需要天数: {days:.2f} 天")
    print(f"主词条最终数值: {final_relic.main_stat_value:.4f}")
    print(f"实际主词条增益: {final_relic.get_main_stat_actual() * 100:.2f}%")

    print("\n副词条强化预测:")
    for stat, data in sim_results_stats.items():
        print(f"{stat}: {data['min']}~{data['max']} (平均{data['avg']:.2f})")
    input("按任意键退出...")