% 定义精通值范围
em = 0:1:2000; % 精通值从 0 到 2000

% 传统增幅反应精通乘区
traditional = 1 + (2.78 * em) ./ (em + 1400);

% 激化反应精通乘区
catalyze = 1 + (5 * em) ./ (em + 1200);

% 剧变反应精通乘区
transformation = 1 + (16 * em) ./ (em + 2000);

% 绘制图形
figure;
plot(em, traditional, 'b', 'LineWidth', 2);
hold on;
plot(em, catalyze, 'r', 'LineWidth', 2);
plot(em, transformation, 'g', 'LineWidth', 2);
hold off;

% 添加标题和标签
title('精通乘区函数比较');
xlabel('精通值 (em)');
ylabel('乘区值');
legend('传统增幅反应', '激化反应', '剧变反应');
grid on;