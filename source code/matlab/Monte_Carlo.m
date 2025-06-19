clear all, clc;

%% 参数设置
num_simulations = 100000;   % 模拟次数（10万次）
max_pulls = 200;            % 最大抽卡次数（200抽）
P_4star = 0.051;           % 四星物品基础概率（5.1%）
P_4star_character = 0.5;   % 四星物品中角色的概率（50%）
P_UP = 0.5;                % 四星角色中UP角色的概率（50%）
num_UP = 3;                % UP角色数量

% 初始化结果存储
results = zeros(num_simulations, 1); % 记录首次抽到目标UP角色的抽数
up_guarantee = false;               % UP保底触发标志（初始为false）

% 初始化统计变量
total_4star = 0;           % 所有四星物品的次数
total_4star_roles = 0;     % 四星角色的次数
total_up_4star = 0;        % UP四星角色的次数

%% 蒙特卡洛模拟
for sim = 1 : num_simulations
    counter_4star = 0;      % 连续未抽到四星的计数器（用于10抽保底）
    up_guarantee = false;   % 重置UP保底标志
    found = false;          % 是否抽到目标UP角色
    
    for pull = 1 : max_pulls
        
        % 判断是否触发四星保底（9抽50%，10抽100%）
        if counter_4star == 8
            is_4star = (rand() < 0.67); % 调整第九抽的概率
        elseif counter_4star == 9
            is_4star = true; % 第十抽100%概率
        else
            % 非保底时按基础概率判定
            is_4star = (rand() < P_4star);
        end
        
        if is_4star
            total_4star = total_4star + 1; % 统计四星次数
            counter_4star = 0; % 重置四星保底计数器
            
            % 判定是否为四星角色（50%概率）
            is_character = (rand() < P_4star_character);
            if is_character
                total_4star_roles = total_4star_roles + 1; % 统计四星角色次数
                
                % 判定是否为UP角色
                if up_guarantee
                    % UP保底触发，必出UP角色
                    up_index = randi(num_UP);
                    up_guarantee = false; % 重置保底标志
                    is_up = true;
                else
                    % 非保底时，50%概率为UP角色
                    is_up = (rand() < P_UP);
                    if is_up
                        up_index = randi(num_UP);
                    else
                        % 非UP角色，触发下次保底
                        up_guarantee = true;
                        is_up = false;
                    end
                end
                
                % 统计UP四星次数
                if is_up
                    total_up_4star = total_up_4star + 1;
                end
                
                if  ~found
                    results(sim) = pull;
                    found = true;
                end
            end
        else
            counter_4star = counter_4star + 1;
        end
    end
    
    if ~found
        results(sim) = Inf; % 记录未抽到的情况
    end
end

%% 数据分析
% 过滤有效结果（抽到目标UP的抽数）
valid_results = results(results ~= Inf);
num_success = length(valid_results);

% 计算首次抽到目标UP的概率分布（PDF）
prob_density = zeros(1, max_pulls);
for k = 1 : max_pulls
    prob_density(k) = sum(valid_results == k) / num_simulations;
end

% 计算累积分布函数（CDF）
prob_distribution = cumsum(prob_density);

% 计算期望值和置信区间
expectation = mean(valid_results);
quantile_90 = quantile(valid_results, 0.9);

% 计算四星综合概率和UP占比
p_4star_sim = total_4star / (num_simulations * max_pulls);
if total_4star_roles > 0
    up_ratio_sim = total_up_4star / total_4star_roles;
else
    up_ratio_sim = 0;
end
up_ratio_theory = 2/3; % 理论值

%% 绘制图形
figure;

% PDF
subplot(2,1,1);
plot(1:max_pulls, prob_density, 'LineWidth', 1.5);
xlabel('抽卡次数');
ylabel('概率密度');
title('首次抽到目标UP四星的概率密度函数（PDF）');
grid on;

% CDF
subplot(2,1,2);
plot(1:max_pulls, prob_distribution, 'LineWidth', 1.5);
xlabel('抽卡次数');
ylabel('累积概率');
title('首次抽到目标UP四星的概率分布函数（CDF）');
ylim([0 1]);
grid on;

%% 输出结果
fprintf('90%% 玩家在 %d 抽内抽到目标UP四星\n', quantile_90);
fprintf('200抽出目标四星总成功率：%.2f%%\n', num_success / num_simulations * 100);
fprintf('\n验证部分：\n');
fprintf('四星物品综合概率：%.2f%% (理论13%%)\n', p_4star_sim*100);
fprintf('UP四星角色模拟占比：%.2f%%\n', up_ratio_sim*100);