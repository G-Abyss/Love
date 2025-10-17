# 💕 Gen式双向奔赴理论 - 用数学证明爱情的力量 (Python版本)
# 警告：本代码仅供娱乐，使用前请确保有一颗相信爱情的心 ❤️

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from PIL import Image
import io
import matplotlib
import platform

# 设置中文字体支持
def setup_chinese_font():
    """设置中文字体支持，避免乱码问题"""
    try:
        if platform.system() == 'Windows':
            # Windows系统使用微软雅黑
            plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
        elif platform.system() == 'Darwin':
            # macOS系统使用苹方
            plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Arial Unicode MS', 'Arial']
        else:
            # Linux系统使用文泉驿
            plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Arial']
        
        # 设置字体大小和样式
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['figure.dpi'] = 100
        
        print("字体设置完成：支持中文显示")
        return True
    except Exception as e:
        print(f"字体设置失败，使用默认字体: {e}")
        return False

# 初始化字体设置
setup_chinese_font()

# 定义爱情的时间轴（从-2到2，就像从陌生到熟悉的过程）
x = np.arange(-2, 2.1, 0.1)  # 创建x轴数据，步长0.1
x[-1] = 2# 将x最后一个元素强制为2
n_images = len(x)  # 记录爱情路上的每一个瞬间

# 为三个不同的"爱情状态"准备存储空间
frames_1 = []  # 存储单方面付出的结果（没有灵魂）
frames_2 = []  # 存储另一个单方面付出的结果（没有内涵）
frames_3 = []  # 存储双向奔赴的完美结果（有灵魂有内涵）

# 核心理论：两个物体的运动方程
# L_O：代表"Love"中的"L"，象征着爱情的上半部分
L_O = np.sqrt(1 - (np.abs(x) - 1)**2)
# V_E：代表"Love"中的"E"，象征着爱情的下半部分
V_E = -3 * np.sqrt(1 - np.sqrt(np.abs(x) / 2))

print("开始生成爱情动画...")
print("正在见证三种不同的爱情结局...")

# 开始模拟爱情的发展过程，每一帧都是爱情路上的一个瞬间
for j in range(n_images):
    # 场景1：单方面付出的悲剧（L_O独自努力）
    # 这就像一个人单方面追求，结果...你懂的 😢
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x[:j+1], L_O[:j+1], color='blue', linewidth=4)  # 蓝色代表忧郁
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 1)
    ax.plot(x[j], L_O[j], '*', markersize=15, color='blue')  # 当前时刻的位置，就像单恋者的心
    ax.set_xlabel('x')
    ax.set_ylabel('L_O')
    ax.set_title('Single-sided Effort (No Soul)')
    ax.grid(True, alpha=0.3)
    
    # 保存当前帧
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    frames_1.append(Image.open(buf))
    plt.close(fig)
    
    # 场景2：另一个单方面付出的悲剧（V_E独自努力）
    # 这就像另一个人也在单方面追求，结果...还是悲剧 😭
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x[:j+1], V_E[:j+1], color='green', linewidth=4)  # 绿色代表...嗯，嫉妒？
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 0)
    ax.plot(x[j], V_E[j], '*', markersize=15, color='green')  # 另一个单恋者的心
    ax.set_xlabel('x')
    ax.set_ylabel('V_E')
    ax.set_title('Another Single-sided Effort (No Content)')
    ax.grid(True, alpha=0.3)
    
    # 保存当前帧
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    frames_2.append(Image.open(buf))
    plt.close(fig)
    
    # 场景3：双向奔赴的完美结局！💕
    # 这就是传说中的"双向奔赴"，两个人都努力，结果...完美！
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(x[:j+1], L_O[:j+1], color='red', linewidth=4)  # 红色代表热情和爱情
    ax.plot(x[:j+1], V_E[:j+1], color='red', linewidth=4)  # 两条红线交织，就像两颗心
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 1)
    ax.plot(x[j], V_E[j], '*', markersize=15, color='red')  # 当前时刻，两颗心相遇
    ax.plot(x[j], L_O[j], '*', markersize=15, color='red')  # 这就是爱情的力量！
    ax.set_xlabel('x')
    ax.set_ylabel('L_O V_E')  # 合在一起就是LOVE！
    ax.set_title('Two-way Love (Perfect Result)')
    ax.grid(True, alpha=0.3)
    
    # 保存当前帧
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    frames_3.append(Image.open(buf))
    plt.close(fig)
    
    # 进度提示：爱情路上第j步完成
    if (j + 1) % 10 == 0:
        print(f"双向奔赴第{j+1}步完成，距离完美爱情又近了一步...")

print("\n开始生成爱情动画 - 见证三种不同的爱情结局...")

# 生成第一个悲剧：单方面付出的结果（没有灵魂）
# 这个GIF会告诉你，单恋是多么的...嗯，没有灵魂 😢
print("正在生成第一个悲剧：单方面付出的结果...")
frames_1[0].save('L_o.gif', 
                save_all=True, 
                append_images=frames_1[1:], 
                duration=100,  # 每帧100ms，就像单恋者的痛苦
                loop=0)  # 无限循环，就像单恋者的痛苦

# 生成第二个悲剧：另一个单方面付出的结果（没有内涵）
# 这个GIF会告诉你，另一个单恋者也是...嗯，没有内涵 😭
print("正在生成第二个悲剧：另一个单方面付出的结果...")
frames_2[0].save('V_E.gif', 
                save_all=True, 
                append_images=frames_2[1:], 
                duration=100,  # 每帧100ms，就像另一个单恋者的痛苦
                loop=0)  # 无限循环，就像另一个单恋者的痛苦

# 生成完美结局：双向奔赴的结果（有灵魂有内涵）💕
# 这个GIF会告诉你，真正的爱情是多么的美好！
print("正在生成完美结局：双向奔赴的结果...")
frames_3[0].save('LOVE.gif', 
                save_all=True, 
                append_images=frames_3[1:], 
                duration=100,  # 每帧100ms，就像永恒的爱情
                loop=0)  # 无限循环，就像永恒的爱情

print("\n恭喜！你已经成功生成了三个爱情动画")
print("现在你可以用这些GIF来证明：双向奔赴才是王道！")
print("单身狗慎看，可能引起不适")
print("\n生成的文件：")
print("- L_o.gif: 单方面付出的结果（没有灵魂）")
print("- V_E.gif: 另一个单方面付出的结果（没有内涵）")
print("- LOVE.gif: 双向奔赴的完美结果（有灵魂有内涵）")
