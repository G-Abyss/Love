% 💕 Gen式双向奔赴理论 - 用数学证明爱情的力量
% 警告：本代码仅供娱乐，使用前请确保有一颗相信爱情的心 ❤️

% 定义爱情的时间轴（从-2到2，就像从陌生到熟悉的过程）
x = -2:0.1:2;
nImages = length(x);  % 记录爱情路上的每一个瞬间

% 为三个不同的"爱情状态"准备存储空间
im1 = cell(size(x));  % 存储单方面付出的结果（没有灵魂）
im2 = cell(size(x));  % 存储另一个单方面付出的结果（没有内涵）
im3 = cell(size(x));  % 存储双向奔赴的完美结果（有灵魂有内涵）

% 核心理论：两个物体的运动方程
% L_O：代表"Love"中的"L"，象征着爱情的上半部分
L_O = sqrt(1-(abs(x)-1).^2);
% V_E：代表"Love"中的"E"，象征着爱情的下半部分
V_E = -3*sqrt(1-sqrt(abs(x)/2));

% 开始模拟爱情的发展过程，每一帧都是爱情路上的一个瞬间
for j = 1:nImages
    % 场景1：单方面付出的悲剧（L_O独自努力）
    % 这就像一个人单方面追求，结果...你懂的 😢
    fig = figure('Visible', 'off');
    set(gcf,'unit','normalized','position',[0.2,0.0,0.70,0.3]);
    plot(x(1:j),L_O(1:j),Color='b',LineWidth=4);  % 蓝色代表忧郁
    axis([-2 2 0 1]);
    hold on;
    plot(x(j),L_O(j),'*');  % 当前时刻的位置，就像单恋者的心
    xlabel('x')
    ylabel('L_O')
    frame = getframe(fig);
    im1{j} = frame2im(frame);
    close;

    % 场景2：另一个单方面付出的悲剧（V_E独自努力）
    % 这就像另一个人也在单方面追求，结果...还是悲剧 😭
    fig = figure('Visible', 'off');
    set(gcf,'unit','normalized','position',[0.2,0.0,0.70,0.9]);
    plot(x(1:j),V_E(1:j),Color='g',LineWidth=4);  % 绿色代表...嗯，嫉妒？
    axis([-2 2 -3 0]);
    hold on;
    plot(x(j),V_E(j),'*');  % 另一个单恋者的心
    xlabel('x')
    ylabel('V_E')
    frame = getframe(fig);
    im2{j} = frame2im(frame);
    disp("Figure"+num2str(j)+",Done");  % 进度提示：爱情路上第j步完成
    close;

    % 场景3：双向奔赴的完美结局！💕
    % 这就是传说中的"双向奔赴"，两个人都努力，结果...完美！
    fig = figure('Visible', 'off');
    set(gcf,'unit','normalized','position',[0.2,0.0,0.70,1.2]);
    plot(x(1:j),L_O(1:j),Color='r',LineWidth=4);  % 红色代表热情和爱情
    axis([-2 2 -3 1]);
    hold on;
    plot(x(1:j),V_E(1:j),Color='r',LineWidth=4);  % 两条红线交织，就像两颗心
    plot(x(j),V_E(j),'*');  % 当前时刻，两颗心相遇
    plot(x(j),L_O(j),'*');  % 这就是爱情的力量！
    xlabel('x')
    ylabel('L_O V_E')  % 合在一起就是LOVE！
    frame = getframe(fig);
    im3{j} = frame2im(frame);
    disp("Figure"+num2str(j)+",Done");  % 双向奔赴第j步完成，距离完美爱情又近了一步
    close;
end

%% 🎬 生成爱情动画 - 见证三种不同的爱情结局

% 生成第一个悲剧：单方面付出的结果（没有灵魂）
% 这个GIF会告诉你，单恋是多么的...嗯，没有灵魂 😢
filename = 'L_o.gif'; 
for idx = 1:nImages
    [A,map] = rgb2ind(im1{idx},256);
    if idx == 1
        imwrite(A,map,filename,'gif','LoopCount',Inf,'DelayTime',0.1);  % 无限循环，就像单恋者的痛苦
    else
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',0.1);
    end
end

% 生成第二个悲剧：另一个单方面付出的结果（没有内涵）
% 这个GIF会告诉你，另一个单恋者也是...嗯，没有内涵 😭
filename = 'V_E.gif'; 
for idx = 1:nImages
    [A,map] = rgb2ind(im2{idx},256);
    if idx == 1
        imwrite(A,map,filename,'gif','LoopCount',Inf,'DelayTime',0.1);  % 无限循环，就像另一个单恋者的痛苦
    else
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',0.1);
    end
end

% 生成完美结局：双向奔赴的结果（有灵魂有内涵）💕
% 这个GIF会告诉你，真正的爱情是多么的美好！
filename = 'LOVE.gif'; 
for idx = 1:nImages
    [A,map] = rgb2ind(im3{idx},256);
    if idx == 1
        imwrite(A,map,filename,'gif','LoopCount',Inf,'DelayTime',0.1);  % 无限循环，就像永恒的爱情
    else
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',0.1);
    end
end

% 🎉 恭喜！你已经成功生成了三个爱情动画
% 现在你可以用这些GIF来证明：双向奔赴才是王道！
% 单身狗慎看，可能引起不适 😏