clear all,clc;
%% 初始化

P = zeros(90, 90); 
for i = 0 : 88
    P(i + 1, 1) = 0.006 + 0.06 * max(0, i - 72);  %73抽后出金概率将会线性增加
    P(i + 1, i + 2) = 1 - P(i + 1, 1);
end
P(90, 1) = 1;

%% 第k抽出金的概率

p = zeros(1, 90); 
e = 0;  %e代表期望
for k = 1 : 90
    p(1, k) = P(k, 1);
    for i = 0 : k - 2
        p(1, k) = p(1, k) * P(i + 1, i + 2);
    end
    e = e + k * p(1, k);
end

%% 综合概率（含保底）计算
PP = P^10000;
pi = PP(1, :); % 因MATLAB向量从1开始，因此所有指标+1
prob2 = pi(1, 1);
prob3 = 0;
for i = 0 : 89
    prob3 = prob3 + pi(1, i + 1) * P(i + 1, 1);
end

%% 输出结果

figure;
plot(p, "LineWidth", 1);
title('第k抽出金概率')
grid on;
fprintf('首次出金期望抽数为：%f\n', e);
fprintf('综合概率（含保底）为：%f\n', prob3);
